# LeetCode 练习

Python 刷题仓库，使用 `uv` 管理依赖，Ruff 统一代码风格。

## 项目结构

```
.
├── .github/                  # GitHub Actions 工作流与脚本
│   ├── workflows/            # CI 工作流（格式化检查、AI 代码审查）
│   └── scripts/              # 辅助脚本（AI 审查等）
├── .pre-commit-config.yaml   # Pre-commit 钩子配置
├── pyproject.toml            # 项目元数据与工具配置
├── uv.lock                   # 依赖锁文件
└── README.md
```

## 环境准备

本仓库使用 [uv](https://docs.astral.sh/uv/) 进行 Python 环境与依赖管理。

```bash
# 安装依赖
uv sync

# 激活虚拟环境
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS / Linux
```

## 代码规范

- 所有代码通过 [Ruff](https://docs.astral.sh/ruff/) 格式化与检查
- Pre-commit 钩子在提交前自动运行 Ruff

```bash
# 手动格式化
ruff format .

# 手动检查
ruff check .

# 自动修复
ruff check . --fix
```

## 安装 Pre-commit 钩子

```bash
pre-commit install
```

提交代码前会自动执行 Ruff 格式化与 lint 检查。

## 题目分类

> 待补充：按标签或难度整理已完成的题目。

## 许可证

MIT

