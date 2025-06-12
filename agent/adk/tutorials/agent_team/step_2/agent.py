from typing import Optional

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from sub_agent import greeting_agent, farewell_agent

# @title 定义模型常量
AGENT_MODEL = 'openai/qwen2.5-72b-instruct'


# @title 为问候和告别智能体定义工具
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


# @title 定义 get_weather 工具 (沿用 Step 1 并优化)
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
    print(f"--- Tool: get_weather called for city: {city} ---")
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

# @title 定义问候和告别子智能体
# --- 问候智能体 ---
greeting_agent = Agent(
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

# --- 告别智能体 ---
farewell_agent = Agent(
    # 可以使用相同或不同的模型
    model=LiteLlm(model=AGENT_MODEL),  # 此示例继续使用 GPT
    name="farewell_agent",
    instruction="你是告别智能体。你的唯一任务是提供礼貌的再见消息。"
                "当用户表示他们要离开或结束对话时使用 'say_goodbye' 工具"
                "（例如，使用再见、谢谢再见、回头见等词语）。"
                "不要执行任何其他操作。",
    description="使用 'say_goodbye' 工具处理简单的告别和再见。",  # 对委托至关重要
    tools=[say_goodbye],
)
print(f"✅ 智能体 '{farewell_agent.name}' 已使用模型 '{AGENT_MODEL}' 创建。")
