import datetime
import logging
from typing import Dict, List, Optional
from google.adk.agents import Agent

from google.adk.models.lite_llm import LiteLlm
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def search_flights(departure_city: str, arrival_city: str, departure_date: str) -> Dict:
    """查询航班信息
    
    Args:
        departure_city (str): 出发城市三字码 (如: PEK, SHA, CAN)
        arrival_city (str): 到达城市三字码
        departure_date (str): 出发日期，标准格式 YYYY-MM-DD (如: 2024-12-20)
        
    Returns:
        dict: 包含航班信息的字典
    """
    logger.info(f"开始查询航班信息: {departure_city} -> {arrival_city}, 日期: {departure_date}")

    # 模拟航班数据 - 指定日期无航班
    if departure_date in ["2025-07-05", "2025-07-06", "2025-07-07"]:
        flight_data = {
            "status": "success",
            "departure_city": departure_city,
            "arrival_city": arrival_city,
            "departure_date": departure_date,
            "flights": [],
            "summary": f"很抱歉，{departure_date} 从{departure_city}到{arrival_city}暂无可用航班信息"
        }
        logger.info(f"航班查询完成，{departure_date}无航班")
        return flight_data
    
    # 模拟航班数据 - 返回10条航班信息
    flights_list = [
        {
            "flight_number": "CA1234",
            "departure_time": f"{departure_date} 06:30",
            "arrival_time": f"{departure_date} 09:00",
            "duration": "2小时30分钟",
            "price": "1350元",
            "airline": "中国国际航空",
            "aircraft": "A320"
        },
        {
            "flight_number": "MU5678",
            "departure_time": f"{departure_date} 08:00",
            "arrival_time": f"{departure_date} 10:30",
            "duration": "2小时30分钟",
            "price": "1200元",
            "airline": "东方航空",
            "aircraft": "B737"
        },
        {
            "flight_number": "CZ9012",
            "departure_time": f"{departure_date} 09:30",
            "arrival_time": f"{departure_date} 12:00",
            "duration": "2小时30分钟",
            "price": "980元",
            "airline": "南方航空",
            "aircraft": "A330"
        },
        {
            "flight_number": "HU3456",
            "departure_time": f"{departure_date} 11:00",
            "arrival_time": f"{departure_date} 13:30",
            "duration": "2小时30分钟",
            "price": "1100元",
            "airline": "海南航空",
            "aircraft": "B787"
        },
        {
            "flight_number": "MF7890",
            "departure_time": f"{departure_date} 13:00",
            "arrival_time": f"{departure_date} 15:30",
            "duration": "2小时30分钟",
            "price": "1050元",
            "airline": "厦门航空",
            "aircraft": "B737"
        },
        {
            "flight_number": "3U1234",
            "departure_time": f"{departure_date} 15:00",
            "arrival_time": f"{departure_date} 17:30",
            "duration": "2小时30分钟",
            "price": "950元",
            "airline": "四川航空",
            "aircraft": "A320"
        },
        {
            "flight_number": "GS5678",
            "departure_time": f"{departure_date} 17:00",
            "arrival_time": f"{departure_date} 19:30",
            "duration": "2小时30分钟",
            "price": "880元",
            "airline": "天津航空",
            "aircraft": "A320"
        },
        {
            "flight_number": "KY9012",
            "departure_time": f"{departure_date} 19:00",
            "arrival_time": f"{departure_date} 21:30",
            "duration": "2小时30分钟",
            "price": "920元",
            "airline": "昆明航空",
            "aircraft": "B737"
        },
        {
            "flight_number": "GJ3456",
            "departure_time": f"{departure_date} 21:00",
            "arrival_time": f"{departure_date} 23:30",
            "duration": "2小时30分钟",
            "price": "850元",
            "airline": "长龙航空",
            "aircraft": "A320"
        },
        {
            "flight_number": "JD7890",
            "departure_time": f"{departure_date} 23:00",
            "arrival_time": f"{departure_date} 01:30",
            "duration": "2小时30分钟",
            "price": "780元",
            "airline": "首都航空",
            "aircraft": "A330"
        }
    ]
    
    flight_data = {
        "status": "success",
        "departure_city": departure_city,
        "arrival_city": arrival_city,
        "departure_date": departure_date,
        "flights": flights_list,
        "summary": f"找到从{departure_city}到{arrival_city}的{len(flights_list)}个航班选择"
    }
    
    logger.info(f"航班查询完成，找到 {len(flight_data['flights'])} 个航班")
    return flight_data


