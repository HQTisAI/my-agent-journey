"""
Advanced Agent Implementation
高级 Agent 实现 - 支持工具调用和记忆
"""

from typing import Optional, List, Dict, Any
from .base import BaseAgent, AgentConfig


class AdvancedAgent(BaseAgent):
    """高级 Agent 类 - 支持工具调用和记忆"""

    def __init__(
        self,
        model: str = "gpt-4",
        personality: str = "你是一个专业的AI助手",
        tools: Optional[List] = None,
        memory: Optional[Any] = None,
        enable_thought_chain: bool = True
    ):
        """
        初始化高级 Agent

        Args:
            model: 模型名称
            personality: 人设
            tools: 工具列表
            memory: 记忆系统
            enable_thought_chain: 是否启用思维链
        """
        super().__init__(model, personality, tools, memory)
        self.enable_thought_chain = enable_thought_chain
        self.thought_chain = []

    def chat(self, message: str) -> str:
        """
        对话（带工具调用和记忆）

        Args:
            message: 用户消息

        Returns:
            回复
        """
        # 如果有记忆系统，先查询相关记忆
        if self.config.memory:
            relevant_memories = self.config.memory.search(message)
            if relevant_memories:
                message = f"相关记忆: {relevant_memories}\n\n用户: {message}"

        # 检查是否需要调用工具
        if self.config.tools:
            tool_response = self._check_and_call_tool(message)
            if tool_response:
                return tool_response

        # 生成回复
        response = super().chat(message)

        # 如果有记忆系统，保存对话
        if self.config.memory:
            self.config.memory.add(message, response)

        return response

    def _check_and_call_tool(self, message: str) -> Optional[str]:
        """
        检查并调用工具

        Args:
            message: 用户消息

        Returns:
            工具调用结果，如果不需要调用则返回 None
        """
        # 简化实现：检查关键词
        for tool in self.config.tools:
            if tool.name.lower() in message.lower():
                try:
                    result = tool.execute(message)
                    return f"🔧 使用工具 '{tool.name}':\n{result}"
                except Exception as e:
                    return f"工具调用失败: {str(e)}"

        return None

    def think(self, thought: str):
        """
        记录思考过程

        Args:
            thought: 思考内容
        """
        self.thought_chain.append(thought)

    def get_thought_chain(self) -> List[str]:
        """获取思维链"""
        return self.thought_chain

    def export_dialog(self) -> str:
        """
        导出对话历史

        Returns:
            格式化的对话文本
        """
        output = ["=== 对话历史 ===\n"]
        for msg in self.conversation_history:
            role = "👤 用户" if msg["role"] == "user" else "🤖 Agent"
            output.append(f"{role}: {msg['content']}\n")

        if self.thought_chain:
            output.append("\n=== 思维链 ===\n")
            for i, thought in enumerate(self.thought_chain, 1):
                output.append(f"{i}. {thought}\n")

        return "".join(output)


if __name__ == "__main__":
    # 测试代码
    from tools import SimpleTool

    # 创建一个简单的测试工具
    class TestTool(SimpleTool):
        name = "计算器"
        description = "执行简单的数学计算"

        def execute(self, input_text: str) -> str:
            try:
                # 提取数字并计算
                import re
                numbers = re.findall(r'\d+', input_text)
                if len(numbers) >= 2:
                    result = int(numbers[0]) + int(numbers[1])
                    return f"计算结果: {result}"
                return "需要至少两个数字"
            except Exception as e:
                return f"计算错误: {e}"

    # 创建高级 Agent
    agent = AdvancedAgent(
        model="gpt-4",
        tools=[TestTool()]
    )

    # 测试对话
    response = agent.chat("请使用计算器帮我算 5 + 3")
    print(response)
