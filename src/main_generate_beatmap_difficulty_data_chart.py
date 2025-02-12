import os
from typing import cast

from custom_types import ManiaHitObject
from exporter.generate_beatmap_difficulty_data_chart import (
    generate_beatmap_difficulty_data_chart,
)
from reader import hit_objects_parser, load_hit_objects_list, load_osu_file_metadata


def call_beatmap_difficulty_data_chart_generator(
    osu_file_full_path: str,
    time_range_start: int,
    time_range_end: int,
    window: int,
    dir_path: str,
):
    """生成铺面图像

    Args:
        osu_file_full_path (str): 铺面完整路径
        time_range_start (int): 开始时间刻 单位为毫秒
        time_range_end (int): 结束时间刻 单位为毫秒
        window (int): 窗口大小 单位为毫秒
        dir_path (str): 生成目录路径
    """
    print(
        f"Processing time range: [{time_range_start}, {time_range_end})\n处理时间范围：[{time_range_start}, {time_range_end})"
    )
    print(f"Reading {osu_file_full_path}...\n读取中 {osu_file_full_path}...\n")

    # 读取并解析 [HitObjects] 下每行的数据为更易于处理的形式
    # 简单小程序，相信用户输入的是 mania 铺面不是其他别的
    parsed_hit_objects_list: list[ManiaHitObject] = cast(
        list[ManiaHitObject],
        hit_objects_parser(
            load_osu_file_metadata(osu_file_full_path),
            load_hit_objects_list(osu_file_full_path),
        ),
    )

    print("Building charts...\n正在生成图表...\n")

    generate_beatmap_difficulty_data_chart(
        parsed_hit_objects_list,
        window=window,
        time_range=(time_range_start, time_range_end),
        generate_individual_key_charts=False,
        generate_individual_adjacent_keys_charts=False,
        dir_path=dir_path,
    )

    print(f"Generated charts in {dir_path}\n已生成图表在 {dir_path}\n")


if __name__ == "__main__":
    input_value: str = ""
    osu_file_full_path: str

    print(
        """\
Press Enter to use the default value.
如需取默认值，直接回车即可\n"""
    )

    window: int = int(
        input(
            """\
Enter the window size (in milliseconds, must be an integer, recommended values are 100, 200, 500, 1000. Default is 1000)
The larger the window size, the smoother the curve but less likely to show small changes.:
输入窗口大小（单位为毫秒，必须为整数，建议 100、200、500、1000。默认值为 1000）
窗口值越大，曲线越平滑但是不易展现出小突变："""
        )
        or 1000
    )
    time_range_start: int = int(
        input(
            """\
Input time range start (in milliseconds, must be an integer, -1 for no limit, default is -1):
输入开始时间刻（单位为毫秒，必须为整数，-1 表示不设限，默认值为 -1）："""
        )
        or -1
    )
    time_range_end: int = int(
        input(
            """\
Input time range end (in milliseconds, must be an integer, -1 for no limit, default is -1)
输入结束时间刻（单位为毫秒，必须为整数，-1 表示不设限，默认值为 -1）："""
        )
        or -1
    )

    while not input_value:
        input_value = input(
            """\
Enter the full path of the osu file to specify the beatmap to convert directly Or Type f and press Enter to enter batch tasks mode.
输入 osu 文件完整路径直接指定要转换的铺面 或者 输入 f 之后回车进入批量转换模式："""
        ).strip()

    if input_value.lower() != "f":
        osu_file_full_path = input_value

        call_beatmap_difficulty_data_chart_generator(
            osu_file_full_path=osu_file_full_path,
            time_range_start=time_range_start,
            time_range_end=time_range_end,
            window=window,
            dir_path="charts",
        )

    else:
        osu_file_dir_path: str = ""
        while not osu_file_dir_path:
            osu_file_dir_path = input(
                """\
Enter the directory path containing .osu files for batch processing:
输入包含 .osu 文件的目录路径以进行批量处理："""
            ).strip()

        for filename in os.listdir(osu_file_dir_path):
            if filename.endswith(".osu"):
                osu_file_full_path = os.path.join(osu_file_dir_path, filename)
                call_beatmap_difficulty_data_chart_generator(
                    osu_file_full_path=osu_file_full_path,
                    time_range_start=time_range_start,
                    time_range_end=time_range_end,
                    window=window,
                    dir_path=os.path.join(
                        osu_file_dir_path, filename.removesuffix(".osu")
                    ),
                )

    print("Generation complete.\n生成完毕\n")
    input("Press Enter to exit\n按 Enter 退出\n")
