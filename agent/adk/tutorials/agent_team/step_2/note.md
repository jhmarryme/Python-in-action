在本步骤中，我们将扩展之前的天气查询智能体，创建一个由多个专门智能体组成的团队：
1. 为处理问候（`say_hello`）和告别（`say_goodbye`）创建简单工具。
2. 创建两个新的专门子智能体：`greeting_agent` 和 `farewell_agent`。
3. 更新我们的主要天气智能体（`weather_agent_v2`）作为**根智能体**。
4. 配置根智能体及其子智能体，实现**自动委托**。
5. 通过发送不同类型的请求来测试委托流程
为什么构建智能体团队？
- 模块化：更容易开发、测试和维护各个智能体。
- 专业化：每个智能体可以根据其特定任务进行微调（指令、模型选择）。
- 可扩展性：通过添加新智能体来更容易地添加新功能。
- 效率：允许使用更简单/更便宜的模型来处理更简单任务（如问候）。
### 1. 定义工具
我们将为不同的智能体定义专门的工具：
**文件:** `tutorials/agent_team/step_2/agent.py`
```python
# @title 为问候和告别智能体定义工具  
def say_hello(name: Optional[str] = None) -> str:  
    """提供简单的问候。如果提供姓名，将使用它。  
  
    Args:        name (str, optional): 要问候的人的姓名。如果未提供，默认为通用问候。  
  
    Returns:        str: 友好的问候消息。  
    """    if name:  
        greeting = f"你好，{name}！"  
        print(f"--- 工具：say_hello 被调用，姓名：{name} ---")  
    else:  
        greeting = "你好！"  # 如果姓名为 None 或未明确传递时的默认问候  
        print(f"--- 工具：say_hello 被调用，无特定姓名（姓名参数值：{name}）---")  
    return greeting  
  
  
def say_goodbye() -> str:  
    """提供简单的告别消息来结束对话。"""  
    print(f"--- 工具：say_goodbye 被调用 ---")  
    return "再见！祝你有美好的一天。"  
  
  
# @title 定义 get_weather 工具 (沿用 Step 1 并优化)  
def get_weather(city: str) -> dict:  
    """获取指定城市的当前天气报告。  
  
    Args:        city (str): 城市名称（例如，"New York"、"London"、"Tokyo"）。  
  
    Returns:        dict: 包含天气信息的字典。  
              包含一个 'status' 键（'success' 或 'error'）。  
              如果是 'success'，包含 'report' 键与天气详情。  
              如果是 'error'，包含 'error_message' 键。  
    """    print(f"--- 工具: get_weather called for city: {city} ---")  
    city_normalized = city.lower().replace(" ", "")  # 基本输入标准化  
  
    # 优化点：添加中文城市名作为键，以匹配LLM可能提取的中文城市名  
    mock_weather_db = {  
        "纽约": {"status": "success", "report": "纽约的天气是晴朗的，温度为 25°C。"},  
        "伦敦": {"status": "success", "report": "伦敦多云，温度为 15°C。"},  
        "东京": {"status": "success", "report": "东京有小雨，温度为 18°C。"},  
    }  
  
    return mock_weather_db.get(  
        city_normalized,  
        {"status": "error", "error_message": f"抱歉，我没有 '{city}' 的天气信息。"}  
    )
```
### 2. 定义子智能体
使用的模型统一为`qwen2.5-72b-instruct`，不同的模型能力不同，较老的模型可能会导致一些未知的问题，比如`qwen-plus`会导致根智能体无法正常调用子智能体的能力。
**文件:** `tutorials/agent_team/step_2/agent.py`
```
AGENT_MODEL = 'openai/qwen2.5-72b-instruct'
```
我们将创建两个专门的子智能体来处理问候和告别：
```python
# @title 定义问候和告别子智能体  
# --- 问候智能体 ---greeting_agent = Agent(  
    # 为简单任务使用潜在不同/更便宜的模型  
    model=LiteLlm(model=AGENT_MODEL),  
    name="greeting_agent",  
    instruction="你是问候智能体。你的唯一任务是为用户提供友好的问候。"  
                "使用 'say_hello' 工具生成问候。"  
                "如果用户提供了他们的姓名，确保将其传递给工具。"  
                "不要参与任何其他对话或任务。",  
    description="使用 'say_hello' 工具处理简单问候和你好。",  # 对委托至关重要  
    tools=[say_hello],  
)  
print(f"✅ 智能体 '{greeting_agent.name}' 已使用模型 '{AGENT_MODEL}' 创建。")  
  
# --- 告别智能体 ---farewell_agent = Agent(  
    # 可以使用相同或不同的模型  
    model=LiteLlm(model=AGENT_MODEL),  # 此示例继续使用 GPT    name="farewell_agent",  
    instruction="你是告别智能体。你的唯一任务是提供礼貌的再见消息。"  
                "当用户表示他们要离开或结束对话时使用 'say_goodbye' 工具"  
                "（例如，使用再见、谢谢再见、回头见等词语）。"  
                "不要执行任何其他操作。",  
    description="使用 'say_goodbye' 工具处理简单的告别和再见。",  # 对委托至关重要  
    tools=[say_goodbye],  
)  
print(f"✅ 智能体 '{farewell_agent.name}' 已使用模型 '{AGENT_MODEL}' 创建。")
```
- 子智能体 `description` 字段应该准确且简洁地总结他们的特定功能。这对于有效自动委托至关重要。
- 子智能体 `instruction` 字段应该针对他们的有限范围，告诉他们具体要做什么，_什么不要做_（例如，"你的唯一任务是..."）。
### 3. 定义根智能体
根智能体作为团队协调者，负责处理天气查询并将其他任务委托给专门的子智能体：
> 自动委托（自动流程）通过提供 `sub_agents` 列表，ADK 实现了自动委托。当根智能体收到用户查询时，它的 LLM 不仅考虑其自身的指令和工具，还考虑每个子智能体的 `description`。
> 如果 LLM 确定查询与子智能体描述的能力（例如，"处理简单问候"）相符，它将自动生成一个特殊的内部动作，将控制权转移到该子智能体，以便该轮次。子智能体然后使用自己的模型、指令和工具处理查询。

