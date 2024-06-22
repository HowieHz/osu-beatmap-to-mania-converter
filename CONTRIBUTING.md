# 贡献指南

## 软件发版前要做的事情

1. version.py 更新版本号

## 部署开发环境

### 在本地部署 Python3.12 环境

[Download Python](https://www.python.org/downloads/)

### 下载项目源码，并进入到项目根目录

```bash
git clone https://github.com/HowieHz/osu-beatmap-to-mania-converter && cd osu-beatmap-to-mania-converter/
```

### 创建虚拟环境

```bash
python -m venv .venv
```

### 进入虚拟环境

在 Windows 环境下

```powershell
./.venv/Scripts/activate
```

在 Bash

```bash
source ./.venv/bin/activate
```

附：退出虚拟环境的指令

```bash
deactivate
```

### 安装项目所需库

```bash
pip install -r requirements.txt
```

创建 pre-commit 钩子，以便在每次提交前自动格式化代码

```bash
pre-commit install
```

<!-- 附：导出当前虚拟环境中的库

```bash
pip freeze > requirements.txt
``` -->

## 怎么打开 DEBUG 模式

对于交互式程序 `interactive_interface.py`
根据你的环境，用对应的方法设置环境变量，使得 `DEBUG_FLAG=True`

在 Bash

```bash
export DEBUG_FLAG=True
```

在 PowerShell

```powershell
$env:DEBUG_FLAG="True"
```

<!-- 查看此变量
```powershell
$env:DEBUG_FLAG
``` -->

在 CMD

```cmd
set DEBUG_FLAG=True
```

<!-- 查看此变量
```cmd
echo %DEBUG_FLAG%
``` -->

## 构建二进制文件

> 使用 nuitka 库

安装 nuitka 库

```shell
pip install nuitka
```

生成二进制文件

```shell
nuitka .\src\main.py --standalone --onefile
```
