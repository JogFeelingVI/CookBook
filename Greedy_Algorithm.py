# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-05-13 08:58:09
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-05-13 09:30:11

from collections import defaultdict
from dataclasses import dataclass


@dataclass
class item:
    name: str
    zhongliang: int
    danjia: int
    zongjia: int = 0

    def __init__(self, name: str, zl: int, dj: int):
        self.name = name
        self.zhongliang = zl
        self.danjia = dj
        self.zongjia = zl * dj
        
    def midu(self):
        return self.zhongliang / self.zongjia


def make_change(coins, amount):
    """
    找零钱的贪婪算法

    Args:
        coins: 可用硬币的面值列表（降序排列）
        amount: 目标金额

    Returns:
        用于找零的硬币数量，如果无法找零则返回 -1
    """
    coin_count = dict().fromkeys(coins, 0)
    remaining_amount = amount

    for coin in coins:
        while remaining_amount >= coin:
            remaining_amount -= coin
            coin_count[coin] += 1

    return coin_count


def fractional_knapsack(capacity, items):
    """
    分数背包问题的贪婪算法

    Args:
        capacity: 背包容量
        items: 物品列表，每个物品包含重量和价值

    Returns:
        背包的最大价值
    """
    items.sort(key=lambda x: x.midu() , reverse=True)  # 按价值密度排序
    print(f'{items=}')
    total_value = 0
    remaining_capacity = capacity

    for it in items:
        weight, value = it.zhongliang, it.zongjia
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            total_value += fraction * value
            break

    return total_value


def main():
    print("Hello, World!")
    money = [100, 50, 20, 10, 5, 1]
    tcoin = 536
    piands = make_change(money, 600 - tcoin)
    print(f"{piands=}")
    # //
    # 示例
    items_box = [
        item("shuiguo", 20, 5),
        item("kuaiquanshui", 5, 2),
        item("shizhijing", 2, 5),
        item("powback", 2, 1),
        item('phone',25,50000)
    ]
    # items = [(10, 60), (20, 100), (30, 120)]  # 物品重量和价值
    capacity = 50  # 背包容量
    max_value = fractional_knapsack(capacity, items_box)
    print(f"背包最大价值: {max_value}")


if __name__ == "__main__":
    main()
