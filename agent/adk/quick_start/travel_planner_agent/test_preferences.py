#!/usr/bin/env python3
"""
测试航班推荐是否能够正确结合用户偏好
"""

import asyncio
import json
from agent import root_agent


async def test_preference_based_recommendation():
    """测试基于用户偏好的航班推荐"""
    
    print("=== 测试航班推荐结合用户偏好 ===\n")
    
    # 测试用例：用户偏好中国国际航空和东方航空，预算1000-2000元，商务出行
    test_query = "我想从北京去上海，明天出发"
    
    print(f"用户查询: {test_query}")
    print("预期行为:")
    print("- 优先推荐中国国际航空和东方航空的航班")
    print("- 价格控制在1000-2000元范围内")
    print("- 选择适合商务出行的时间段（上午或下午）")
    print("- 推荐理由中明确说明用户偏好匹配度")
    print("\n" + "="*50 + "\n")
    
    try:
        response = await root_agent.run(test_query)
        print("Agent回复:")
        print(response)
        
        # 分析回复中是否包含用户偏好信息
        print("\n" + "="*50)
        print("偏好匹配分析:")
        
        if "中国国际航空" in response or "东方航空" in response:
            print("✓ 包含用户偏好的航空公司")
        else:
            print("✗ 未包含用户偏好的航空公司")
            
        if "1000-2000元" in response or "预算" in response:
            print("✓ 考虑了预算范围")
        else:
            print("✗ 未考虑预算范围")
            
        if "商务出行" in response or "商务" in response:
            print("✓ 考虑了出行风格")
        else:
            print("✗ 未考虑出行风格")
            
        if "推荐理由" in response or "recommendation_reason" in response:
            print("✓ 包含推荐理由")
        else:
            print("✗ 未包含推荐理由")
            
    except Exception as e:
        print(f"测试过程中出现错误: {e}")


async def test_user_preferences_tool():
    """测试用户偏好工具"""
    
    print("\n=== 测试用户偏好工具 ===\n")
    
    from agent import get_user_preferences
    
    try:
        preferences = get_user_preferences()
        print("用户偏好信息:")
        print(json.dumps(preferences, ensure_ascii=False, indent=2))
        
        # 验证关键偏好信息
        prefs = preferences.get('preferences', {})
        
        print("\n关键偏好验证:")
        print(f"预算范围: {prefs.get('budget_range', '未设置')}")
        print(f"航空公司偏好: {prefs.get('preferred_airlines', '未设置')}")
        print(f"出行风格: {prefs.get('travel_style', '未设置')}")
        print(f"座位偏好: {prefs.get('seat_preference', '未设置')}")
        print(f"餐饮偏好: {prefs.get('meal_preference', '未设置')}")
        
    except Exception as e:
        print(f"获取用户偏好时出现错误: {e}")


async def test_flight_search_tool():
    """测试航班搜索工具"""
    
    print("\n=== 测试航班搜索工具 ===\n")
    
    from agent import search_flights
    
    try:
        # 测试航班搜索
        flight_data = search_flights("PEK", "SHA", "2024-12-20")
        
        print("航班搜索结果:")
        print(f"出发城市: {flight_data['departure_city']}")
        print(f"到达城市: {flight_data['arrival_city']}")
        print(f"出发日期: {flight_data['departure_date']}")
        print(f"航班数量: {len(flight_data['flights'])}")
        
        print("\n前3个航班信息:")
        for i, flight in enumerate(flight_data['flights'][:3], 1):
            print(f"{i}. {flight['airline']} {flight['flight_number']}")
            print(f"   时间: {flight['departure_time']} - {flight['arrival_time']}")
            print(f"   价格: {flight['price']}")
            print()
            
        # 分析是否有用户偏好的航空公司
        preferred_airlines = ["中国国际航空", "东方航空"]
        available_airlines = [flight['airline'] for flight in flight_data['flights']]
        
        print("航空公司匹配分析:")
        for airline in preferred_airlines:
            if airline in available_airlines:
                print(f"✓ {airline} - 有可用航班")
            else:
                print(f"✗ {airline} - 无可用航班")
                
    except Exception as e:
        print(f"航班搜索时出现错误: {e}")


async def main():
    """主测试函数"""
    
    print("智能行程规划Agent - 用户偏好测试")
    print("="*50)
    
    # 测试用户偏好工具
    await test_user_preferences_tool()
    
    # 测试航班搜索工具
    await test_flight_search_tool()
    
    # 测试完整的偏好推荐
    await test_preference_based_recommendation()
    
    print("\n" + "="*50)
    print("测试完成！")


if __name__ == "__main__":
    asyncio.run(main()) 