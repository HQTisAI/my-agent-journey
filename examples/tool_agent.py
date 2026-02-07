"""
Tool Agent Example
带工具的 Agent 使用示例
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import AdvancedAgent
from tools import CalculatorTool, WebSearchTool


def main():
    """运行带工具的 Agent 示例"""

    print("=== AI Agent 工具使用示例 ===\n")

    # 创建 Agent 并添加工具
    agent = AdvancedAgent(
        model="gpt-4",
        personality="你是一个有帮助的助手，可以使用各种工具",
        tools=[CalculatorTool(), WebSearchTool()]
    )

    # 测试工具调用
    test_inputs = [
        "请帮我计算 15 + 27",
        "搜索一下 Python 教程",
        "计算 100 * 0.5",
        "帮我查询 AI 相关信息"
    ]

    print("测试工具调用:\n")

    for user_input in test_inputs:
        response = agent.chat(user_input)
        print(f"👤 你: {user_input}")
        print(f"🤖 Agent: {response}\n")

    # 导出对话和思维链
    print("=== 思维链 ===")
    for i, thought in enumerate(agent.get_thought_chain(), 1):
        print(f"{i}. {thought}")


if __name__ == "__main__":
    main()
