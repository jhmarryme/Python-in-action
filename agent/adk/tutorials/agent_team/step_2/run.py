# @title Define Agent Interaction Function
import asyncio

from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types  # For creating message Content/Parts

from agent import root_agent


async def call_agent_async(query: str, runner: Runner, user_id: str, session_id: str):
    """Sends a query to the agent and prints the final response."""
    print(f"\n>>> User Query: {query}")

    content = types.Content(role='user', parts=[types.Part(text=query)])

    final_response_text = "智能体没有产生最终响应。"  # Default fallback

    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        # You can uncomment the line below to see *all* events during execution
        # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")

        # Key Concept: is_final_response() marks the concluding message for the turn.
        if event.is_final_response():
            if event.content and event.content.parts:
                # Assuming text response in the first part
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:  # Handle potential errors/escalations
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            # Add more checks here if needed (e.g., specific error codes)
            break  # Stop processing events once the final response is found

    print(f"<<< Agent Response: {final_response_text}")


async def run_team_conversation():
    print("\n--- 测试智能体团队委托 ---")
    # InMemorySessionService 是本教程的简单、非持久存储。
    session_service = InMemorySessionService()

    # 定义用于标识交互上下文的常量
    APP_NAME = "weather_tutorial_agent_team"
    USER_ID = "user_1_agent_team"
    SESSION_ID = "session_001_agent_team"
    session = await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    print(f"会话已创建：App='{APP_NAME}'，User='{USER_ID}'，Session='{SESSION_ID}'")

    # --- 获取实际根智能体对象 ---
    # 使用确定的变量名称

    # 创建特定于此智能体团队测试的运行器
    runner_agent_team = Runner(
        agent=root_agent,  # 使用根智能体对象
        app_name=APP_NAME,  # 使用特定的应用名称
        session_service=session_service  # 使用特定的会话服务
    )
    # 更正打印语句以显示实际根智能体的名称
    print(f"已为智能体 '{root_agent.name}' 创建运行器。")

    # 总是通过根智能体的运行器交互，传递正确的 ID
    await call_agent_async("你好！",
                           runner=runner_agent_team,
                           user_id=USER_ID,
                           session_id=SESSION_ID)
    await call_agent_async("纽约的天气如何？",
                           runner=runner_agent_team,
                           user_id=USER_ID,
                           session_id=SESSION_ID)
    await call_agent_async("谢谢，再见！",
                           runner=runner_agent_team,
                           user_id=USER_ID,
                           session_id=SESSION_ID)


if __name__ == "__main__":
    asyncio.run(run_team_conversation())
