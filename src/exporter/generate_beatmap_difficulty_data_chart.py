from typing import Optional

import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatter, LogLocator

from custom_types import ManiaHitObject


def calculate_kps(
    hit_objects: list[ManiaHitObject],
    window: int = 1000,
    keys_list: Optional[list[int]] = None,
) -> dict[int, int]:
    """计算每秒的键数 (KPS)

    Args:
        hit_objects (list[ManiaHitObject]): 解析后的铺面对象列表
        window (int, optional): 时间窗口，以毫秒为单位. 默认为 1000。
        keys_list (list[int], optional): 计算范围内的键列表. 默认为 None。

    Returns:
        dict[int, int]: 每个时间窗口的起始时间和这个窗口内对应的键数，起始时间以毫秒为单位
    """
    if keys_list is None:
        # 读取 hit_objects 里最大的 key
        max_key = max(obj["key"] for obj in hit_objects)
        keys_list = [i for i in range(1, 1 + max_key)]

    # start_time 和 end_time 以毫秒为单位
    kps_data = {}  # 默认值下 >=0s <1s 放在 [0]，>=1s <2s 放在 [1]，以此类推
    for obj in hit_objects:
        if obj["key"] not in keys_list:
            continue
        window_start_time: int = obj["start_time"] // window
        if window_start_time not in kps_data:
            kps_data[window_start_time] = 1
        else:
            kps_data[window_start_time] += 1
    return kps_data


def calculate_key_time_delta(
    hit_objects: list[ManiaHitObject],
    keys_list: Optional[list[int]] = None,
) -> list[tuple[int, int]]:
    """计算键时间差

    Args:
        hit_objects (list[ManiaHitObject]): 解析后的铺面对象列表
        keys_list (list[int], optional): 计算范围内的键列表. 默认为 None。

    Returns:
        list[tuple[int, int]]: 每个键的起始时间和下一个键的时间差，时间以毫秒为单位
    """
    if keys_list is None:
        # 读取 hit_objects 里最大的 key
        max_key = max(obj["key"] for obj in hit_objects)
        keys_list = [i for i in range(1, 1 + max_key)]

    # 统计 hit_objects_list 中出现的 obj['start_time'] 并且按照升序排列，并且检查 obj['key'] 在 keys_list 范围内
    sorted_start_times: list[int] = sorted(
        {obj["start_time"] for obj in hit_objects if obj["key"] in keys_list}
    )

    # 计算 key_time_delta
    key_time_delta = []
    for i in range(len(sorted_start_times) - 1):
        start_time = sorted_start_times[i]
        next_start_time = sorted_start_times[i + 1]
        delta = next_start_time - start_time
        key_time_delta.append((start_time, delta))
    return key_time_delta


def calculate_avg_key_time_delta(
    hit_objects: list[ManiaHitObject],
    window: int = 1000,
    keys_list: Optional[list[int]] = None,
) -> dict[int, int]:
    """计算平均键时间差 (平均 KTD)

    Args:
        hit_objects (list[ManiaHitObject]): 解析后的铺面对象列表
        window (int, optional): 时间窗口，以毫秒为单位. 默认为 1000。
        keys_list (list[int], optional): 计算范围内的键列表. 默认为 None。

    Returns:
        dict[int, int]: 每个时间窗口的起始时间和这个窗口内对应的平均键时间差，起始时间以毫秒为单位
    """
    if keys_list is None:
        # 读取 hit_objects 里最大的 key
        max_key = max(obj["key"] for obj in hit_objects)
        keys_list = [i for i in range(1, 1 + max_key)]

    # 调用 calculate_key_time_delta 计算
    key_time_deltas = calculate_key_time_delta(hit_objects, keys_list)

    # 计算每个时间窗口的平均键时间差
    time_delta_data: dict[list[int]] = {}
    for start_time, delta in key_time_deltas:
        window_start_time: int = start_time // window
        if window_start_time not in time_delta_data:
            time_delta_data[window_start_time] = []
        time_delta_data[window_start_time].append(delta)

    # 计算每个时间窗口的平均值
    avg_key_time_delta_data: dict[int, int] = {}
    for window_start_time in time_delta_data:
        avg_key_time_delta_data[window_start_time] = sum(
            time_delta_data[window_start_time]
        ) / len(time_delta_data[window_start_time])

    return avg_key_time_delta_data


