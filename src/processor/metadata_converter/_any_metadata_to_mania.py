def _any_metadata_to_mania(osu_file_metadata: list[str]) -> list[str]:
    """设置元数据 Mode 标识为 mania

    Args:
        osu_file_metadata (list[str]): 未被转换的元数据列，每行应有换行符（"\\n"）

    Returns:
        list[str]: 转换后的元数据列，每行应有换行符（"\\n"）
    """
    # 找到目标索引然后替换，整个文件 Mode 开头的按理来说只有这一处
    for line in osu_file_metadata:
        if line.startswith("Mode:"):
            osu_file_metadata[osu_file_metadata.index(line)] = "Mode: 3\n"
            break
    return osu_file_metadata
