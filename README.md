# osu-beatmap-to-mania-converter

> Convert OSU!Standard(osu!std)/OSU!Taiko to OSU!Mania

![GitHub](https://img.shields.io/github/license/HowieHz/osu-beatmap-to-mania-converter)
![GitHub all releases](https://img.shields.io/github/downloads/HowieHz/osu-beatmap-to-mania-converter/total)
![GitHub release (latest by date)](https://img.shields.io/github/downloads/HowieHz/osu-beatmap-to-mania-converter/latest/total)
![GitHub repo size](https://img.shields.io/github/repo-size/HowieHz/osu-beatmap-to-mania-converter)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a657069d04fe47588b6c44d55883c4e1)](https://app.codacy.com/gh/HowieHz/osu-beatmap-to-mania-converter/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

## 主要功能

- 将 OSU!Standard 铺面转换为 OSU!Mania 铺面。
- （！制作中）将 OSU!Taiko 铺面转换为 OSU!Mania 铺面。

如果想支持本项目就点个 star 吧，你的支持将指引我砥砺前行。

如在使用中遇到 Bug，想提出新功能，对现有功能不满，想提出建议，想问问题，想进行讨论。欢迎前来[提出新的 Issue](https://github.com/HowieHz/osu-beatmap-to-mania-converter/issues/new/choose)。

在我的博客上阅读：[点我跳转](https://howiehz.top/archives/osu-beatmap-to-mania-converter-readme)

## 为何创建此项目

For fun.

## 这个软件的用途

### 对于 OSU!Standard 转 OSU!Mania

1. 帮助萌新分配左手的两个键，而不是一直单戳
2. OSU!Mania 铺师直接从 OSU!Standard 铺面采音用
3. 手法分析/铺面解析
4. 在主模式开 Autopilot mod 享受游戏（广义上，此软件生成的铺面相较于原铺，就相当于 NO SV 铺面相较于 SV 铺面）

### 对于 OSU!Taiko 转 OSU!Mania

1. OSU!Mania 铺师直接从 OSU!Taiko 铺面采音用
2. 手法分析/铺面解析
3. ...

[我有不同的见解/我想补充](https://github.com/HowieHz/osu-beatmap-to-mania-converter/issues/new/choose)

## 这个软件可以生成怎样的铺面

### 对于 OSU!Standard 转 OSU!Mania

1. 符合一般玩家双指分配的铺面（低密度单戳，高密度两指交替击打）
2. 单戳练习铺生成器 （参数例：最大叠键数 1000000，最小叠键时间间距设置为 0）
3. 强双练习铺生成器 （参数例：最大叠键数 1，最小叠键时间间隔 1000000）

### 对于 OSU!Taiko 转 OSU!Mania

1. 符合一般玩家手指分配音符的铺面
2. 小红圈和小蓝圈单戳的铺面（参数例：红圈列/蓝圈列最大叠键数 1000000，红圈列/蓝圈列最小叠键时间间距设置为 0）
3. 小红圈和小蓝圈强制两指交换击打的铺面（参数例：红圈列/蓝圈列最大叠键数 1，红圈列/蓝圈列最小叠键时间间距设置为 1000000）

---

- [osu-beatmap-to-mania-converter](#osu-beatmap-to-mania-converter)
  - [主要功能](#主要功能)
  - [为何创建此项目](#为何创建此项目)
  - [这个软件的用途](#这个软件的用途)
    - [对于 OSU!Standard 转 OSU!Mania](#对于-osustandard-转-osumania)
    - [对于 OSU!Taiko 转 OSU!Mania](#对于-osutaiko-转-osumania)
  - [这个软件可以生成怎样的铺面](#这个软件可以生成怎样的铺面)
    - [对于 OSU!Standard 转 OSU!Mania](#对于-osustandard-转-osumania-1)
    - [对于 OSU!Taiko 转 OSU!Mania](#对于-osutaiko-转-osumania-1)
  - [物件转换规则，可生成的铺面类型](#物件转换规则可生成的铺面类型)
    - [OSU!Standard 转 OSU!Mania](#osustandard-转-osumania)
      - [物件转换规则](#物件转换规则)
      - [可生成铺面](#可生成铺面)
    - [OSU!Taiko 转 OSU!Mania](#osutaiko-转-osumania)
      - [物件转换规则](#物件转换规则-1)
      - [可生成铺面](#可生成铺面-1)
  - [软件可配置项说明](#软件可配置项说明)
    - [OSU!Standard 转 OSU!Mania](#osustandard-转-osumania-1)
      - [基础设置](#基础设置)
      - [输出目标 OSU!Mania 2k/4k 为才有的配置项](#输出目标-osumania-2k4k-为才有的配置项)
  - [如何下载使用](#如何下载使用)
    - [通过二进制文件运行交互式命令行程序](#通过二进制文件运行交互式命令行程序)
      - [Windows](#windows)
      - [MacOS \& Linux](#macos--linux)
    - [通过源码运行交互式命令行程序](#通过源码运行交互式命令行程序)
    - [通过二进制文件运行命令行程序](#通过二进制文件运行命令行程序)
      - [Windows 平台](#windows-平台)
      - [MacOS \& Linux 平台](#macos--linux-平台)
    - [通过源码运行命令行程序](#通过源码运行命令行程序)
  - [开发中的雷](#开发中的雷)
    - [读取主模式铺面](#读取主模式铺面)
    - [输出 Mania 模式铺面](#输出-mania-模式铺面)
  - [软件原理解释](#软件原理解释)
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
      - [其他的 mania 2k 输出选项](#其他的-mania-2k-输出选项)
    - [滞后](#滞后)
      - [i18n](#i18n)
      - [项目环境配置/文档](#项目环境配置文档)
    - [后备](#后备)
  - [开发指南](#开发指南)
  - [更新日志](#更新日志)
  - [项目数据统计](#项目数据统计)
    - [Star History](#star-history)

---

## 物件转换规则，可生成的铺面类型

### OSU!Standard 转 OSU!Mania

#### 物件转换规则

1. 主模式音符 -> mania 音符
2. 主模式长条 -> mania 长条
3. 主模式转盘 -> mania 长条

#### 可生成铺面

- OSU!Mania 1k
- OSU!Mania 2k
- OSU!Mania 4k（将 4k 左边两轨当 2k 使用，无需玩家制作 2k 界面皮肤）

### OSU!Taiko 转 OSU!Mania

#### 物件转换规则

> 红色在内侧，蓝色在外侧。

1. 小红圈（别名 d（咚）） -> mania 音符
2. 小蓝圈（别名 k（咔）） -> mania 音符
3. 大红圈（别名 D/O） -> mania 音符
4. 大蓝圈（别名 K/X） -> mania 音符
5. 长黄条（滚动条） -> mania 长条
6. 大的长黄条 -> mania 长条
7. 拨浪鼓（转盘） -> mania 长条

注：

1. 长黄条/大的长黄条的转换是不完美的。因为实际上你游玩 taiko 铺面的时候，不论是大黄条还是小黄条，应按照黄条上面的白点的节奏击打任意一个键，而不是作为一个长条来按。
2. 拨浪鼓（转盘）的转换是不完美的。因为实际上你游玩 taiko 铺面的时候，你应该交替击打红蓝键来完成转盘。

#### 可生成铺面

- OSU!Mania 4k
  - 按照手法设置对应从左到右 1 到 4 轨。手法设置用字母 d 和 k 来表示如何分配四个键的位置，如：kddk（直观手法）, ddkk/kkdd（硬抗手法）, dkdk/kdkd/dkkd（少见的手法）。
  - 小红圈就在其中一个 d 轨生成一个音符
  - 大红圈就在两个 d 轨都生成音符，形成双押（可配置将大红圈视为小红圈）
  - 小蓝圈就在其中一个 k 轨生成一个音符
  - 大蓝圈就在两个 k 轨都生成音符，形成双押（可配置将大蓝圈视为小蓝圈）
  - 大/小黄条和拨浪鼓转换后的长音符在某个轨道上生成
  - （具体有关“其中一个 x 轨”，“某个轨道” 具体是其中的哪个轨道，则由具体生成时的软件设置来决定）
- OSU!Mania 5k
  - 从左到右依次是 1-5 轨道
  - 1 轨道放小红圈转换后的音符
  - 2 轨道放大红圈转换后的音符
  - 3 轨道放大/小黄条和拨浪鼓转换后的长音符
  - 4 轨道放小蓝圈转换后的音符
  - 5 轨道放大蓝圈转换后的音符

## 软件可配置项说明

### OSU!Standard 转 OSU!Mania

#### 基础设置

1. 设置惯用单戳指所在轨道：物件会优先生成在这个轨道上（main key）
2. 设置铺面从哪一轨开始生成（start key）
3. 是否移除铺面变速（可选项：全移除，不移除，仅移除继承时间点（绿线））（Remove SV）

#### 输出目标 OSU!Mania 2k/4k 为才有的配置项

1. 交互起手设置：最开始的交互哪个轨道起手（Trill start key）
2. 纵连两键间距小于多少毫秒开始转交互（Minimum Jack Time Interval）
3. 几个纵开始转交互（Maximum number of jack notes）

## 如何下载使用

### 通过二进制文件运行交互式命令行程序

#### Windows

从 [Releases](https://github.com/HowieHz/osu-beatmap-to-mania-converter/releases) 下载最新版本二进制文件。
运行 `.exe` 为后缀的程序，即可开始运行交互式命令行程序，随后根据引导完成操作即可。

#### MacOS & Linux

请看[通过源码运行交互式命令行程序](#通过源码运行交互式命令行程序)

### 通过源码运行交互式命令行程序

下载项目源码，然后进入到项目根目录。
在本地部署 Python3.12 环境后，运行以下指令。
即可从源码运行此项目。

```bash
python ./src/main.py
```

### 通过二进制文件运行命令行程序

#### Windows 平台

从 [Releases](https://github.com/HowieHz/osu-beatmap-to-mania-converter/releases) 下载最新版本二进制文件。
在下载文件所在目录的资源管理器的地址栏，输入 cmd 之后回车，在随后弹出的命令行窗口中输入以下指令

```bash
osu-beatmap-to-mania-converter.exe -h
```

即可看到相关帮助

#### MacOS & Linux 平台

请看[通过源码运行命令行程序](#通过源码运行命令行程序)

### 通过源码运行命令行程序

下载项目源码，然后进入到项目根目录。
在本地部署 Python3.12 环境后，运行以下指令。
即可从源码运行此项目。

```bash
python ./src/main.py -h
```

## 开发中的雷

### 读取主模式铺面

1. 下面这两段都是 ranked 主模式图取的滑条的数据，可以看到滑条后半部分数据是可以省略的。所以取长度数据要用正数索引值去取。
   - 24,164,11997,6,0,L|32:244,1,57.5,6|0,0:0|0:0,0:0:0:0:
   - 308,340,12297,2,0,L|300:260,1,57.5

### 输出 Mania 模式铺面

1. 官方 wiki 是 长键语法：x,y,开始时间,物件类型,长键音效,结束时间,长键音效组
   - 错了，实际上长键语法是 x,y,开始时间,物件类型,长键音效,结束时间:长键音效组
   - 结束时间和长键音效组分隔符是冒号不是逗号！

## 软件原理解释

<details><summary>点我展开查看</summary>

### 程序结构

[读取器（包括预处理）](./src/lib/reader/) -> [处理器（数据转换）](./src/lib/processor/) -> [生成器（生成可以直接写入文件的文本）](./src/lib/exporter/)

### 软件如何根据 .osu 文件生成 Mania 铺面

.osu 文件解析：[官方 wiki：.osu 文件解释文档](https://osu.ppy.sh/wiki/zh/Client/File_formats/osu_%28file_format%29)

如依然有不理解的，欢迎致邮 `howie_hzgo@outlook.com`。如果你正在开发相关读取铺面文件/生成铺面的工具我会在力所能及的层面提供帮助。

#### osu!std to osu!mania

共同的步骤

1. 读取除 [HitObjects] 以外的信息，命名为 osu_file_metadata
2. 读取 [HitObjects] 信息，根据 osu_file_metadata 使用 std_hit_objects_parser 函数进行预处理，命名为 parsed_hit_objects_list
3. 使用 std_object_type_to_mania_1k 函数将 parsed_hit_objects_list 中类型为主模式滑条和主模式转盘的转换为 Mania 长音符，并且放到 1 轨，处理后的命名为 parsed_mania_1k_hit_objects_list
4. 根据配置项去除铺面 sv 信息（处理 osu_file_metadata）

##### to mania!mania 1k

1. 将元数据处理为 mania 1k 的元数据（处理 osu_file_metadata）
   - 设置 Mode 为 3 （设置铺面模式为 Mania）
   - 设置 CircleSize 为 1 （设置信息为 1k）
   - 设置 BeatmapSetID 为 -1
2. 根据 osu_file_metadata 和 parsed_mania_1k_hit_objects_list 生成铺面

##### to osu!mania 2k

1. 根据配置项处理 parsed_mania_1k_hit_objects_list，处理后的命名为 parsed_mania_2k_hit_objects_list
2. 将元数据处理为 mania 2k 的元数据（处理 osu_file_metadata）
   - 设置 Mode 为 3 （设置铺面模式为 Mania）
   - 设置 CircleSize 为 2 （设置信息为 2k）
   - 设置 BeatmapSetID 为 -1
3. 根据 osu_file_metadata 和 parsed_mania_2k_hit_objects_list 生成铺面

##### to osu!mania 4k

1. 根据配置项处理 parsed_mania_1k_hit_objects_list，处理后的命名为 parsed_mania_2k_hit_objects_list
2. 将元数据处理为 mania 4k 的元数据（处理 osu_file_metadata）
   - 设置 Mode 为 3 （设置铺面模式为 Mania）
   - 设置 CircleSize 为 4 （设置信息为 4k）
   - 设置 BeatmapSetID 为 -1
3. 根据 osu_file_metadata 和 parsed_mania_2k_hit_objects_list 生成铺面

#### osu!taiko to osu!mania 4k

1. 读取除 [HitObjects] 以外的信息，命名为 osu_file_metadata
2. 读取 [HitObjects] 信息，根据 osu_file_metadata 使用 taiko_hit_objects_parser 函数进行预处理，命名为 parsed_hit_objects_list
   - 预处理分类了大黄条，小黄条，大红圈，小红圈，大蓝圈，小蓝圈，拨浪鼓（转盘）
   - 按照英文官网 wiki 起的类型名：large slider, slider, large red notes, red notes, large blue note, blue note, spinner
3. 用 taiko_object_type_to_mania_5k 函数将 parsed_hit_objects_list 中类型为大小黄条和拨浪鼓（转盘）的转换为 Mania 长音符，处理后的命名为 parsed_mania_5k_hit_objects_list
   - 从左到右依次是 1-5 轨道
   - 1 轨道放小红圈转换后的音符
   - 2 轨道放大红圈转换后的音符
   - 3 轨道放小蓝圈转换后的音符
   - 4 轨道放大蓝圈转换后的音符
   - 5 轨道放大/小黄条和拨浪鼓转换后的长音符
4. 根据配置项去除铺面 sv 信息（处理 osu_file_metadata）
5. 根据配置项处理 parsed_mania_5k_hit_objects_list，处理后的命名为 parsed_mania_4k_hit_objects_list
6. 将元数据处理为 mania 4k 的元数据（处理 osu_file_metadata）
   - 设置 Mode 为 3 （设置铺面模式为 Mania）
   - 设置 CircleSize 为 4 （设置信息为 4k）
   - 设置 BeatmapSetID 为 -1
7. 根据 osu_file_metadata 和 parsed_mania_4k_hit_objects_list 生成铺面

</details>

## TODO

<details><summary>点我展开查看</summary>

### 优先且易实现

1. 添加时间计量，每个步骤花费了多少时间

### 优先

1. cli 程序
2. 完成其他的 mania 2k 输出选项
   1. 生成后提供直接修改游戏内铺面标题的设置

#### 其他的 mania 2k 输出选项

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

</details>

## 开发指南

见 [CONTRIBUTING](./CONTRIBUTING)

## 更新日志

见 [Releases](https://github.com/HowieHz/osu-beatmap-to-mania-converter/releases)

## 项目数据统计

### Star History

<a href="https://star-history.com/#HowieHz/osu-beatmap-to-mania-converter&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HowieHz/osu-beatmap-to-mania-converter&type=Date&theme=dark" loading="lazy" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HowieHz/osu-beatmap-to-mania-converter&type=Date" loading="lazy" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HowieHz/osu-beatmap-to-mania-converter&type=Date" loading="lazy" />
 </picture>
</a>
