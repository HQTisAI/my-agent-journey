# 📝 我的 AI Agent 学习之旅

> 从零开始学习 AI Agent 的过程记录 - 不是框架，是学习笔记

**注意：这不是一个开箱即用的框架，而是我学习过程中的代码积累和笔记。**

---

## 🔍 起因

2025 年底，我开始接触 AI Agent 这个概念。起初只是跟着教程跑一些 demo，但很快就发现很多问题：

1. **教程太简化** - 只展示成功的代码，不展示踩坑的过程
2. **缺少细节** - 比如说"调用 OpenAI API"，但实际调用的参数是什么、遇到什么错误，都不说
3. **没有真实场景** - 都是用"你好"测试，没有实际用途

所以我决定自己走一遍完整的流程，把遇到的问题都记录下来。

---

## 📅 时间线

### 2025.12 - 第一次接触

**尝试：** 调用 OpenAI API 做一个简单的对话机器人

**遇到的问题：**
1. API Key 怎么保存？硬编码不安全，但 `.env` 又不知道怎么读
2. 超时怎么处理？网络波动时候一直等
3. Token 怎么计数？OpenAI 的 token 计算很麻烦

**解决：**
- 学了 `python-dotenv` 库
- 加了 `timeout` 和重试逻辑
- 用 `tiktoken` 估算 token（虽然不准，但够用）

**代码：** 见 `v1/` 目录

---

### 2026.01 - 尝试工具调用

**动机：** 发现 Agent 不只是对话，需要能调用外部工具

**尝试 1：** 手动 if-else 判断

```python
if "计算" in message:
    return calculator()
```

**问题：** 太笨了，无法处理"用算术帮我算 5+3"这样的表达

**尝试 2：** 看 LangChain 的工具调用

**问题：** 文档太多，概念复杂，没看懂就放弃了

**尝试 3：** 自己实现一个简单版

- 定义工具接口
- 让 LLM 输出 JSON 格式的工具调用
- 手动解析 JSON 执行工具

**结果：** 可以用了，虽然很简陋

**代码：** 见 `v2/tool_calling.py`

---

### 2026.02 - 记忆系统

**问题发现：** 对话一多，Agent 就忘了之前说过什么

**尝试：** 简单的对话历史列表

```python
history = []
history.append(user_msg)
history.append(ai_msg)
```

**问题：** 历史一长，token 就爆了，而且无关的对话也在里面

**尝试 2：** 只保留最近的 10 条

**问题：** 还是会忘记重要的信息（比如用户名字）

**尝试 3：** 学习 RAG（检索增强生成）

- 用向量数据库存之前的对话
- 根据当前问题检索相关历史
- 只把相关的作为上下文

**当前状态：** 正在学习中，代码在 `v3/memory/`

---

## 📂 目录结构

```
my-agent-journey/
├── v1/              # 第一个版本 - 简单的对话机器人
│   ├── simple_bot.py
│   ├── api_call.py
│   └── README.md     # 当时的笔记
├── v2/              # 工具调用尝试
│   ├── tool_calling.py
│   ├── tools.py
│   └── README.md     # 踩坑记录
├── v3/              # 记忆系统（进行中）
│   ├── memory.py
│   ├── vector_db.py
│   └── README.md
└── journal/           # 学习日记
    ├── 2025-12.md
    ├── 2026-01.md
    └── 2026-02.md
```

## 🤔 目前卡住的问题

1. **Token 计算** - OpenAI 的计费按 token，但 tiktoken 算出来的和实际消耗有差异，不知道为什么
2. **并发限制** - 同时处理多个用户时候，怎么共享上下文？
3. **工具链** - 如果一个任务需要调用多个工具（查资料 -> 计算 -> 生成结果），怎么做？

## 📚 学习资源（对我有用的）

- **[LangChain 文档](https://python.langchain.com/)** - 概念清晰，但上手难
- **[OpenAI Cookbook](https://github.com/openai/openai-cookbook)** - 实用例子多
- **[AutoGPT 论文](https://arxiv.org/abs/2304.03442)** - 理论看不完，但了解一下思路

## 📝 下一步计划

- [ ] 理解 Vector Database 的原理和选择
- [ ] 尝试多 Agent 协作（比如一个查资料，一个写内容）
- [ ] 评估不同的 LLM 在 Agent 任务上的表现

## ⚠️ 重要说明

**这个仓库不是给别人用的**：

1. 代码可能很乱，因为还在学习中
2. 有些方案可能是错的，只是我当时的尝试
3. 不会有版本号的稳定发布，都是实验性的

如果你也在学 Agent，希望我的踩坑记录对你有帮助。如果有更好的做法，欢迎告诉我！

---

## 📧 本地运行

```bash
# 克隆
git clone https://github.com/HQTisAI/my-agent-journey.git
cd my-agent-journey

# 安装依赖
pip install -r requirements.txt

# 配置
cp .env.example .env
# 填入你的 API key

# 运行不同版本
cd v1
python simple_bot.py
```

---

*更新时间：2026-02-07*

**如果你也在学 AI Agent，或者有类似的学习笔记，欢迎交流！**
