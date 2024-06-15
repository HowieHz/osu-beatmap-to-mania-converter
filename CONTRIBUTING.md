# 贡献指南

## 软件发版前要做的事情

1. version.py 更新版本号

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
