# @title 导入必要的库

from typing import Optional

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.tool_context import ToolContext

# @title 定义模型常量
AGENT_MODEL = 'openai/qwen2.5-72b-instruct'


# @title 为问候和告别智能体定义工具 (沿用 Step 2)
def say_hello(name: Optional[str] = None) -> str:
    """提供简单的问候。如果提供姓名，将使用它。

    Args:
        name (str, optional): 要问候的人的姓名。如果未提供，默认为通用问候。

    Returns:
        str: 友好的问候消息。
    """
    if name:
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


# @title 创建状态感知天气工具
def get_weather_stateful(city: str, tool_context: ToolContext) -> dict:
    """获取指定城市的当前天气报告，并根据会话状态调整温度单位。

    Args:
        city (str): 城市名称（例如，"New York"、"London"、"Tokyo"）。
        tool_context (ToolContext): 提供对当前会话状态的访问。

    Returns:
        dict: 包含天气信息的字典。
              包含一个 'status' 键（'success' 或 'error'）。
              如果是 'success'，包含 'report' 键与天气详情。
              如果是 'error'，包含 'error_message' 键。
    """
    print(f"--- 工具: get_weather_stateful called for city: {city} ---")
    city_normalized = city.lower().replace(" ", "")

    # 从会话状态中获取温度单位偏好
    preferred_unit = tool_context.state.get("user_preference_temperature_unit", "Celsius")
    print(f"--- 从会话状态读取温度单位: {preferred_unit} ---")

    # 模拟天气数据（内部始终以摄氏度存储）
    mock_weather_db = {
        "newyork": {"temp_c": 25, "condition": "sunny"},
        "london": {"temp_c": 15, "condition": "cloudy"},
        "tokyo": {"temp_c": 18, "condition": "light rain"},
        "纽约": {"temp_c": 25, "condition": "sunny"},
        "伦敦": {"temp_c": 15, "condition": "cloudy"},
        "东京": {"temp_c": 18, "condition": "light rain"},
    }

    if city_normalized in mock_weather_db:
        data = mock_weather_db[city_normalized]
        temp_c = data["temp_c"]
        condition = data["condition"]

        # 根据状态偏好格式化温度
        if preferred_unit == "Fahrenheit":
            temp_value = (temp_c * 9 / 5) + 32  # 计算华氏度
            temp_unit = "°F"
        else:  # 默认为摄氏度
            temp_value = temp_c
            temp_unit = "°C"

        report = f"{city.capitalize()} 的天气是 {condition}，温度为 {temp_value:.0f}{temp_unit}。"
        result = {"status": "success", "report": report}
        print(f"--- 工具：以 {preferred_unit} 生成报告。结果：{result} ---")

        # 写入状态的示例（此工具可选）
        tool_context.state["last_city_checked_stateful"] = city
        print(f"--- 工具：更新状态 'last_city_checked_stateful'：{city} ---")

        return result
    else:
        # 处理未找到的城市
        error_msg = f"抱歉，我没有 '{city}' 的天气信息。"
        print(f"--- 工具：未找到城市 '{city}'。---")
        return {"status": "error", "error_message": error_msg}


# @title 定义问候和告别子智能体 (沿用 Step 2)
greeting_agent = Agent(
    model=LiteLlm(model=AGENT_MODEL),
    name="greeting_agent",
    instruction="你是问候智能体。你的唯一任务是为用户提供友好的问候。"
                "使用 'say_hello' 工具生成问候。"
                "如果用户提供了他们的姓名，确保将其传递给工具。"
                "不要参与任何其他对话或任务。",
    description="使用 'say_hello' 工具处理简单问候和你好。",
    tools=[say_hello],
)
print(f"✅ 智能体 '{greeting_agent.name}' 已使用模型 '{AGENT_MODEL}' 创建。")

farewell_agent = Agent(
    model=LiteLlm(model=AGENT_MODEL),
    name="farewell_agent",
    instruction="你是告别智能体。你的唯一任务是提供礼貌的再见消息。"
                "当用户表示他们要离开或结束对话时使用 'say_goodbye' 工具"
                "（例如，使用再见、谢谢再见、回头见等词语）。"
                "不要执行任何其他操作。",
    description="使用 'say_goodbye' 工具处理简单的告别和再见。",
    tools=[say_goodbye],
)
print(f"✅ 智能体 '{farewell_agent.name}' 已使用模型 '{AGENT_MODEL}' 创建。")

# @title 定义根智能体 (集成子智能体和状态感知工具)
root_agent = Agent(
    name="root_agent_stateful",
    model=LiteLlm(model=AGENT_MODEL),
        description="Main agent: Provides weather (state-aware unit), delegates greetings/farewells., saves report to state.",
        instruction="You are the main Weather Agent. Your job is to provide weather using 'get_weather_stateful'. "
                    "The tool will format the temperature based on user preference stored in state. "
                    "Delegate simple greetings to 'greeting_agent' and farewells to 'farewell_agent'. "
                    "Handle only weather requests, greetings, and farewells.",
    tools=[get_weather_stateful],
    sub_agents=[greeting_agent, farewell_agent],
    output_key="last_weather_report"
)
print(f"✅ 智能体 '{root_agent.name}' 已使用模型 '{AGENT_MODEL}' 创建。")
