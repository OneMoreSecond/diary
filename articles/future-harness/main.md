# Harness 走向何方？

## Harness 的长期使命

- 从后训练侧看：从用户场景中收集反馈信号，长期共生演进
- 从用户侧看：帮助模型拓展能力，改善任务表现

## 后训练侧

AI系统要长期发展，必须有长期反馈信号增长机制，要么厂商内部制作数据集，要么从外部场景中收集人类与环境反馈信号。

从外部场景收集反馈信号时，Harness 能决定数据和反馈的形态。
怎样让Agent轨迹的反馈信号更强？需要把弱反馈、低频反馈、隐性反馈，转化成强反馈、高频反馈、显性反馈。

### 人类反馈

现在 Harness 与人交互时，更多还是被动等待输入。是否可以引导用户更明确的展现意图与反馈？

现有功能例如：

- Copilot ask question tool 允许模型以 tool use 形式频繁向用户提问
- ChatGPT 回答问题后会提出几个下一步选择
- Claude Code 允许多个 tool use 异步进行

功能设想：

- Agent 工作时可以高频异步调用 ask question tool，将 side question 体验从现有的“人问Agent”扩展到“Agent问人”。

## 用户侧

人会写代码封装功能，将软性组合升级为硬性抽象，从更高层级表达需求，也避免犯错。

Agent也一样。
提示词灵活但无法完全保证模型行为，程序死板但提供确定性。
Agent 良好工作需要提示词、程序与 Harness（软硬中介）的协作。

### 从确定性建立信任

不仅是拦截模型一次错误，更是在对齐用户心智中 Agent 行为的边界

- bash 命令 approve
- sandbox 限制文件读写
- 虚拟机限制 Agent 行为影响机器上其他用户
- Hook 在特定时机触发固定行为

### 扩展机制

扩展模型自身结构上不足的能力

- Tool：tool description 直接注入，tool use 由模型决定
- Skill：skill description 直接注入，read skill 由模型决定
- Memory：memory index 直接注入，read memory 由模型决定

Tool 是最基础的机制。
Skill 为用户提供简单好上手的知识索引。
Memory 则主要处理跨 session 信息流通。

问题：足够了吗？还有什么扩展？

#### 读与写

能读的地方尽量能 **主动** 修改：

- 改 AGENTS.md
- 改 SKILL.md 提示词与 script/ 程序
- 记录新的 memory 与整理旧的 memory
- few shot 固化 bash approve pattern（这个似乎暂时不会被记入 memory）

### 消除摩擦

如何连接 Agent 与外部的软件世界？
冷启动的几个层次：

- Agent session 冷启动：为模型提供合适的文本前缀
- 用户帮 Agent 在项目上冷启动：为新近使用 Agent 的项目建立合适的配置
- Agent 产业早期阶段：将外部世界非 Agent-native 的信息接入 LLM

针对现有非 Agent-native 的环境：

- MCP：针对特定接口开发，比较繁重，更适合用于整合一套解决方案的内部组件
- CLI shell：通用但要求用户专业背景
- GUI computer use：通用但要求模型适配

畅想：会有 Agent-native 的软件与信息生态吗？能是什么样？

### 预设与自定义

两个方向：

- Claude code：Harness 包含丰富功能，开箱即用。更适合：模型厂商 + 同质场景
- Pi：专注于核心框架，但保留丰富的扩展空间。更适合：社区开发 + 异质场景

“丰富功能” 的边界在哪里？
Harness 可不可以自己造一套 Excel？
思考：Harness 自身面向比较同质的人，扩展功能面向比较异质的事。

## 尚无答案的思考

1. 弯道超车：怎样超越 Claude Code 与 Codex？
2. 如何收集与学习更长程反馈？尝试定义“判断力”“审美”：将 life-long reward 投射到即时 reward 的能力
