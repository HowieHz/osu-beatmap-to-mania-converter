from typing import cast


def any_metadata_remove_sv(
    remove_sv_option: str, osu_file_metadata: list[str]
) -> list[str]:
    """移除元数据中的变速

    Args:
        remove_sv_option (str): 是否移除铺面变速（可选项：全移除 - all，不移除 - none，仅移除继承时间点（绿线） - inherited_timing_points）
        osu_file_metadata (list[str]): 未被转换的元数据列，每行应有换行符（"\\n"）

    Returns:
        list[str]: 转换后的元数据列，每行应有换行符（"\\n"）
    """
    if remove_sv_option == "none":
        return osu_file_metadata

    marked_osu_file_metadata = cast(
        list[str | None], osu_file_metadata
    )  # None 是被标记要被移除的行
    remove_line_flag: bool = False
    skip_line_flag: int = 0
    ret_osu_file_metadata: list[str]

    if remove_sv_option == "all":
        for index, line in enumerate(osu_file_metadata):
            if skip_line_flag > 0:
                skip_line_flag -= 1
                continue

            if line.rstrip() == "[TimingPoints]":  # 识别到 TimingPoints
                remove_line_flag = True
                skip_line_flag = 1  # 跳过第一行红线
                continue

            if line.rstrip() == "" and remove_line_flag:  # 读取到 TimingPoints 末了
                break

            if remove_line_flag:
                marked_osu_file_metadata[index] = (
                    None  # 要是这里直接 remove 会导致索引错乱，标记为 None，待会统一清理
                )

        ret_osu_file_metadata = list(filter(None, marked_osu_file_metadata))
    elif remove_sv_option == "inherited_timing_points":
        for index, line in enumerate(osu_file_metadata):
            if skip_line_flag > 0:
                skip_line_flag -= 1
                continue

            if line.rstrip() == "[TimingPoints]":  # 识别到 TimingPoints
                remove_line_flag = True
                skip_line_flag = 1  # 跳过第一行红线
                continue

            if line.rstrip() == "" and remove_line_flag:  # 读取到 TimingPoints 末了
                break

            if remove_line_flag and line.rstrip().split(",")[-2] == "0":
                marked_osu_file_metadata[index] = (
                    None  # 要是这里直接 remove 会导致索引错乱，标记为 None，待会统一清理
                )

        ret_osu_file_metadata = list(filter(None, marked_osu_file_metadata))

    return ret_osu_file_metadata
