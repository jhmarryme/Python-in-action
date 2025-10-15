import asyncio

from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from .agent import root_agent

APP_NAME = "evaluate_tutorial_app"
USER_ID = "user_eval_root"
SESSION_ID = "session_eval_root_001"


async def call_agent_async(query: str, runner: Runner):
    print(f"\n>>> User Query: {query}")
    content = types.Content(role='user', parts=[types.Part(text=query)])
    final_text = "(无最终响应)"

    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break

    print(f"<<< Agent Response: {final_text}")


async def run_conversation():
    session_service = InMemorySessionService()
    await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

    await call_agent_async("What's the weather in London?", runner)
    await call_agent_async("Tell me the weather in New York", runner)
    await call_agent_async("天气怎么样？", runner)


if __name__ == "__main__":
    asyncio.run(run_conversation())
