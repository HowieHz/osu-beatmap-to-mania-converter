def load_osu_file_metadata(file_full_path: str) -> list[str]:
    """加载 osu 格式的文件中的除去 [HitObjects] 的部分

    Args:
        file_full_path (str): osu 文件完整路径

    Returns:
        list[str]: 文件数据，除去 [HitObjects] 的部分，每行末尾带回车（\\n)
    """
    meta_data_list: list[str] = []

    with open(file=file_full_path, mode="r+", encoding="utf-8") as f:
        # 警告：此处把文件全读到内存里，如果遇到极端不正常的文件（几个 G 的铺面）可能导致内存占用过大
        lines: list[str] = f.readlines()

        # 这个为 True 就把接下来的内容写到输出列表内
        append_meta_data_list_flag: bool = True

        for line in lines:
            if line.rstrip() == "[HitObjects]":
                append_meta_data_list_flag = False
            
            if not append_meta_data_list_flag:
                if line.strip() == "":  # 读到 \n 代表 [HitObjects] 的部分结束
                    append_meta_data_list_flag = True
                continue

            meta_data_list.append(line)

        return meta_data_list
