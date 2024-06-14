# osu-beatmap-to-mania-converter

> Convert osu!standard(osu!std) to osu!mania

## 主要功能

将 osu!std 铺面转换为 osu!mania 铺面。

如果想支持本项目就点个 star 吧，你的支持将指引我砥砺前行。

如遇到 Bug，想提出新功能，对现有功能不满，想提出建议，想问问题，单纯想进行讨论，欢迎前来[提出新的 Issue](https://github.com/HowieHz/osu-beatmap-to-mania-converter/issues/new/choose)。

---

- [osu-beatmap-to-mania-converter](#osu-beatmap-to-mania-converter)
  - [主要功能](#主要功能)
    - [输出铺面类型](#输出铺面类型)
    - [输出规则](#输出规则)
    - [Mania 2k 铺面输出可配置项](#mania-2k-铺面输出可配置项)
  - [如何下载使用](#如何下载使用)
    - [通过二进制文件运行](#通过二进制文件运行)
    - [Windows](#windows)
    - [MacOS \& Linux](#macos--linux)
    - [通过源码运行](#通过源码运行)
  - [程序结构](#程序结构)
    - [当目标产物为 osu!mania 1k](#当目标产物为-osumania-1k)
    - [当目标产物为 osu!mania 2k](#当目标产物为-osumania-2k)
  - [为何创建此项目](#为何创建此项目)
  - [TODO](#todo)
  - [更新日志](#更新日志)

---

### 输出铺面类型

osu!mania 1k, osu!mania 2k

### 输出规则

1. 主模式音符 -> mania 音符
2. 主模式长条 -> mania 长条
3. 主模式转盘 -> mania 长条

### Mania 2k 铺面输出可配置项

> 需重写此段描述

标记 TODO 的表示还是未完成的功能

1. 长纵转交互：生成成 1k 的时候会出现大量的纵连，此时根据这个规则开始转换
   - （TODO）两音符击打时间间距小于一个值（Anti long jack）
     - mode1: 不管这个间隔时间是否恒定（variable time interval）
     - mode2: 要求这个间隔时间必须恒定（constant time interval）
   - （TODO）从哪个开始转换为交互（Conversion starts position）
     - mode1: 满足要求便从计算的第一个开始转换（Conversion starts with the first）
     - mode2: 满足要求从满足要求的那个开始转换（比如是大于 3 个连续音符开始转换，那就把第四个音符放在另一个轨道，前三个音符保持为一个三连段纵）（Conversion starts from a position of attainment）
   - （TODO）转换模式（trill or jack）
     - mode1: 满足要求便全部转换成交互（All to trill）
     - mode2: 满足要求便全部转换为短纵（All to jack）
     - mode3: 多少连续音符转换为分组短纵，超过多少音符转换为交互（Long jack converted to trill, keep short jack）
2. （TODO）防止交互头尾连起来短纵选项：前一个交互的最后一个音符和下一个交互开头的音符要是间隔小于一个值，下一个交互就从另一个轨道开始（Anti minijack between trill）
3. 检测 ln 尾部和下一个 note 的间距，小于一个值就把这个 note 放到另一列上

设置选项

1. 设置惯用单戳指所在轨道：物件会优先生成在这个轨道上（main key）
2. 设置铺面从哪一轨开始生成（start key）
3. 交互起手设置：最开始的交互哪个轨道起手（Trill start key）
4. 纵连两键间距小于多少毫秒开始转交互（Minimum Jack Time Interval）
5. 几个纵开始转交互（Maximum number of jack notes）

## 如何下载使用

### 通过二进制文件运行

### Windows

从 [Releases](https://github.com/HowieHz/osu-beatmap-to-mania-converter/releases) 下载最新版本二进制文件。
解压后，运行 `main.exe` 即可开始运行程序，随后根据程序引导完成操作即可。

### MacOS & Linux

请看[通过源码运行](#通过源码运行)

### 通过源码运行

下载项目源码，然后进入到项目根目录。  
在本地部署 Python 环境后，运行以下指令。
即可从源码运行此项目。

```bash
pip install -r requirements.txt
```

```bash
python ./src/main.py
```

## 程序结构

### 当目标产物为 osu!mania 1k

[读取器（包括预处理）](./src/lib/reader/) -> [处理器（数据转换）](./src/lib/processor/) -> [生成器](./src/lib/exporter/)

### 当目标产物为 osu!mania 2k

[读取器（包括预处理）](./src/lib/reader/) -> [处理器（数据转换）](./src/lib/processor/) -> [生成器](./src/lib/exporter/)

## 为何创建此项目

1. 好玩
2. 帮助萌新分配左手的两个键，而不是一直单戳

## TODO

1. 完成基本功能
2. 创建 GUI 程序
3. 创建 github-action 以便于在每次提交自动构建多平台二进制文件
4. 配置自动格式化程序，在每次提交前检查
5. 配置自动类型检查工具，在每次提交前检查
6. README 引导开发人员创建虚拟环境
7. 贡献文档要求强制进行类型检查
8. 给 README 添加徽章
9. 写项目单元测试
10. 配置线上单元测试检查的软件
11. 编写英文文档
12. 软件支持英文
13. cli 程序
14. 程序运行加上计时器
15. 允许用户运行完的时候输入一个值直接打开浏览器到项目页面
16. 生成后提供直接修改游戏内铺面标题的设置
17. 添加时间计量，每个步骤花费了多少时间
18. 允许用户使用 json 文件配置
19. 允许用户设置主要指，然后 1k 转 2k 的时候把 note 先全都丢那个轨道上

## 更新日志

...
