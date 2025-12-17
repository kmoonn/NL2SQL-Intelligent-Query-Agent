# NL2SQL-Intelligent-Query-Agent

基于 LLMs 和 RAG 的 NL2SQL 智能问数 Agent

- 配置大模型和数据源，通过大模型和 RAG 结合实现高质量的 text2sql；
- 支持 Docker 部署，快速嵌入业务系统，用户通过聊天框对话进行数据分析。

### 技术栈

- 后端：Python
  - 框架：FastAPI
  - 环境管理：uv
- 前端
  - 框架：Vue.js
  - 组件库：Element
  - 依赖管理：npm
- 中间件：
  - 向量扩展：PostgreSQL
  - 部署：Docker
- 支持数据库
  - MySQL

## 工作原理

### 整体架构

三个参与方：
- 用户（**User**）
- 数据源（**DB**）
- 大模型（**LLM**）

## 前置知识

### [LLM](docs/LLM.md)

### [Prompt](docs/Prompt.md)

### [RAG](docs/RAG.md)