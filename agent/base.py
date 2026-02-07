"""
Base Agent Implementation
基础 Agent 实现
"""

import os
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class AgentConfig:
    """Agent 配置类"""
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 1000
    personality: str = "你是一个有帮助的AI助手"
    tools: Optional[List] = None
    memory: Optional[Any] = None


class BaseAgent:
    """基础 Agent 类"""

    def __init__(
        self,
        model: str = "gpt-3.5-turbo",
        personality: str = "你是一个有帮助的AI助手",
        tools: Optional[List] = None,
        memory: Optional[Any] = None
    ):
        """
        初始化 Agent

        Args:
            model: 使用的模型名称
            personality: Agent 的人设/性格
            tools: 可用的工具列表
            memory: 记忆系统
        """
        self.config = AgentConfig(
            model=model,
            personality=personality,
            tools=tools or [],
            memory=memory
        )
        self.conversation_history = []

    def chat(self, message: str) -> str:
        """
        与 Agent 对话

        Args:
            message: 用户消息

        Returns:
            Agent 的回复
        """
        # 添加用户消息到历史
        self.conversation_history.append({
            "role": "user",
            "content": message
        })

        # 生成回复
        response = self._generate_response()

        # 添加 Assistant 回复到历史
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })

        return response

    def _generate_response(self) -> str:
        """
        生成回复（实际实现）

        Returns:
            生成的回复
        """
        # 这里简化实现，实际会调用 LLM API
        import random

        responses = [
            "这是一个很好的问题！",
            "我理解你的意思。",
            "让我来帮你解答。",
            "这是一个有趣的话题。",
        ]

        return random.choice(responses)

    def reset(self):
        """重置对话历史"""
        self.conversation_history = []

    def add_tool(self, tool: Any):
        """添加工具"""
        self.config.tools.append(tool)

    def set_personality(self, personality: str):
        """设置人设"""
        self.config.personality = personality

    def get_conversation_history(self) -> List[Dict]:
        """获取对话历史"""
        return self.conversation_history


if __name__ == "__main__":
    # 测试代码
    agent = BaseAgent(
        model="gpt-4",
        personality="你是一个友好的AI助手"
    )

    response = agent.chat("你好！")
    print(f"用户: 你好！")
    print(f"Agent: {response}")