**文件:** `tutorials/agent_team/step_2/agent.py`
```python
# @title 定义根智能体 (集成子智能体和天气工具)  
root_agent = Agent(  
    name="root_agent",  # 给它一个新的版本名称  
    model=LiteLlm(model=AGENT_MODEL),  
    description="主要协调智能体。处理天气请求并将问候/告别委托给专家。",  
    instruction="你是协调团队的主要天气智能体。你的主要职责是提供天气信息。"  
                "仅对特定天气请求使用 'get_weather' 工具（例如，'伦敦的天气'）。"  
                "你有专门的子智能体："  
                "1. 'greeting_agent'：处理像'嗨'、'你好'这样的简单问候。将此类委托给它。"  
                "2. 'farewell_agent'：处理像'再见'、'回头见'这样的简单告别。将此类委托给它。"  
                "分析用户的查询。如果是问候，委托给 'greeting_agent'。如果是告别，委托给 'farewell_agent'。"  
                "如果是天气请求，使用 'get_weather' 自己处理。"  
                "对于其他任何事情，适当回应或说明你无法处理。",  
    tools=[get_weather],  # 根智能体仍需要天气工具用于其核心任务  
    # 关键变化：在这里链接子智能体！  
    sub_agents=[greeting_agent, farewell_agent]  
)
```
- - 添加 `sub_agents` 参数：我们传递一个包含刚刚创建的 `greeting_agent` 和 `farewell_agent` 实例的列表。
- - 更新 `instruction`：我们明确告诉根智能体_关于_它的子智能体以及_何时_应该将任务委托给它们。
### 4. 运行团队对话
**文件:** `tutorials/agent_team/step_2/run.py`
```python
async def call_agent_async(query: str, runner: Runner, user_id: str, session_id: str):  
    """Sends a query to the agent and prints the final response."""  
    print(f"\n>>> User Query: {query}")  
  
    content = types.Content(role='user', parts=[types.Part(text=query)])  
  
    final_response_text = "智能体没有产生最终响应。"  # Default fallback  
  
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):  
        # You can uncomment the line below to see *all* events during execution  
        # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")  
        # Key Concept: is_final_response() marks the concluding message for the turn.        if event.is_final_response():  
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
  
    # --- 获取实际根智能体对象 ---    # 创建特定于此智能体团队测试的运行器  
    runner_agent_team = Runner(  
        agent=root_agent,  # 使用根智能体对象  
        app_name=APP_NAME,  # 使用特定的应用名称  
        session_service=session_service  # 使用特定的会话服务  
    )  
    print(f"已为智能体 '{root_agent.name}' 创建运行器。")  
  
    # 总是通过根智能体的运行器交互，传递正确的 ID    await call_agent_async("你好！",  
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
```
运行流程：
1. "你好！" 查询进入 `runner_agent_team`。
2. 根智能体（`weather_agent_team`）收到它并根据其指令和 `greeting_agent` 的描述将任务委托给 `greeting_agent`。
3. `greeting_agent` 处理查询，调用其 `say_hello` 工具并生成响应。
4. "纽约的天气如何？" 查询_未_委托给根智能体，而是直接由根智能体使用其 `get_weather` 工具处理。
5. "谢谢，再见！" 查询委托给 `farewell_agent`，它使用其 `say_goodbye` 工具。
```
✅ 智能体 'greeting_agent' 已使用模型 'openai/qwen2.5-72b-instruct' 创建。
✅ 智能体 'farewell_agent' 已使用模型 'openai/qwen2.5-72b-instruct' 创建。

--- 测试智能体团队委托 ---
会话已创建：App='weather_tutorial_agent_team'，User='user_1_agent_team'，Session='session_001_agent_team'
已为智能体 'root_agent' 创建运行器。

>>> User Query: 你好！
--- 工具：say_hello 被调用，无特定姓名（姓名参数值：None）---
<<< Agent Response: 你好！

>>> User Query: 纽约的天气如何？
--- 工具: get_weather called for city: 纽约 ---
<<< Agent Response: 纽约的天气是晴朗的，温度为 25°C。

>>> User Query: 谢谢，再见！
--- 工具：say_goodbye 被调用 ---
<<< Agent Response: 再见！祝你有美好的一天。

```
### 5. web运行
使用自带的web端页面运行agent，不需要设置 Runner 和 Session Service。
只需要切换目录后执行`adk web`即可。
```
agent_team/      <-- 切换到此目录
    step_2/
        __init__.py
        agent.py
        .env
```

### 总结
* **定义了专门的工具：** 为不同任务创建了专门的工具（`say_hello`、`say_goodbye`、`get_weather`）。
* **创建了子智能体：** 实现了两个专门的子智能体（`greeting_agent` 和 `farewell_agent`）来处理特定任务。
* **实现了根智能体：** 创建了一个协调者智能体，它可以根据任务类型将请求委托给适当的子智能体。
* **测试了团队协作：** 通过发送不同类型的查询（问候、天气查询、告别）来测试智能体团队的协作能力。