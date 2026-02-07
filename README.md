# 🤖 AI Agent Starter

> 一个开箱即用的 AI Agent 开发框架，让构建智能体变得简单快速

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## ✨ 特性

- 🚀 **快速开始** - 5 分钟内创建你的第一个 AI Agent
- 🧩 **模块化设计** - 灵活组合不同组件
- 🔌 **多模型支持** - OpenAI、Anthropic、本地模型
- 📝 **自动记忆** - 内置短期和长期记忆系统
- 🎯 **工具调用** - 轻松集成外部工具和 API
- 🌐 **Web 界面** - 可选的交互式 UI

## 📦 快速安装

```bash
# 克隆仓库
git clone https://github.com/HQTisAI/ai-agent-starter.git
cd ai-agent-starter

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入你的 API keys
```

## 🚀 使用示例

### 创建简单 Agent

```python
from agent import Agent

# 初始化 agent
agent = Agent(
    model="gpt-4",
    name="智能助手",
    personality="你是一个友好、专业的AI助手"
)

# 对话
response = agent.chat("你好！")
print(response)
```

### 工具调用 Agent

```python
from agent import Agent
from tools import web_search, calculator

agent = Agent(
    model="gpt-4",
    tools=[web_search, calculator]
)

# agent 会自动调用工具
response = agent.chat("搜索一下今天北京的天气")
print(response)
```

### 记忆增强 Agent

```python
from agent import Agent
from memory import LongTermMemory

# 配置长期记忆
memory = LongTermMemory(storage="sqlite")

agent = Agent(
    model="gpt-4",
    memory=memory
)

# agent 会记住之前的对话
agent.chat("我叫小王")
response = agent.chat("我叫什么名字？")
# 输出：你叫小王
```

## 📁 项目结构

```
ai-agent-starter/
├── agent/              # Agent 核心实现
│   ├── __init__.py
│   ├── base.py         # 基础 Agent 类
│   └── advanced.py     # 高级 Agent 类
├── tools/              # 内置工具
│   ├── __init__.py
│   ├── web_search.py
│   ├── calculator.py
│   └── code_executor.py
├── memory/             # 记忆系统
│   ├── __init__.py
│   ├── short_term.py
│   └── long_term.py
├── examples/           # 使用示例
│   ├── simple_agent.py
│   ├── tool_agent.py
│   └── multi_agent.py
├── tests/              # 测试
├── docs/               # 文档
└── web/                # Web 界面（可选）
```

## 🎯 支持的模型

- ✅ OpenAI GPT-4 / GPT-3.5
- ✅ Anthropic Claude
- ✅ Google Gemini
- ✅ 本地模型 (Ollama, LocalAI)
- ✅ 自定义 API

## 🔧 配置

创建 `.env` 文件：

```env
# OpenAI
OPENAI_API_KEY=sk-xxx

# Anthropic
ANTHROPIC_API_KEY=sk-ant-xxx

# 其他配置
LOG_LEVEL=info
MEMORY_TYPE=sqlite
```

## 📚 进阶用法

### 多 Agent 协作

```python
from agent import Agent

# 创建多个 agent
researcher = Agent(name="研究员", role="搜集信息")
writer = Agent(name="作家", role="撰写文章")

# 协作完成任务
result = collaborate(researcher, writer, task="写一篇关于AI的文章")
```

### 自定义工具

```python
from agent import Tool

@tool
def weather_api(location: str):
    """查询天气"""
    # 你的天气 API 逻辑
    return f"{location} 今天晴天，25°C"

agent = Agent(tools=[weather_api])
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🌟 Star History

如果这个项目对你有帮助，请给它一个 Star ⭐

## 📞 联系方式

- 作者：HQTisAI
- 邮箱：jinhanwangwang@gmail.com
- GitHub：[@HQTisAI](https://github.com/HQTisAI)