def generate_beatmap_difficulty_data_chart(
    hit_objects_list: list[ManiaHitObject],
    keys: Optional[int] = None,
    window: int = 1000,
    time_range: tuple[int, int] = (-1, -1),
    generate_individual_key_charts: bool = True,
    generate_individual_adjacent_keys_charts: bool = True,
) -> None:
    """生成图表，表示该铺面的难度信息

    Args:
        hit_objects_list (list[ManiaHitObject]): 铺面物件数据
        keys (int, optional): 铺面键数
        window (int, optional): 时间窗口，以毫秒为单位. 默认为 1000。
        time_range (tuple[int,int], optional): 时间范围，以毫秒为单位，格式 (开始时间, 结束时间), 包括开始时间，不包括结束时间, -1,-1 表示从头到尾，默认 (-1, -1)
        generate_individual_key_charts (bool, optional): 是否生成单独的单轨的图
        generate_individual_adjacent_keys_charts (bool, optional): 是否生成单独的邻轨的图
    """
    # 两类
    # 第一类 横轴时间，纵轴kps
    # 第二类 横轴时间，纵轴前后两键出现时间

    # 第一类提供五张，分别是四条轨和总体
    # 第二类提供八张，分别是四条轨，1+2轨，2+3轨，3+4轨，总体

    if keys is None:
        # 读取 hit_objects 里最大的 key
        keys = max(obj["key"] for obj in hit_objects_list)

    keys_list = [i for i in range(1, 1 + keys)]

    # 横轴为时间，纵轴为 KPS
    # 计算总体铺面 kps
    total_kps = calculate_kps(hit_objects_list, window=window, keys_list=keys_list)
    # 计算每个键的 kps
    keys_kps = {}
    for key in keys_list:
        keys_kps[key] = calculate_kps(hit_objects_list, window=window, keys_list=[key])

    # 还原原始时间
    total_kps = {time * window / 1000: kps for time, kps in total_kps.items()}
    keys_kps = {
        key: {time * window / 1000: kps for time, kps in kps_data.items()}
        for key, kps_data in keys_kps.items()
    }

    # 按照时间范围过滤
    if time_range != (-1, -1):
        start_time, end_time = time_range
        if start_time != -1:
            total_kps = {
                time: kps for time, kps in total_kps.items() if time >= start_time / 1000
            }
            keys_kps = {
                key: {
                    time: kps
                    for time, kps in kps_data.items()
                    if time >= start_time / 1000
                }
                for key, kps_data in keys_kps.items()
            }
        if end_time != -1:
            total_kps = {
                time: kps for time, kps in total_kps.items() if time < end_time / 1000
            }
            keys_kps = {
                key: {
                    time: kps for time, kps in kps_data.items() if time < end_time / 1000
                }
                for key, kps_data in keys_kps.items()
            }

    # 生成折线图

    # 检查 charts 文件夹是否存在，不存在则创建
    import os

    if not os.path.exists("charts"):
        os.makedirs("charts")

    # 生成总体铺面的折线图
    plt.figure(figsize=(10, 5))
    plt.plot(list(total_kps.keys()), list(total_kps.values()), label="Total KPS")
    plt.xlabel("Time (s)")
    plt.ylabel("KPS")
    plt.title("Total KPS over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig("charts/total_kps_chart.png")
    plt.close()

    if generate_individual_key_charts:
        # 生成每个键的折线图
        for key, kps in keys_kps.items():
            plt.figure(figsize=(10, 5))
            plt.plot(list(kps.keys()), list(kps.values()), label=f"Key {key} KPS")
            plt.xlabel("Time (s)")
            plt.ylabel("KPS")
            plt.title(f"Key {key} KPS over Time")
            plt.legend()
            plt.grid(True)
            plt.savefig(f"charts/key_{key}_kps_chart.png")
            plt.close()

    # 把每个键的折线图画一张图里
    plt.figure(figsize=(10, 5))
    for key, kps in keys_kps.items():
        plt.plot(list(kps.keys()), list(kps.values()), label=f"Key {key} KPS")
    plt.xlabel("Time (s)")
    plt.ylabel("KPS")
    plt.title("Keys KPS over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig("charts/keys_kps_chart.png")
    plt.close()

    # 横轴为时间，纵轴为 KTD
    # 计算总体 KTD
    total_ktd = calculate_avg_key_time_delta(
        hit_objects_list, window=window, keys_list=keys_list
    )
    # 计算每个键的 KTD
    keys_ktd = {}
    for key in keys_list:
        keys_ktd[key] = calculate_avg_key_time_delta(
            hit_objects_list, window=window, keys_list=[key]
        )

    # 计算相邻两轨的 KTD，如 1 2 3 4 就要计算 1+2，2+3，3+4
    adjacent_keys_ktd = {}
    for i in range(1, keys):
        adjacent_keys_ktd[f"{i}+{i+1}"] = calculate_avg_key_time_delta(
            hit_objects_list, window=window, keys_list=[i, i + 1]
        )

    # 还原原始时间
    total_ktd = {time * window / 1000: ktd for time, ktd in total_ktd.items()}
    keys_ktd = {
        key: {time * window / 1000: ktd for time, ktd in ktd_data.items()}
        for key, ktd_data in keys_ktd.items()
    }
    adjacent_keys_ktd = {
        key_pair: {time * window / 1000: ktd for time, ktd in ktd_data.items()}
        for key_pair, ktd_data in adjacent_keys_ktd.items()
    }

    # 按照时间范围过滤
    if time_range != (-1, -1):
        start_time, end_time = time_range
        if start_time != -1:
            total_ktd = {
                time: ktd for time, ktd in total_ktd.items() if time >= start_time / 1000
            }
            keys_ktd = {
                key: {
                    time: ktd
                    for time, ktd in ktd_data.items()
                    if time >= start_time / 1000
                }
                for key, ktd_data in keys_ktd.items()
            }
            adjacent_keys_ktd = {
                key_pair: {
                    time: ktd
                    for time, ktd in ktd_data.items()
                    if time >= start_time / 1000
                }
                for key_pair, ktd_data in adjacent_keys_ktd.items()
            }
        if end_time != -1:
            total_ktd = {
                time: ktd for time, ktd in total_ktd.items() if time < end_time / 1000
            }
            keys_ktd = {
                key: {
                    time: ktd for time, ktd in ktd_data.items() if time < end_time / 1000
                }
                for key, ktd_data in keys_ktd.items()
            }
            adjacent_keys_ktd = {
                key_pair: {
                    time: ktd for time, ktd in ktd_data.items() if time < end_time / 1000
                }
                for key_pair, ktd_data in adjacent_keys_ktd.items()
            }

    # 生成折线图

    # 生成总体铺面的折线图
    plt.figure(figsize=(10, 5))
    plt.plot(list(total_ktd.keys()), list(total_ktd.values()), label="Total KTD")
    plt.xlabel("Time (s)")
    plt.ylabel("KTD (ms)")  # 添加单位 ms
    plt.gca().invert_yaxis()  # 纵轴颠倒
    plt.title("Total KTD over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig("charts/total_ktd_chart.png")
    plt.close()

    if generate_individual_key_charts:
        # 生成每个键的折线图
        for key, ktd in keys_ktd.items():
            plt.figure(figsize=(10, 5))
            plt.plot(list(ktd.keys()), list(ktd.values()), label=f"Key {key} KTD")
            plt.xlabel("Time (s)")
            plt.ylabel("KTD (ms)")  # 添加单位 ms
            plt.gca().invert_yaxis()  # 纵轴颠倒
            plt.title(f"Key {key} KTD over Time")
            plt.legend()
            plt.grid(True)
            plt.savefig(f"charts/key_{key}_ktd_chart.png")
            plt.close()

    if generate_individual_adjacent_keys_charts:
        # 生成相邻两轨的折线图
        for key_pair, ktd in adjacent_keys_ktd.items():
            plt.figure(figsize=(10, 5))
            plt.plot(list(ktd.keys()), list(ktd.values()), label=f"Keys {key_pair} KTD")
            plt.xlabel("Time (s)")
            plt.ylabel("KTD (ms)")  # 添加单位 ms
            plt.gca().invert_yaxis()  # 纵轴颠倒
            plt.title(f"Keys {key_pair} KTD over Time")
            plt.legend()
            plt.grid(True)
            plt.savefig(f"charts/keys_{key_pair}_ktd_chart.png")
            plt.close()

    # 生成每个键和相邻两轨的折线图在一张图里
    plt.figure(figsize=(10, 5))
    for key, ktd in keys_ktd.items():
        plt.plot(
            list(ktd.keys()), list(ktd.values()), label=f"Key {key} KTD", color="blue"
        )
    for key_pair, ktd in adjacent_keys_ktd.items():
        plt.plot(
            list(ktd.keys()),
            list(ktd.values()),
            label=f"Keys {key_pair} KTD",
            color="red",
        )
    plt.xlabel("Time (s)")
    plt.ylabel("KTD (ms)")  # 添加单位 ms
    plt.gca().invert_yaxis()  # 纵轴颠倒
    plt.title("Keys and Adjacent Keys KTD over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig("charts/keys_and_adjacent_keys_ktd_chart.png")
    plt.close()

    # 生成对数折线图并标清晰的纵轴刻度

    # 生成总体铺面的折线图
    plt.figure(figsize=(10, 5))
    plt.plot(list(total_ktd.keys()), list(total_ktd.values()), label="Total KTD")
    plt.xlabel("Time (s)")
    plt.ylabel("KTD (ms)")  # 添加单位 ms
    plt.yscale("log")  # 设置纵轴为对数尺度
    plt.gca().invert_yaxis()  # 纵轴颠倒

    # 设置清晰的纵轴刻度
    plt.gca().yaxis.set_major_locator(LogLocator(base=10.0, numticks=15))
    plt.gca().yaxis.set_major_formatter(LogFormatter(base=10.0, labelOnlyBase=True))

    plt.title("Total KTD over Time")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig("charts/total_ktd_chart_log.png")  # 文件名强调对数
    plt.close()

    if generate_individual_key_charts:
        # 生成每个键的折线图
        for key, ktd in keys_ktd.items():
            plt.figure(figsize=(10, 5))
            plt.plot(list(ktd.keys()), list(ktd.values()), label=f"Key {key} KTD")
            plt.xlabel("Time (s)")
            plt.ylabel("KTD (ms)")  # 添加单位 ms
            plt.yscale("log")  # 设置纵轴为对数尺度
            plt.gca().invert_yaxis()  # 纵轴颠倒

            # 设置清晰的纵轴刻度
            plt.gca().yaxis.set_major_locator(LogLocator(base=10.0, numticks=15))
            plt.gca().yaxis.set_major_formatter(
                LogFormatter(base=10.0, labelOnlyBase=True)
            )

            plt.title(f"Key {key} KTD over Time")
            plt.legend()
            plt.grid(True, which="both", ls="--")
            plt.savefig(f"charts/key_{key}_ktd_chart_log.png")  # 文件名强调对数
            plt.close()

    if generate_individual_adjacent_keys_charts:
        # 生成相邻两轨的折线图
        for key_pair, ktd in adjacent_keys_ktd.items():
            plt.figure(figsize=(10, 5))
            plt.plot(list(ktd.keys()), list(ktd.values()), label=f"Keys {key_pair} KTD")
            plt.xlabel("Time (s)")
            plt.ylabel("KTD (ms)")  # 添加单位 ms
            plt.yscale("log")  # 设置纵轴为对数尺度
            plt.gca().invert_yaxis()  # 纵轴颠倒

            # 设置清晰的纵轴刻度
            plt.gca().yaxis.set_major_locator(LogLocator(base=10.0, numticks=15))
            plt.gca().yaxis.set_major_formatter(
                LogFormatter(base=10.0, labelOnlyBase=True)
            )

            plt.title(f"Keys {key_pair} KTD over Time")
            plt.legend()
            plt.grid(True, which="both", ls="--")
            plt.savefig(f"charts/keys_{key_pair}_ktd_chart_log.png")  # 文件名强调对数
            plt.close()

    # 生成每个键和相邻两轨的折线图在一张图里
    # adjacent_keys 都红色调 1+2 2+3 3+4
    # keys 都蓝色调 1 2 3 4
    plt.figure(figsize=(10, 5))
    for key, ktd in keys_ktd.items():
        plt.plot(
            list(ktd.keys()), list(ktd.values()), label=f"Key {key} KTD", color="blue"
        )
    for key_pair, ktd in adjacent_keys_ktd.items():
        plt.plot(
            list(ktd.keys()),
            list(ktd.values()),
            label=f"Keys {key_pair} KTD",
            color="red",
        )
    plt.xlabel("Time (s)")
    plt.ylabel("KTD (ms)")  # 添加单位 ms
    plt.yscale("log")  # 设置纵轴为对数尺度
    plt.gca().invert_yaxis()  # 纵轴颠倒

    # 设置清晰的纵轴刻度
    plt.gca().yaxis.set_major_locator(LogLocator(base=10.0, numticks=15))
    plt.gca().yaxis.set_major_formatter(LogFormatter(base=10.0, labelOnlyBase=True))

    plt.title("Keys and Adjacent Keys KTD over Time")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig("charts/keys_and_adjacent_keys_ktd_chart_log.png")  # 文件名强调对数
    plt.close()
