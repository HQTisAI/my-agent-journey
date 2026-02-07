"""
Tool Base Classes
工具基类
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import json


class Tool(ABC):
    """工具基类"""

    name: str = "BaseTool"
    description: str = "基础工具"

    @abstractmethod
    def execute(self, input_text: str) -> str:
        """
        执行工具

        Args:
            input_text: 输入文本

        Returns:
            执行结果
        """
        pass

    def get_schema(self) -> Dict[str, Any]:
        """获取工具的 JSON Schema"""
        return {
            "name": self.name,
            "description": self.description,
            "type": "function"
        }


class SimpleTool(Tool):
    """简单工具 - 适合快速创建工具"""

    name: str = "SimpleTool"
    description: str = "简单工具"

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None):
        if name:
            self.name = name
        if description:
            self.description = description

    def execute(self, input_text: str) -> str:
        """执行（子类覆盖）"""
        raise NotImplementedError("Subclass must implement execute()")


# 内置工具示例
class CalculatorTool(SimpleTool):
    """计算器工具"""

    name = "计算器"
    description = "执行基本数学计算 (+, -, *, /)"

    def execute(self, input_text: str) -> str:
        try:
            # 安全的数学表达式求值
            import re
            # 只允许数字和基本运算符
            expr = re.sub(r'[^\d\+\-\*\/\(\)\.\s]', '', input_text)
            if not expr:
                return "没有找到有效的数学表达式"

            result = eval(expr)  # 注意：实际生产环境应该用更安全的方法
            return f"计算结果: {expr} = {result}"
        except Exception as e:
            return f"计算错误: {str(e)}"


class WebSearchTool(SimpleTool):
    """网页搜索工具"""

    name = "网页搜索"
    description = "搜索网络信息"

    def execute(self, input_text: str) -> str:
        try:
            # 这里应该调用实际的搜索 API
            # 简化实现：返回模拟结果
            return f"🔍 搜索 '{input_text}' 的结果:\n\n1. 示例搜索结果 1\n2. 示例搜索结果 2\n3. 示例搜索结果 3"
        except Exception as e:
            return f"搜索失败: {str(e)}"


if __name__ == "__main__":
    # 测试工具
    calc = CalculatorTool()
    print(calc.execute("5 + 3"))
    print(calc.execute("10 * 2"))

    search = WebSearchTool()
    print(search.execute("AI Agent"))
