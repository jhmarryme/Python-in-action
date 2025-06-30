在本步骤中，将使用 Agent Development Kit (ADK) 构建一个智能体。这个智能体将是一个简单的天气查询机器人，能够根据用户的城市请求提供天气信息。将学习如何定义工具、创建智能体，以及如何运行智能体进行对话。
### 1. 定义工具

在 ADK 中，**工具 (Tool)** 是智能体可以用来执行特定任务的函数或服务。智能体通过调用这些工具来与外部世界交互或获取信息。

在这个天气查询智能体中，我们将定义一个名为 `get_weather` 的工具，它模拟了一个天气数据库，根据城市名称返回天气报告。

**文件:** `tutorials/agent_team/step_1/agent.py`
> **文档字符串至关重要！** 智能体的 LLM 严重依赖函数的**文档字符串**来理解：
> - 工具做什么
> - _何时使用它
> - 它需要什么参数（`city: str`）
> - 它返回什么信息
```python
# ... existing code ...

# @title 定义 get_weather 工具
def get_weather(city: str) -> dict:
    """获取指定城市的当前天气报告。

    Args:
        city (str): 城市名称（例如，"New York"、"London"、"Tokyo"）。

    Returns:
        dict: 包含天气信息的字典。
              包含一个 'status' 键（'success' 或 'error'）。
              如果是 'success'，包含 'report' 键与天气详情。
              如果是 'error'，包含 'error_message' 键。
    """
    # 最佳实践：记录工具执行以便于调试
    print(f"--- Tool: get_weather called for city: {city} ---")
    city_normalized = city.lower().replace(" ", "")  # 基本输入标准化

    # 为简单起见的模拟天气数据
    mock_weather_db = {
        "newyork": {"status": "success", "report": "纽约的天气是晴朗的，温度为 25°C。"},
        "london": {"status": "success", "report": "伦敦多云，温度为 15°C。"},
        "tokyo": {"status": "success", "report": "东京有小雨，温度为 18°C。"},
    }

    # 优化点：使用 dict.get() 更简洁地处理字典查找和默认值
    return mock_weather_db.get(
        city_normalized,
        {"status": "error", "error_message": f"抱歉，我没有 '{city}' 的天气信息。"}
    )

# ... existing code ...
```
*   `get_weather` 函数接受一个 `city` 参数，并返回一个字典，其中包含天气状态和报告（或错误信息）。
*   内部使用一个模拟数据库来提供预定义城市的天气。
### 2. 定义智能体

在 ADK 中，**智能体 (Agent)** 是应用程序的核心逻辑，它利用大型语言模型 (LLM) 进行推理，并可以调用定义的工具。

在这里，我们将创建一个名为  `root_agent` 的智能体。

**文件:** `tutorials/agent_team/step_1/agent.py`

```python
# ... existing code ...
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm  # For multi-model support

# @title 定义天气智能体
# 使用前面定义的模型常量之一
AGENT_MODEL = 'openai/qwen2.5-72b-instruct'

# ... existing code (get_weather function) ...

# @title 定义天气智能体
root_agent = Agent(
    name="weather_agent_v1",
    model=LiteLlm(model=AGENT_MODEL),  # 指定底层 LLM
    description="为特定城市提供天气信息。",  # 对于稍后的任务分配至关重要
    instruction="你是一个有用的天气助手。你的主要目标是提供当前天气报告。"
                "当用户询问特定城市的天气时，"
                "你必须使用 'get_weather' 工具查找信息。"
                "分析工具的响应：如果状态为 'error'，礼貌地告知用户错误信息。"
                "如果状态为 'success'，向用户清晰简洁地呈现天气 'report'。"
                "仅在提到城市进行天气请求时使用该工具。",
    tools=[get_weather],  # 使该工具可用于此智能体
)
# ... existing code ...
```

*   `name`: 智能体的唯一标识符。
*   `model`: 指定智能体将使用的底层 LLM。这里使用了 `LiteLlm` 并指定了 `openai/qwen2.5-72b-instruct` 模型。
*   `description`: 对智能体能力的简短描述，对于多智能体系统中的任务委托非常重要。
*   `instruction`: 智能体的核心指令，指导 LLM 如何执行任务，何时以及如何使用可用的工具。清晰的指令对于智能体的行为至关重要。
*   `tools`: 一个列表，包含此智能体可以使用的所有工具。在这里，我们将之前定义的 `get_weather` 工具添加到列表中。

### 3. 设置 Runner 和 Session Service
为了运行智能体并管理对话上下文，ADK 提供了 `Runner` 和 `SessionService`。
*   **`Runner`**: 引擎负责编排交互流程。它接受用户输入，将其路由到适当的智能体，根据智能体的逻辑管理对 LLM 和工具的调用，通过 `SessionService` 处理会话更新，并生成表示交互进展的事件。
*   **`SessionService`**: 负责管理不同用户和会话的对话历史和状态。`InMemorySessionService` 是一个简单的实现，将所有内容存储在内存中，适用于测试和简单的应用程序。它跟踪交换的消息。
**文件:** `tutorials/agent_team/step_1/run.py`

