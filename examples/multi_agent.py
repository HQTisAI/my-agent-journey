"""
Multi-Agent Collaboration Example
多 Agent 协作示例
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import AdvancedAgent


class AgentCollaborator:
    """Agent 协作器"""

    def __init__(self):
        self.agents = {}

    def add_agent(self, name: str, agent: AdvancedAgent):
        """添加 Agent"""
        self.agents[name] = agent
        agent.set_personality(f"你是{name}，负责相应任务")

    def collaborate(self, task: str, sequence: list) -> str:
        """
        让 Agent 协作完成任务

        Args:
            task: 任务描述
            sequence: Agent 执行顺序

        Returns:
            最终结果
        """
        current_input = f"任务: {task}\n\n"
        results = []

        for agent_name in sequence:
            if agent_name not in self.agents:
                continue

            agent = self.agents[agent_name]
            response = agent.chat(current_input)

            results.append(f"=== {agent_name} ===\n{response}")
            current_input = f"前面的工作:\n{response}\n\n需要继续:\n"

        return "\n\n".join(results)


def main():
    """运行多 Agent 协作示例"""

    print("=== 多 Agent 协作示例 ===\n")

    # 创建协作器
    collaborator = AgentCollaborator()

    # 创建不同角色的 Agent
    researcher = AdvancedAgent(
        model="gpt-4",
        personality="你是一个研究员，擅长搜集和分析信息"
    )

    writer = AdvancedAgent(
        model="gpt-4",
        personality="你是一个作家，擅长撰写文章"
    )

    reviewer = AdvancedAgent(
        model="gpt-4",
        personality="你是一个编辑，擅长审阅和修改内容"
    )

    # 添加 Agent
    collaborator.add_agent("研究员", researcher)
    collaborator.add_agent("作家", writer)
    collaborator.add_agent("编辑", reviewer)

    # 执行协作任务
    task = "写一篇关于人工智能发展历史的短文"
    sequence = ["研究员", "作家", "编辑"]

    print(f"任务: {task}\n")
    print(f"协作顺序: {' → '.join(sequence)}\n")

    result = collaborator.collaborate(task, sequence)
    print(result)

    print("\n=== 协作完成 ===")


if __name__ == "__main__":
    main()
