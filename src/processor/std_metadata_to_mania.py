def any_metadata_to_mania(osu_file_metadata: list[str]) -> list[str]:
    """将 osu 铺面的元数据转换成 osu!mania 的元数据

    Args:
        osu_file_metadata (list[str]): 未被转换的元数据列，每行应有换行符（"\\n"）

    Returns:
        list[str]: 转换后的元数据列，每行应有换行符（"\\n"）
    """
    # 找到目标索引然后替换，整个文件 Mode 开头的按理来说只有这一处
    # 所以以防万一出现 "Mode:  0\n"，如果没找到，"Mode: 0\n"。就会去找第一个 Mode 开头之后替换。
    try:
        osu_file_metadata[osu_file_metadata.index("Mode: 0\n")] = "Mode: 3\n"
    except ValueError:
        for line in osu_file_metadata:
            if line.startswith("Mode:"):
                osu_file_metadata[osu_file_metadata.index(line)] = "Mode: 3\n"
                break
    return osu_file_metadata