```python
# ... existing code ...
import asyncio

from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types  # For creating message Content/Parts

from tutorials.agent_team.step_1.agent import weather_agent

APP_NAME = "weather_tutorial_app"
USER_ID = "user_1"
SESSION_ID = "session_001"  # Using a fixed ID for simplicity


async def call_agent_async(query: str, runner: Runner):  
    """Sends a query to the agent and prints the final response."""  
    print(f"\n>>> User Query: {query}")  
  
    # Prepare the user's message in ADK format  
    content = types.Content(role='user', parts=[types.Part(text=query)])  
  
    final_response_text = "智能体没有产生最终响应。"  # 默认值  
  
    # 关键概念：run_async 执行智能体逻辑并产生事件。  
    # 我们遍历事件以找到最终答案。  
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):  
        # 你可以取消注释下面的行以查看执行期间的*所有*事件  
        # print(f"  [事件] 作者：{event.author}，类型：{type(event).__name__}，最终：{event.is_final_response()}，内容：{event.content}")  
  
        # 关键概念：is_final_response() 标记轮次的结束消息。  
        if event.is_final_response():  
            if event.content and event.content.parts:  
                # 假设第一部分中的文本响应  
                final_response_text = event.content.parts[0].text  
            elif event.actions and event.actions.escalate:  # 处理潜在错误/升级  
                final_response_text = f"智能体升级：{event.error_message or '无特定消息。'}"  
            # 如果需要，在这里添加更多检查（例如，特定错误代码）  
            break  # 找到最终响应后停止处理事件  
  
    print(f"<<< Agent Response: {final_response_text}")

# ... existing code ...
```

*   `call_agent_async` 函数负责向智能体发送用户查询并处理返回的事件流，直到找到最终响应。
*   `runner.run_async` 是核心方法，它执行智能体逻辑并返回一个异步迭代器，可以通过它获取智能体执行过程中的各种事件。
*   `event.is_final_response()` 用于识别对话轮次的最终输出。

### 4. 运行对话
现在，将把所有组件组合起来，运行一个实际的对话，并观察智能体的行为。
配置你的key：
```
# 设置为 False 以直接使用 API 密钥（多模型需要）  
GOOGLE_GENAI_USE_VERTEXAI=FALSE  
  
# --- 替换为你实际的密钥 ---
GOOGLE_API_KEY=
OPENAI_API_KEY=
OPENAI_API_BASE=https://dashscope.aliyuncs.com/compatible-mode/v1  
```
**文件:** `tutorials/agent_team/step_1/run.py`

```python
# ... existing code ...

async def run_conversation():  
    session_service = InMemorySessionService()  
    # Create the specific session where the conversation will happen  
    session = await session_service.create_session(  
        app_name=APP_NAME,  
        user_id=USER_ID,  
        session_id=SESSION_ID  
    )  
    print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")  
    runner = Runner(  
        agent=root_agent,  # The agent we want to run  
        app_name=APP_NAME,  # Associates runs with our app  
        session_service=session_service  # Uses our session manager  
    )  
    print(f"Runner created for agent '{runner.agent.name}'.")  
    await call_agent_async("london的天气如何？", runner)  
    await call_agent_async("告诉我newyork的天气", runner)  
    await call_agent_async("巴黎怎么样？", runner)  # 期望工具的错误消息  
  
if __name__ == "__main__":  
    asyncio.run(run_conversation())
```
*   `run_conversation` 函数初始化 `InMemorySessionService` 和 `Runner`。
*   它创建了一个新的会话，用于存储对话上下文。
*   最后，它通过 `call_agent_async` 发送了几个查询来测试智能体的响应：
    *   **“london的天气如何？”**：智能体将使用 `get_weather` 工具并返回伦敦的天气信息。
    *   **“告诉我newyork的天气”**：智能体将使用 `get_weather` 工具并返回纽约的天气信息。
    *   **“巴黎怎么样？”**：由于 `get_weather` 工具没有“巴黎”的天气信息，智能体将处理工具返回的错误信息并礼貌地回应用户。
```
Session created: App='weather_tutorial_app', User='user_1', Session='session_001'
Runner created for agent 'weather_agent_v1'.

>>> User Query: london的天气如何？
--- Tool: get_weather called for city: london ---
<<< Agent Response: 伦敦目前是多云天气，温度为 15°C。

>>> User Query: 告诉我newyork的天气
--- Tool: get_weather called for city: newyork ---
<<< Agent Response: 纽约现在的天气是晴朗的，温度为 25°C。

>>> User Query: 巴黎怎么样？
--- Tool: get_weather called for city: 巴黎 ---
<<< Agent Response: 对不起，我目前无法获取到巴黎的天气信息。请稍后再试或尝试其他城市。

```
---
### 5. web运行
使用自带的web端页面运行agent，不需要设置 Runner 和 Session Service。
只需要切换目录后执行`adk web`即可。
```
agent_team/      <-- 切换到此目录
    step_1/
        __init__.py
        agent.py
        .env
```

### 总结
*   **定义了一个工具：** `get_weather`，它是一个模拟天气查询的函数。
*   **创建了一个智能体：** `weather_agent`，它被配置为使用 `get_weather` 工具。
*   **设置了运行环境：** 使用 `Runner` 和 `InMemorySessionService` 来运行智能体并管理会话。
*   **进行了交互测试：** 向智能体发送了多个查询，并观察了其如何通过工具获取信息并做出响应，包括处理工具的错误情况。
* 
这是构建更复杂、多功能智能体应用程序的基础。