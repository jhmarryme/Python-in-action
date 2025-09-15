from a2a.server.agent_execution import AgentExecutor
from openai import AsyncOpenAI
from typing import Literal, Optional, List, AsyncIterable, Dict, Any
import os
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.server.tasks import TaskUpdater
from a2a.utils import new_agent_text_message, new_task
from a2a.types import TaskState, Part, TextPart


# server是专家智能体，基本不用改变智能体原有的逻辑
class CodingAgent:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str,
        model: str = "qwen-plus",
        tool_choice: Literal["auto", "required", "none"] = "auto",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        enable_thinking: Optional[bool] = None,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.enable_thinking = enable_thinking
        self.tool_choice = tool_choice

        self.client = AsyncOpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )

    async def stream(
        self, messages: List[dict[str, str]]
    ) -> AsyncIterable[Dict[str, Any]]:
        system_prompt = [
            {
                "role": "system",
                "content": "你是一个代码助手，根据用户的输入，生成对应的代码。注意你只能写代码，遇到不是代码的问题需要你反问用户，让用户明确需求",
            }
        ]
        messages = system_prompt + messages

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stream=True,  # 代码问题必须流式输出！
            tool_choice=self.tool_choice,
        )
        collected_content = []

        async for chunk in response:
            if chunk.choices[0].delta.content:
                collected_content.append(chunk.choices[0].delta.content)
                yield {
                    "is_final_answer": False,
                    "content": chunk.choices[0].delta.content,
                }

        yield {
            "is_final_answer": True,
            "content": "".join(collected_content),
        }


class CodingAgentExecutor(AgentExecutor):
    def __init__(self, agent: CodingAgent) -> None:
        self.agent = agent

    # 必须实现execute和cancel方法
    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        # 给request对应的response

        message = {
            "role": "user" if context.message.role == "user" else "assistant",
            # "content": context.message.parts[0].root.text,
            "content": context.get_user_input(),
        }
        messages = [message]

        # 找到当前任务
        task = context.current_task
        if not task:
            task = new_task(context.message)
            context.current_task = task
            await event_queue.enqueue_event(task)
        updater = TaskUpdater(event_queue, task.id, task.context_id)

        try:
            # 解析了A2A Client发来的请求，就可以让Server智能体干活了，按照正常逻辑进行调用，需要注意执行过程和结束都需要跟Client保持通信，要不断更新当前任务的状态
            async for chunk in self.agent.stream(messages):
                is_final_answer = chunk.get("is_final_answer")
                content = chunk.get("content")
                if not is_final_answer:
                    await updater.update_status(
                        TaskState.working,
                        new_agent_text_message(
                            content,
                            task.context_id,
                            task.id,
                        ),
                    )
                else:
                    # 任务完成了，加一个工件artifact
                    await updater.add_artifact(
                        parts=[Part(root=TextPart(text=content))],
                        name="coding_result",
                        last_chunk=True,
                    )
                    await updater.complete()
                    break

        except Exception as e:
            await updater.update_status(
                TaskState.failed,
                new_agent_text_message(
                    str(e),
                    task.context_id,
                    task.id,
                ),
            )

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        raise Exception("cancel not supported")


if __name__ == "__main__":
    import asyncio

    async def main():
        coding_agent = CodingAgent(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            stream=True,
        )

        # 测试案例
        result = coding_agent.invoke_stream(
            [
                {
                    "role": "user",
                    "content": "写一个快速排序算法",
                }
            ]
        )
        async for chunk in result:
            print(chunk)

    asyncio.run(main())
