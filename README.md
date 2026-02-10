# AI Agent 学习笔记

从零开始学 AI Agent，记录过程。

不是框架，就是笔记，代码质量别细看。

## 为什么写这个

网上教程要么太简单（hello world 级别），要么太复杂（上来就 LangChain 全家桶）。
我想找个中间地带，从最基础的 API 调用开始，一步步搞明白 Agent 到底是怎么回事。

## 目录

- `journal/` - 学习日志，按日期记
- `agent/` - 自己写的简单 agent，能跑但很粗糙
- `tools/` - 给 agent 用的工具函数
- `examples/` - 跟着教程敲的代码

## 目前进度

刚搞明白 function calling 是怎么回事，在试着让 agent 自己决定调用什么工具。
ReAct 模式看了论文但还没完全理解，先照着别人的代码抄了一版。

## 用到的

- OpenAI API（主要）
- 一些开源模型（通过 API 中转）
- Python，没用框架

---

*随缘更新*