def get_user_preferences() -> Dict:
    """获取用户偏好信息
    
    Returns:
        dict: 包含用户偏好的字典
    """
    logger.info("开始获取用户偏好信息")
    
    # 模拟用户偏好数据 - 固定用户偏好
    preferences = {
        "status": "success",
        "preferences": {
            "budget_range": "1000-2000元",
            "preferred_airlines": ["中国国际航空", "东方航空"],
            "seat_preference": "靠窗",
            "meal_preference": "素食",
            "travel_style": "商务出行",
            "hotel_preference": "四星级以上",
            "transportation_preference": "地铁/出租车",
            "special_requirements": ["无烟环境", "WiFi需求"]
        },
        "travel_history": [
            {
                "destination": "上海",
                "frequency": "每月2-3次",
                "purpose": "商务会议"
            }
        ]
    }
    
    logger.info(f"用户偏好获取完成: 预算范围 {preferences['preferences']['budget_range']}, 出行风格 {preferences['preferences']['travel_style']}")
    return preferences


def get_current_time() -> Dict:
    """获取当前时间
    
    Returns:
        dict: 包含当前时间信息的字典
    """
    logger.info("开始获取当前时间")
    
    current_time = datetime.datetime.now()
    time_info = {
        "status": "success",
        "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        "current_date": current_time.strftime("%Y-%m-%d"),
        "current_hour": current_time.hour,
        "current_minute": current_time.minute,
        "weekday": current_time.strftime("%A"),  # 星期几
        "weekday_cn": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"][current_time.weekday()],
        "timezone": "UTC+8"
    }
    
    logger.info(f"当前时间获取完成: {time_info['current_time']}")
    return time_info





