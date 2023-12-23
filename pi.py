# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-12-22 21:24:40
# @Last Modified by:   Your name
# @Last Modified time: 2023-12-23 19:46:19
from collections import deque
import math, random, dataclasses

class FixedSizeQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = deque(maxlen=maxsize)

    def put(self, item):
        self.queue.append(item)

    def get(self):
        return self.queue.popleft()

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)
    
    def average(self):
        if len(self.queue) == 0:
            return 0
        else:
            return sum(self.queue) / len(self.queue)

@dataclasses.dataclass
class deyao:
    bianchang: float
    cos: float


def computing(a: float, cos: float) -> float:
    '''call C len'''
    C = cos * math.pi / 180
    return math.sqrt(a**2 + a**2 - 2 * a * a * math.cos(C))


def cutting(quantities: int) -> float:
    '''quantities / 360'''
    return 360 / quantities



def comput(index: int, max=10000000):
    lenx = FixedSizeQueue(5)
    banjin = random.uniform(3, 20)
    for x in range(6, max):
        dens = deyao(banjin, cutting(x))
        print(f'deyao {dens}')
        cos = cutting(x)
        len = computing(dens.bianchang, cos) * x
        lenx.put(len / (dens.bianchang * 2))
    return lenx.average()


def main():
    print(f"Hello, World! {computing(3.5,30.1)}")
    rx = comput(1)
    print(f'cutting {rx}')


if __name__ == "__main__":
    main()
