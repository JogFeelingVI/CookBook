# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-12-22 21:24:40
# @Last Modified by:   Your name
# @Last Modified time: 2023-12-22 21:57:47
import math, random


def computing(a: float, cos: float) -> float:
    '''call C len'''
    C = cos * math.pi / 180
    return math.sqrt(a**2 + a**2 - 2 * a * a * math.cos(C))


def cutting(quantities: int) -> float:
    '''quantities / 360'''
    return 360 / quantities


def comput(index: int, max=100000):
    lenx = []
    a = random.uniform(3, 10)
    for x in range(6, max):
        cos = cutting(x)
        len = computing(a, cos) * x
        lenx.append(len / (a + a))
    return sum(lenx[-5:]) / 5


def main():
    print(f"Hello, World! {computing(3.5,30.1)}")
    rx = comput(1)
    print(f'cutting {rx}')


if __name__ == "__main__":
    main()
