# @title 导入必要的库
import asyncio

from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types  # For creating message Content/Parts

# 从当前目录导入根智能体
from agent import root_agent

# 定义用于标识交互上下文的常量
APP_NAME_STATEFUL = "weather_tutorial_stateful_app"
USER_ID_STATEFUL = "user_stateful_1"
SESSION_ID_STATEFUL = "session_stateful_001"


# @title 定义智能体交互函数
async def call_agent_async(query: str, runner: Runner, user_id: str, session_id: str):
    """Sends a query to the agent and prints the final response."""
    print(f"\n>>> User Query: {query}")

    content = types.Content(role='user', parts=[types.Part(text=query)])

    final_response_text = "智能体没有产生最终响应。"  # Default fallback

    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        # 你可以取消注释下面的行以查看执行期间的*所有*事件
        # print(f"  [事件] 作者：{event.author}，类型：{type(event).__name__}，最终：{event.is_final_response()}，内容：{event.content}")

        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = f"智能体升级：{event.error_message or '无特定消息。'}"
            break

    print(f"<<< Agent Response: {final_response_text}")


# @title 运行会话状态示例
async def run_stateful_conversation():
    print("\n--- 测试会话状态 ---")
    session_service_stateful = InMemorySessionService()

    # 初始化会话，可以设置初始状态
    initial_session_state = {
        "user_preference_temperature_unit": "Celsius",  # 默认摄氏度
    }

    session_stateful = await session_service_stateful.create_session(
        app_name=APP_NAME_STATEFUL,
        user_id=USER_ID_STATEFUL,
        session_id=SESSION_ID_STATEFUL,
        state=initial_session_state  # 设置初始状态
    )
    print(
        f"会话已创建：App='{APP_NAME_STATEFUL}', User='{USER_ID_STATEFUL}', Session='{SESSION_ID_STATEFUL}'，初始状态：{session_stateful.state}")

    runner_stateful = Runner(
        agent=root_agent,
        app_name=APP_NAME_STATEFUL,
        session_service=session_service_stateful
    )
    print(f"已为智能体 '{root_agent.name}' 创建运行器。")

    # 1. 初始查询 (使用默认的摄氏度)
    await call_agent_async(
        "告诉我伦敦的天气。",
        runner=runner_stateful,
        user_id=USER_ID_STATEFUL,
        session_id=SESSION_ID_STATEFUL
    )
    #
    stored_session = session_service_stateful.sessions[APP_NAME_STATEFUL][USER_ID_STATEFUL][SESSION_ID_STATEFUL]
    stored_session.state["user_preference_temperature_unit"] = "Fahrenheit"

    # 检查会话状态是否更新
    current_session = await session_service_stateful.get_session(
        app_name=APP_NAME_STATEFUL,
        user_id=USER_ID_STATEFUL,
        session_id=SESSION_ID_STATEFUL
    )
    if current_session:
        print(f"\n--- 会话当前状态 (手动设置后): {current_session.state}")
    else:
        print("\n❌ 错误: 无法获取会话状态。")

    # 2. 手动设置偏好后查询纽约天气
    await call_agent_async(
        "告诉我纽约的天气。",
        runner=runner_stateful,
        user_id=USER_ID_STATEFUL,
        session_id=SESSION_ID_STATEFUL
    )
    # 3. 测试基础的agent是否正常
    await call_agent_async(
        "再见",
        runner=runner_stateful,
        user_id=USER_ID_STATEFUL,
        session_id=SESSION_ID_STATEFUL
    )


if __name__ == "__main__":
    asyncio.run(run_stateful_conversation())
