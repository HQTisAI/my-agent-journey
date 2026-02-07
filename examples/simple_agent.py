"""
Simple Agent Example
简单的 Agent 使用示例
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import BaseAgent


def main():
    """运行简单 Agent 示例"""

    print("=== AI Agent 简单示例 ===\n")

    # 创建 Agent
    agent = BaseAgent(
        model="gpt-3.5-turbo",
        personality="你是一个友好的AI助手，喜欢帮助他人"
    )

    # 对话循环
    print("开始对话（输入 'quit' 退出）\n")

    while True:
        user_input = input("👤 你: ")

        if user_input.lower() in ['quit', 'exit', '退出']:
            print("👋 再见！")
            break

        # 获取回复
        response = agent.chat(user_input)
        print(f"🤖 Agent: {response}\n")

    # 导出对话
    print("\n=== 对话历史 ===")
    for msg in agent.get_conversation_history():
        role = "👤 你" if msg["role"] == "user" else "🤖 Agent"
        print(f"{role}: {msg['content']}")


if __name__ == "__main__":
    main()
