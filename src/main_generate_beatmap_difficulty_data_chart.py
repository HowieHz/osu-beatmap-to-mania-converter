from custom_types import ManiaHitObject
from exporter import generate_beatmap_difficulty_data_chart
from reader import hit_objects_parser, load_hit_objects_list, load_osu_file_metadata

if __name__ == "__main__":
    osu_file_full_path: str = ""
    while not osu_file_full_path:
        osu_file_full_path = input(
            "Input osu file full path\n输入 osu 文件完整路径："
        ).strip()
    window: int = int(
        input(
            "Input window size (in milliseconds, must be an integer, suggest 100 or 1000, default is 1000)\n输入窗口大小（单位为毫秒，必须为整数，建议 100、200、500、1000，默认值为 1000）："
        )
        or 1000
    )
    time_range_start: int = int(
        input(
            "Input time range start (in milliseconds, must be an integer, -1 for no limit, default is -1)\n输入时间范围开始（单位为毫秒，必须为整数，-1 表示不设限，默认值为 -1）："
        )
        or -1
    )
    time_range_end: int = int(
        input(
            "Input time range end (in milliseconds, must be an integer, -1 for no limit, default is -1)\n输入时间范围结束（单位为毫秒，必须为整数，-1 表示不设限，默认值为 -1）："
        )
        or -1
    )
    print(
        f"Processing time range: [{time_range_start}, {time_range_end})\n处理时间范围：[{time_range_start}, {time_range_end})"
    )
    print("Reading...\n读取中...\n")

    # 读取并解析 [HitObjects] 下每行的数据为更易于处理的形式
    parsed_hit_objects_list: list[ManiaHitObject] = hit_objects_parser(
        load_osu_file_metadata(osu_file_full_path),
        load_hit_objects_list(osu_file_full_path),
    )

    print("Building charts...\n正在生成图表...\n")

    generate_beatmap_difficulty_data_chart(
        parsed_hit_objects_list,
        window=window,
        time_range=(time_range_start, time_range_end),
        generate_individual_key_charts=False,
        generate_individual_adjacent_keys_charts=False,
    )

    print(
        "Generated in the charts folder in the current directory\n已生成在当前目录下的 charts 文件夹中\n"
    )
    input("Press Enter to exit\n按 Enter 退出\n")
