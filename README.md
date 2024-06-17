# osu-beatmap-to-mania-converter

> Convert OSU!Standard(osu!std)/OSU!Taiko to OSU!Mania

![GitHub](https://img.shields.io/github/license/HowieHz/osu-beatmap-to-mania-converter)
![GitHub all releases](https://img.shields.io/github/downloads/HowieHz/osu-beatmap-to-mania-converter/total)
![GitHub release (latest by date)](https://img.shields.io/github/downloads/HowieHz/osu-beatmap-to-mania-converter/latest/total)
![GitHub repo size](https://img.shields.io/github/repo-size/HowieHz/osu-beatmap-to-mania-converter)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a657069d04fe47588b6c44d55883c4e1)](https://app.codacy.com/gh/HowieHz/osu-beatmap-to-mania-converter/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

## 主要功能

- 将 OSU!Standard 铺面转换为 OSU!Mania 铺面。
- （制作中）将 OSU!Taiko 铺面转换为 OSU!Mania 铺面。

如果想支持本项目就点个 star 吧，你的支持将指引我砥砺前行。

如在使用中遇到 Bug，想提出新功能，对现有功能不满，想提出建议，想问问题，想进行讨论。欢迎前来[提出新的 Issue](https://github.com/HowieHz/osu-beatmap-to-mania-converter/issues/new/choose)。

## 为何创建此项目

For fun.

## 这个软件的用途

### 对于 OSU!Standard -> OSU!Mania

1. 帮助萌新分配左手的两个键，而不是一直单戳
2. OSU!Mania 铺师直接从 OSU!Standard 铺面采音用
3. 手法分析/铺面解析
4. 在主模式开 Autopilot mod 享受游戏（广义上，此软件生成的铺面相较于原铺，就相当于 NO SV 铺面相较于 SV 铺面）

### 对于 OSU!Taiko -> OSU!Mania

1. OSU!Mania 铺师直接从 OSU!Taiko 铺面采音用
2. 手法分析/铺面解析
3. ...

[我有不同的见解/我想补充](https://github.com/HowieHz/osu-beatmap-to-mania-converter/issues/new/choose)

## 这个软件可以生成怎样的铺面

### 对于 OSU!Standard 转 OSU!Mania

1. 符合一般玩家双指分配的铺面（低密度单戳，高密度两指交替击打）
2. 单戳练习铺生成器 （参数例：最大叠键数 1000000，最小叠键时间间距设置为 0）
3. 强双练习铺生成器 （参数例：最大叠键数 1，最小叠键时间间隔 1000000）

---

- [osu-beatmap-to-mania-converter](#osu-beatmap-to-mania-converter)
  - [主要功能](#主要功能)
  - [为何创建此项目](#为何创建此项目)
  - [这个软件的用途](#这个软件的用途)
    - [对于 OSU!Standard -\> OSU!Mania](#对于-osustandard---osumania)
    - [对于 OSU!Taiko -\> OSU!Mania](#对于-osutaiko---osumania)
  - [这个软件可以生成怎样的铺面](#这个软件可以生成怎样的铺面)
    - [对于 OSU!Standard 转 OSU!Mania](#对于-osustandard-转-osumania)
    - [输出铺面类型](#输出铺面类型)
      - [OSU!Standard 转 OSU!Mania](#osustandard-转-osumania)
    - [OSU!Taiko 转 OSU!Mania](#osutaiko-转-osumania)
    - [输出规则](#输出规则)
      - [OSU!Standard 转 OSU!Mania](#osustandard-转-osumania-1)
    - [OSU!Taiko 转 OSU!Mania](#osutaiko-转-osumania-1)
    - [OSU!Mania 铺面输出可配置项](#osumania-铺面输出可配置项)
      - [基础设置](#基础设置)
      - [输出目标 OSU!Mania 2k/4k 为才有的配置项](#输出目标-osumania-2k4k-为才有的配置项)
      - [未完成的功能（TODO）](#未完成的功能todo)
  - [如何下载使用](#如何下载使用)
    - [通过二进制文件运行](#通过二进制文件运行)
    - [Windows](#windows)
    - [MacOS \& Linux](#macos--linux)
    - [通过源码运行](#通过源码运行)
  - [程序结构](#程序结构)
  - [软件如何根据 .osu 文件生成 Mania 铺面](#软件如何根据-osu-文件生成-mania-铺面)
    - [osu!std to osu!mania](#osustd-to-osumania)
      - [to mania!mania 1k](#to-maniamania-1k)
      - [to osu!mania 2k](#to-osumania-2k)
      - [to osu!mania 4k](#to-osumania-4k)
    - [osu!taiko to osu!mania 4k](#osutaiko-to-osumania-4k)
  - [TODO](#todo)
    - [优先且易实现](#优先且易实现)
    - [优先](#优先)
    - [滞后](#滞后)
      - [i18n](#i18n)
      - [项目环境配置/文档](#项目环境配置文档)
    - [后备](#后备)
  - [相关文档](#相关文档)
  - [Star History](#star-history)
  - [更新日志](#更新日志)

---

### 输出铺面类型

#### OSU!Standard 转 OSU!Mania

- OSU!Mania 1k
- OSU!Mania 2k
- OSU!Mania 4k（将 4k 左边两轨当 2k 使用，无需玩家制作 2k 界面皮肤）

### OSU!Taiko 转 OSU!Mania

> 咚（红色音符），咔（蓝色音符）。红色在内侧，蓝色在外侧。

Taiko 长条

- OSU!Mania 4k
  - 模式 1
  - ...

### 输出规则

#### OSU!Standard 转 OSU!Mania

1. 主模式音符 -> mania 音符
2. 主模式长条 -> mania 长条
3. 主模式转盘 -> mania 长条

### OSU!Taiko 转 OSU!Mania

1. 红圈, 蓝圈 -> mania 音符
2. 大红圈，大蓝圈 -> mania 音符，但是同时生成在两个轨道上，形成双押（可以设置为转换为单键）
3. 长黄条（滚动条） -> mania 长条
4. 大的长黄条 -> mania 长条
5. 拨浪鼓（转盘） -> mania 长条

注：

1. 长黄条/大的长黄条的转换是不完美的。因为实际上你游玩 taiko 铺面的时候，不论是大黄条还是小黄条，应按照黄条上面的白点的节奏击打任意一个键，而不是作为一个长条来按。
2. 拨浪鼓（转盘）的转换是不完美的。因为实际上你游玩 taiko 铺面的时候，你应该交替击打红蓝键来完成转盘。

### OSU!Mania 铺面输出可配置项

#### 基础设置

1. 设置惯用单戳指所在轨道：物件会优先生成在这个轨道上（main key）
2. 设置铺面从哪一轨开始生成（start key）
3. 是否移除铺面变速（可选项：全移除，不移除，仅移除继承时间点（绿线））（Remove SV）

#### 输出目标 OSU!Mania 2k/4k 为才有的配置项

1. 交互起手设置：最开始的交互哪个轨道起手（Trill start key）
2. 纵连两键间距小于多少毫秒开始转交互（Minimum Jack Time Interval）
3. 几个纵开始转交互（Maximum number of jack notes）

#### 未完成的功能（TODO）

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
3. （TODO）检测 ln 尾部和下一个 note 的间距，小于一个值就把这个 note 放到另一列上
4. （TODO）允许用户调整 2k -> 4k 对应轨道映射

## 如何下载使用

### 通过二进制文件运行

### Windows

从 [Releases](https://github.com/HowieHz/osu-beatmap-to-mania-converter/releases) 下载最新版本二进制文件。
解压后，运行 `.exe` 为后缀的程序，即可开始运行程序，随后根据程序引导完成操作即可。

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

[读取器（包括预处理）](./src/lib/reader/) -> [处理器（数据转换）](./src/lib/processor/) -> [生成器](./src/lib/exporter/)

## 软件如何根据 .osu 文件生成 Mania 铺面

如依然有不理解的，欢迎致邮 `howie_hzgo@outlook.com`。如果你正在开发相关读取铺面文件/生成铺面的工具我会在力所能及的层面提供帮助。

### osu!std to osu!mania

共同的步骤

1. 读取除 [HitObjects] 以外的信息，命名为 osu_file_metadata
2. 读取 [HitObjects] 信息，根据 osu_file_metadata 使用 std_hit_objects_parser 函数进行预处理，命名为 parsed_hit_objects_list
3. 使用 std_object_type_to_mania_1k 函数将 parsed_hit_objects_list 中类型为主模式滑条和主模式转盘的转换为 Mania 长音符，并且放到 1 轨，处理后的命名为 parsed_mania_1k_hit_objects_list
4. 根据配置项去除铺面 sv 信息（处理 osu_file_metadata）

#### to mania!mania 1k

1. 将元数据处理为 mania 1k 的元数据（处理 osu_file_metadata）
   - 设置 Mode 为 3 （设置铺面模式为 Mania）
   - 设置 CircleSize 为 1 （设置信息为 1k）
   - 设置 BeatmapSetID 为 -1
2. 根据 osu_file_metadata 和 parsed_mania_1k_hit_objects_list 生成铺面

#### to osu!mania 2k

1. 根据配置项处理 parsed_mania_1k_hit_objects_list，处理后的命名为 parsed_mania_2k_hit_objects_list
2. 将元数据处理为 mania 2k 的元数据（处理 osu_file_metadata）
   - 设置 Mode 为 3 （设置铺面模式为 Mania）
   - 设置 CircleSize 为 2 （设置信息为 2k）
   - 设置 BeatmapSetID 为 -1
3. 根据 osu_file_metadata 和 parsed_mania_2k_hit_objects_list 生成铺面

#### to osu!mania 4k

1. 根据配置项处理 parsed_mania_1k_hit_objects_list，处理后的命名为 parsed_mania_2k_hit_objects_list
2. 将元数据处理为 mania 4k 的元数据（处理 osu_file_metadata）
   - 设置 Mode 为 3 （设置铺面模式为 Mania）
   - 设置 CircleSize 为 4 （设置信息为 4k）
   - 设置 BeatmapSetID 为 -1
3. 根据 osu_file_metadata 和 parsed_mania_2k_hit_objects_list 生成铺面

### osu!taiko to osu!mania 4k

1. 读取除 [HitObjects] 以外的信息，命名为 osu_file_metadata
2. 读取 [HitObjects] 信息，根据 osu_file_metadata 使用 taiko_hit_objects_parser 函数进行预处理，命名为 parsed_hit_objects_list
   - 预处理分类了大黄条，小黄条，大红圈，小红圈，大蓝圈，小篮圈，拨浪鼓（转盘）
   - 按照英文官网 wiki 起的类型名：large slider, slider, large red notes, red notes, large blue note, blue note, spinner
3. 用 taiko_object_type_to_mania_5k 函数将 parsed_hit_objects_list 中类型为大小黄条和拨浪鼓（转盘）的转换为 Mania 长音符，处理后的命名为 parsed_mania_5k_hit_objects_list
   - 从左到右依次是 1-5 轨道
   - 1 轨道放小红圈转换后的音符
   - 2 轨道放大红圈转换后的音符
   - 3 轨道放小蓝圈转换后的音符
   - 4 轨道放大篮圈转换后的音符
   - 5 轨道放大/小黄条和拨浪鼓转换后的长音符
4. 根据配置项去除铺面 sv 信息（处理 osu_file_metadata）
5. 根据配置项处理 parsed_mania_5k_hit_objects_list，处理后的命名为 parsed_mania_4k_hit_objects_list
6. 将元数据处理为 mania 4k 的元数据（处理 osu_file_metadata）
   - 设置 Mode 为 3 （设置铺面模式为 Mania）
   - 设置 CircleSize 为 4 （设置信息为 4k）
   - 设置 BeatmapSetID 为 -1
7. 根据 osu_file_metadata 和 parsed_mania_4k_hit_objects_list 生成铺面

## TODO

### 优先且易实现

1. 添加时间计量，每个步骤花费了多少时间

### 优先

1. cli 程序
2. 完成其他的 mania 2k 输出选项
   1. 生成后提供直接修改游戏内铺面标题的设置

### 滞后

1. 允许用户运行完的时候输入一个值直接打开浏览器到项目页面
2. （前置任务：cli 程序）允许用户使用 json 文件配置
3. 语言文字中的默认值从 options_default 取

#### i18n

1. 编写英文文档
2. 软件支持英文

#### 项目环境配置/文档

1. 创建 github-action 以便于在每次提交自动构建多平台二进制文件
2. 配置自动格式化程序，在每次提交前检查
3. 配置自动类型检查工具，在每次提交前检查
4. README 引导开发人员创建虚拟环境
5. 贡献文档要求强制进行类型检查
6. 写项目单元测试
7. 配置线上单元测试检查的软件

### 后备

1. 创建 GUI 程序（肯定是基于 cli，做个 cli 的调用。用简单的 python web 框架调用 cli 是上策，用其他语言写 gui 算中策，用 pyside/pyqt 是下策）

## 相关文档

1. [.osu 文件解释文档](https://osu.ppy.sh/wiki/zh/Client/File_formats/osu_%28file_format%29)

## Star History

<a href="https://star-history.com/#HowieHz/osu-beatmap-to-mania-converter&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HowieHz/osu-beatmap-to-mania-converter&type=Date&theme=dark" loading="lazy" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HowieHz/osu-beatmap-to-mania-converter&type=Date" loading="lazy" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HowieHz/osu-beatmap-to-mania-converter&type=Date" loading="lazy" />
 </picture>
</a>

## 更新日志

见 [Releases](https://github.com/HowieHz/osu-beatmap-to-mania-converter/releases)
