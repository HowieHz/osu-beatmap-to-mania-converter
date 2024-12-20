from custom_types import ManiaHitObject
from exporter import generate_beatmap_difficulty_data_chart
from reader import hit_objects_parser, load_hit_objects_list, load_osu_file_metadata

if __name__ == "__main__":
    osu_file_full_path = input("Input osu file full path\n输入 osu 文件完整路径: ")
    print("Reading...\n读取中...\n")

    # 读取并解析 [HitObjects] 下每行的数据为更易于处理的形式
    parsed_hit_objects_list: list[ManiaHitObject] = hit_objects_parser(
        load_osu_file_metadata(osu_file_full_path),
        load_hit_objects_list(osu_file_full_path),
    )

    print("Building charts...\n正在生成图表...\n")

    generate_beatmap_difficulty_data_chart(
        parsed_hit_objects_list,
        window=100,
        time_range=(-1, -1),
        generate_individual_key_charts=True,
        generate_individual_adjacent_keys_charts=True,
    )

    print(
        "Generated in the charts folder in the current directory\n已生成在当前目录下的 charts 文件夹中\n"
    )
    input("Press Enter to exit\n按 Enter 退出\n")
