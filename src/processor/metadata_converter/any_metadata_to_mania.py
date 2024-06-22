def any_metadata_to_mania(osu_file_metadata: list[str], keys: int) -> list[str]:
    """将 osu 铺面的元数据转换成 osu!mania 的元数据\n
    1. 设置 Mode 标识为 mania\n
    2. 设置 CircleSize 为 keys 参数\n
    3, 设置 BeatmapSetID 为 -1\n

    Args:
        osu_file_metadata (list[str]): 未被转换的元数据列，每行应有换行符（"\\n"）
        keys (int): 铺面键数

    Returns:
        list[str]: 转换后的元数据列，每行应有换行符（"\\n"）
    """
    # 设置键数为 keys
    # 找到目标索引然后替换，整个文件 CircleSize 开头的按理来说只有这一处
    for line in osu_file_metadata:
        if line.startswith("CircleSize:"):
            osu_file_metadata[osu_file_metadata.index(line)] = f"CircleSize:{keys}\n"
            break

    # 设置 BeatmapSetID 为 -1
    for line in osu_file_metadata:
        if line.startswith("BeatmapSetID:"):
            osu_file_metadata[osu_file_metadata.index(line)] = "BeatmapSetID:-1\n"
            break

    # 设置 Mode 标识为 mania
    # 找到目标索引然后替换，整个文件 Mode 开头的按理来说只有这一处
    for line in osu_file_metadata:
        if line.startswith("Mode:"):
            osu_file_metadata[osu_file_metadata.index(line)] = "Mode: 3\n"
            break
    return osu_file_metadata
