from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

AGENT_MODEL = 'openai/qwen2.5-72b-instruct'


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
    city_normalized = city.lower().replace(" ", "")

    mock_weather_db = {
        "newyork": {"status": "success", "report": "纽约的天气是晴朗的，温度为 25°C。"},
        "london": {"status": "success", "report": "伦敦多云，温度为 15°C。"},
        "tokyo": {"status": "success", "report": "东京有小雨，温度为 18°C。"},
    }

    return mock_weather_db.get(
        city_normalized,
        {"status": "error", "error_message": f"抱歉，我没有 '{city}' 的天气信息。"}
    )


root_agent = Agent(
    name="evaluate_weather_agent",
    model=LiteLlm(model=AGENT_MODEL),
    description="用于演示 ADK 评估的简单天气智能体。",
    instruction=(
        "你是一个有用的天气助手。当用户询问特定城市的天气时，"
        "必须使用 'get_weather' 工具。根据工具返回：如果是 'error'，"
        "礼貌地说明未知；如果是 'success'，清晰给出 report。仅在明确城市时调用工具。"
    ),
    tools=[get_weather],
)
