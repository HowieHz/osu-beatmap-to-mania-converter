import os

from logger import debug
from copy import deepcopy

# .osu 文件官方文档 https://osu.ppy.sh/wiki/zh/Client/File_formats/osu_%28file_format%29

def load_osu_file(file_full_path: str) -> list[str]:
    """加载 osu 格式的文件中的 HitObjects

    Args:
        file_full_path (str): osu 文件完整路径

    Returns:
        list[str]: [HitObjects] 下每行的数据，例如 256,192,11000,21,2
    """
    hit_objects_list:list[str] = []
    
    with open(file=file_full_path, mode="r+", encoding="utf-8") as f:
        debug(f"osu file format version: {f.readline()}") # 第一行应该是 osu file format v14
        
        lines: list[str] = list(deepcopy(f.readlines())) # 警告：此处把文件全读到内存里，如果遇到极端不正常的文件（几个 G 的铺面）可能导致内存占用过大
        for line in lines:
            debug(f"read line: {line}")
            if line == "[HitObjects]\n":
                lines = lines[1:] # 去除第一项
                break
        debug(f"lines {lines}")
        # 现在 lines 是 [HitObjects] 开始的，再去掉一行
        lines = lines[1:]
        
        for line in lines:
            debug(f"read line 2: {line}")  # 读到的 line 都是一串数据最后加个 \n 
            if line == "\n": # 不停读取，直到读取到空行就 break
                break
            hit_objects_list.append(line.removesuffix("\n"))
        
        debug(f"hit_objects_list: {hit_objects_list}")
        return hit_objects_list
