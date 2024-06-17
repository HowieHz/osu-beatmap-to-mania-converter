# 贡献指南

## 软件发版前要做的事情

1. version.py 更新版本号

## 部署开发环境

1. 在本地部署 Python3.12 环境后
2. 下载项目源码，然后进入到项目根目录
3. 创建虚拟环境后
4. 运行以下指令

```bash
pip install -r requirements.txt
```

创建 pre-commit 钩子，以便在每次提交前自动格式化代码

```bash
pre-commit install
```

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