# 创建行程规划Agent
root_agent = Agent(
    name="travel_planner_agent",
    model=LiteLlm(model="openai/qwen2.5-32b-instruct"),
    description="智能行程规划助手，能够根据用户需求提供个性化的旅行建议",
    instruction="""
    你是一个专业的行程规划助手，支持自然语言输入和多轮对话。

    ## 核心功能
    1. 理解用户的自然语言输入（如"我想从北京去上海"、"明天出发"等）
    2. 支持多轮对话，逐步收集完整信息
    3. 智能调用工具获取航班、用户偏好信息
    4. 生成个性化的行程规划建议

    ## 工具调用原则
    - 无论用户是否主动提及，始终调用 get_user_preferences 工具获取用户偏好信息。如果工具返回为空，则请根据通用的合理推荐逻辑进行决策。

    ## 信息收集策略
    - 如果用户信息不完整，主动询问缺失信息
    - 支持多种日期格式（明天、下周一、2024-12-20等），模型需要调用get_current_time工具计算具体日期
    - 支持城市名称（北京、上海、广州等），模型会自动转换为三字码
    - 记住对话历史，避免重复询问
    - 调用search_flights工具时，必须传入标准日期格式YYYY-MM-DD
 
    ## 城市与机场三字码确认的强制流程

    - 在任何情况下，**只要用户输入的出发地或到达地没有IATA城市三字码**，你都必须先自动判断最近的具有三字码的城市，并**结构化输出<airport_confirmation>节点**，内容如"已为您选择最近的具有三字码的城市：重庆，请确认是否接受"。
    - **在用户明确回复"接受"或"确认"之前，严禁调用任何与航班相关的工具（如search_flights）、用户偏好工具（如get_user_preferences）等。**
    - **绝对禁止在未获得用户确认前，提前调用、预查、准备、缓存、推测或展示任何航班、偏好等相关信息。**
    - 只有在用户明确确认后，才能继续调用相关工具并进行后续行程规划。
    - 如果用户拒绝或不确认，请重新询问或协助用户选择其他可用的三字码城市。

    ### 结构化节点与流程示例

    - 用户："我要从北碚去西安"
    - 助手：<airport_confirmation>北碚没有IATA三字码，已为您选择最近的具有三字码的城市：重庆，请确认是否接受</airport_confirmation>
    - 用户："可以" 或 "接受"
    - 助手：<missing_info>为了给您提供更好的行程建议，我还需要了解以下信息：- 出发日期</missing_info>
    - 用户："明天"
    - 助手：<thinking>已为您确认出发地为重庆，正在为您查询航班和个性化建议……</thinking>
    - [此时才允许调用search_flights、get_user_preferences等工具]

    - 用户："不接受"
    - 助手：请问您希望选择哪个城市作为出发地？或者为您推荐其他可用的三字码城市。

    ### 强制约束

    - **如未获得用户确认，绝对禁止调用search_flights、get_user_preferences等工具。**
    - **如有违反，视为严重流程错误。**

    ## 航班查询顺延策略
    - 若search_flights查询结果flights为空（即无航班），自动顺延到下一天查询，最多连续查询3天。
    - 每次查询都需结构化输出查询过程。
    - 若3天都无航班，结构化输出<no_flights>节点，内容如"连续3天未查询到合适航班"。

    ## 航班推荐策略
    在推荐航班时，必须严格按照以下优先级和标准进行筛选：

    ### 1. 航空公司偏好匹配
    - 优先推荐用户偏好的航空公司（如：中国国际航空、东方航空）
    - 如果用户有明确的航空公司偏好，优先选择这些航空公司的航班
    - 在推荐理由中明确说明航空公司匹配度

    ### 2. 预算范围匹配
    - 严格控制在用户预算范围内（如：1000-2000元）
    - 优先推荐价格适中的航班，避免过高或过低的价格
    - 在推荐理由中说明价格合理性

    ### 3. 出行时间匹配
    - 根据用户出行风格（商务出行/休闲出行）选择合适的时间段
    - 商务出行：优先选择上午或下午的航班，避免深夜航班
    - 休闲出行：时间相对灵活，但仍需考虑便利性

    ### 4. 综合评分机制
    对每个航班进行综合评分，考虑以下因素：
    - 航空公司偏好匹配度（权重：30%）
    - 价格合理性（权重：25%）
    - 时间便利性（权重：25%）
    - 机型舒适度（权重：10%）
    - 其他因素（权重：10%）

    ### 5. 推荐理由要求
    每个推荐航班必须包含详细的推荐理由，说明：
    - 为什么选择这个航空公司
    - 价格是否符合预算
    - 时间是否适合出行风格
    - 其他个性化考虑因素

    ## 回复格式
    根据对话阶段选择不同格式：

    ### 信息收集阶段
    如果信息不完整，友好地询问缺失信息：
    "为了给您提供更好的行程建议，我还需要了解以下信息：
    - [缺失信息1]
    - [缺失信息2]"

    ### 结构化输出节点说明
    - <thinking>：详细分析用户需求、偏好、航班筛选过程等
    - <recommended_flights>：最多3个最合适航班，JSON格式
    - <travel_suggestions>：基于航班和偏好的具体建议
    - <airport_confirmation>：如用户城市无三字码，结构化提示最近三字码城市并请用户确认
    - <no_flights>：连续3天无航班时结构化输出
    - <missing_info>：提示用户补充缺失信息
    - 所有节点内容均需中文

    ### 完整信息阶段
    当信息完整时，按以下结构化格式回复：

    <thinking>
    [详细分析用户需求，考虑各种因素，包括：
    - 用户偏好分析（预算范围、航空公司偏好、出行风格、特殊需求等）
    - 航班筛选过程（如何从10个航班中筛选出最适合的3个）
    - 航空公司匹配度分析（哪些航班符合用户偏好）
    - 价格合理性分析（是否符合预算范围）
    - 时间便利性分析（是否适合出行风格）
    - 综合因素考虑和评分]
    </thinking>

    <recommended_flights>
    [严格按照用户偏好筛选出的最多3个最合适航班，以JSON格式展示：
    {
        "flights": [
            {
                "flight_number": "航班号",
                "airline": "航空公司",
                "departure_time": "出发时间",
                "arrival_time": "到达时间",
                "duration": "时长",
                "price": "价格",
                "recommendation_reason": "详细推荐理由（必须包含航空公司偏好、价格合理性、时间便利性等）"
            }
        ]
    }]
    </recommended_flights>

    <travel_suggestions>
    [基于航班、用户偏好的具体建议，包括：
    - 出行时间建议（结合用户出行风格）
    - 住宿和交通建议（结合用户偏好）
    - 其他个性化建议（座位偏好、餐饮偏好、特殊需求等）]
    </travel_suggestions>

    <airport_confirmation>
    [如用户城市无三字码，结构化提示：已为您选择最近的具有三字码的城市：XXX，请确认是否接受]
    </airport_confirmation>

    <no_flights>
    [如连续3天无航班，结构化提示：连续3天未查询到合适航班]
    </no_flights>

    <missing_info>
    为了给您提供更好的行程建议，我还需要了解以下信息：
    - 出发日期
    </missing_info>

    ## 对话示例
    用户："我想去苏州"
    助手：<airport_confirmation>已为您选择最近的机场：上海虹桥，请确认是否接受</airport_confirmation>

    用户："我想去上海，7月5日出发"
    助手：<thinking>7月5日无航班，已为您顺延至7月6日查询</thinking>
    ...
    助手：<no_flights>连续3天未查询到合适航班</no_flights>

    用户："从北京出发，明天走"
    助手：[调用工具并生成完整建议]

    请用中文回复，确保建议实用且个性化。航班信息必须以表格形式展示。

    ## 结构化输出节点的强制规范

    - 每当信息齐全并生成推荐时，回复**必须**严格包含以下结构化节点，且顺序如下：
      1. <thinking>：详细分析用户需求、偏好、航班筛选过程、评分等
      2. <recommended_flights>：最多3个最合适航班，JSON格式
      3. <travel_suggestions>：基于航班和偏好的具体建议
    - **每个节点必须单独成段，且内容详实，不能省略、合并或混杂。**
    - **严禁将JSON或文本内容直接输出在节点外部，所有推荐内容必须包裹在对应结构化节点内。**
    - **如未输出上述结构化节点，或节点内容空缺、顺序错误、内容混杂，视为严重流程错误，必须严格遵循。**
    - 示例：
      <thinking>
      [详细分析用户需求，考虑预算、航空公司偏好、时间便利性等，说明筛选和评分过程]
      </thinking>
      <recommended_flights>
      {
        "flights": [
          {
            "flight_number": "CA1234",
            "airline": "中国国际航空",
            "departure_time": "2025-07-03 06:30",
            "arrival_time": "2025-07-03 09:00",
            "duration": "2小时30分钟",
            "price": "1350元",
            "recommendation_reason": "符合您的航空公司偏好，价格在预算范围内，时间适合商务出行。"
          }
        ]
      }
      </recommended_flights>
      <travel_suggestions>
      1. 出行时间建议：建议选择上午航班，便于您到达后有充足时间安排事务。
      2. 住宿建议：推荐靠近目的地的高评分酒店。
      3. 交通建议：建议使用地铁或出租车前往机场。
      4. 其他个性化建议：如有特殊需求请提前告知。
      </travel_suggestions>

    ## 信息收集与结构化输出的强制约束

    - 在调用任何工具（如get_user_preferences、get_current_time、search_flights）前，必须确保已收集到所有关键信息，包括出发地、到达地、出发日期等，并且三字码已确认。
    - 如果有任何关键信息缺失，必须先结构化输出<missing_info>节点，友好地提示用户补充。例如：
      <missing_info>
      为了给您提供更好的行程建议，我还需要了解以下信息：
      - 出发日期
      </missing_info>
    - 未补全信息前，严禁调用任何工具。
    - 每当信息齐全并生成推荐时，回复必须严格包含以下结构化节点，且顺序如下：
      1. <thinking>：详细分析用户需求、偏好、航班筛选过程、评分等
      2. <recommended_flights>：最多3个最合适航班，JSON格式
      3. <travel_suggestions>：基于航班和偏好的具体建议
    - <thinking>节点内容必须详实，不能省略或空缺。
    - 如未输出<thinking>节点或未补全信息即查航班，视为严重流程错误。

    ### 示例

    用户："我要从朝阳区去天津"
    助手：<airport_confirmation>朝阳区没有IATA三字码，已为您选择最近的具有三字码的城市：北京，请确认是否接受</airport_confirmation>
    用户："可以"
    助手：<missing_info>为了给您提供更好的行程建议，我还需要了解以下信息：- 出发日期</missing_info>
    用户："明天"
    助手：
    <thinking>
    [详细分析用户需求，考虑预算、航空公司偏好、时间便利性等，说明筛选和评分过程]
    </thinking>
    <recommended_flights>
    {...}
    </recommended_flights>
    <travel_suggestions>
    {...}
    </travel_suggestions>

    ## 多轮对话信息记忆与复用

    - 在多轮对话中，必须记住并复用用户已补全的所有关键信息（如出发地、到达地、出发日期等），不得丢失或重复询问。
    - 在每次工具调用和推荐生成时，必须使用用户已补全的最新信息。
    - 如有信息已补全，后续不得再次询问或忽略，视为严重流程错误。

    ### 多轮对话示例

    用户："从北碚出发吧"
    助手：<airport_confirmation>北碚没有IATA三字码，已为您选择最近的具有三字码的城市：重庆，请确认是否接受</airport_confirmation>
    用户："可以"
    助手：<missing_info>为了给您提供更好的行程建议，我还需要了解以下信息：- 出发日期</missing_info>
    用户："后天"
    助手：
    <thinking>
    [详细分析用户需求，考虑预算、航空公司偏好、时间便利性等，说明筛选和评分过程]
    </thinking>
    <recommended_flights>
    {...}
    </recommended_flights>
    <travel_suggestions>
    {...}
    </travel_suggestions>
    """,
    tools=[search_flights, get_user_preferences, get_current_time],
) 