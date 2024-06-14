import os

from logger import debug

# .osu 文件官方文档 https://osu.ppy.sh/wiki/zh/Client/File_formats/osu_%28file_format%29


def load_hit_objects_list(file_full_path: str) -> list[str]:
    """加载 osu 格式的文件中的 HitObjects

    Args:
        file_full_path (str): osu 文件完整路径

    Returns:
        list[str]: [HitObjects] 下每行的数据，例如 256,192,11000,21,2。已经去除行末换行符（\\n）
    """
    hit_objects_list: list[str] = []

    with open(file=file_full_path, mode="r+", encoding="utf-8") as f:
        # 第一行应该是 osu file format v14
        osu_file_version: str = f.readline()
        debug("osu file format version", data=osu_file_version)

        # 警告：此处把文件全读到内存里，如果遇到极端不正常的文件（几个 G 的铺面）可能导致内存占用过大
        lines: list[str] = f.readlines()

        # 这个为 true 就把接下来的内容写到输出列表内
        append_hit_objects_list_flag: bool = False
        for line in lines:
            debug("read line", data=line)

            # 对列表操作删除不知道为什么没效果，删除了又从文件头开始读，可能是 f.readlines() 的特性，所以做了一个 flag，这样在单个循环内就可以读取
            if append_hit_objects_list_flag:
                # 读到的 line 都是一串数据最后加个 \n
                debug(f"read line(flag on)", data=line)
                # 读取到 \n 代表 [HitObjects] 数据结束，就 break 循环
                if line == "\n":
                    break
                hit_objects_list.append(line.removesuffix("\n"))

            if line == "[HitObjects]\n":
                append_hit_objects_list_flag = True

        debug("hit_objects_list", data=hit_objects_list)
        return hit_objects_list
