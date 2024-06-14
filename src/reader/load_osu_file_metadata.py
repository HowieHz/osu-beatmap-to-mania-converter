import os

from logger import debug

# .osu 文件官方文档 https://osu.ppy.sh/wiki/zh/Client/File_formats/osu_%28file_format%29


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
            debug("read line", data=line)
            if line == "[HitObjects]\n":
                append_meta_data_list_flag = False

            if append_meta_data_list_flag:
                meta_data_list.append(line)
            else:
                if line == "\n":  # 读到 \n 代表 [HitObjects] 的部分结束
                    append_meta_data_list_flag = True

        debug("meta_data_list", data=meta_data_list)
        return meta_data_list
