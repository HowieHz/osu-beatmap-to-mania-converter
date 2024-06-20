from custom_types import ManiaHitObject


def mania_hit_objects_parser(
    osu_file_metadata: list[str], hit_objects_list: list[str]
) -> list[ManiaHitObject]:
    """解析 [HitObjects] 下每行的数据为更易于处理的形式

    Args:
        osu_file_metadata (list[str]): 铺面元数据
        hit_objects_list (list[str]): [HitObjects] 下每行的数据，例如 256,192,11000,21,2

    Returns:
        list[HitObject]: 一个列表，装了解析后的铺面描述
    """
    rt_list: list[ManiaHitObject] = []

    for hit_object in hit_objects_list:
        object_type: str = ""
        start_time: int | float = 0  # 开始时间，毫秒
        end_time: int | float = 0  # 结束时间，毫秒
        key_position: int = 1  # 键的在哪个轨道，最左边是 1
        number_of_key: int = _read_key_info_from_metadata(
            osu_file_metadata
        )  # 存储铺面是几 k 的

        object_params: list[str] = hit_object.split(",")

        # 处理下数据，十进制转二进制，然后去掉左边 0b 标识，补齐八位避免 IndexError，转换成字符串方便直接取位值
        raw_type: str = str(bin(int(object_params[3]))).removeprefix("0b").zfill(8)

        if raw_type[-1] == "1":
            # 音符（泡泡，米，Note）
            object_type = "hit circle"
            start_time = end_time = int(object_params[2])
            key_position = _x_to_key(int(object_params[0]), number_of_key)
        elif raw_type[-8] == "1":
            # mania 长音符（长条，long note，LN，面）
            # 样例数据 448,192,31331,128,8,31836:2:0:0:0:
            object_type = "hold"
            start_time = int(object_params[2])
            end_time = int(object_params[5].split(":")[0])
            key_position = _x_to_key(int(object_params[0]), number_of_key)
        elif raw_type[-2] == "1" or raw_type[-4] == "1":
            # 主模式滑条 主模式转盘
            object_type = "unknown"
        else:
            object_type = "unknown"

        rt_list.append(
            {
                "type": object_type,
                "start_time": start_time,
                "end_time": end_time,
                "key": key_position,
            }
        )

    return rt_list


def _x_to_key(x: int, keys: int) -> int:
    """x 值转 key 位置

    Args:
        x (int): x 值
        keys (int): 多少 key 的铺面

    Returns:
        int: 位置，从左到右第一轨是 1
    """
    return int(x * keys // 512) + 1


def _read_key_info_from_metadata(osu_file_metadata: list[str]) -> int:
    """读取元数据中标识铺面是几 k

    Args:
        osu_file_metadata (list[str]): 元数据列表

    Returns:
        int: 铺面标识的是几 k
    """
    for line in osu_file_metadata:
        if line.startswith("CircleSize:"):
            return int(line.removesuffix("CircleSize:").strip())
