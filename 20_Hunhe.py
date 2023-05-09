# @Author: JogFeelingVi
# @Date: 2023-03-01 15:32:07
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2023-03-01 15:32:07

import random as rDx
from enum import Enum
from typing import List


class way(Enum):
    keys = [
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        5,
        6,
        7,
    ]
    Jieguo = [
        22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        40
    ]

    def toV(self):
        return self.value


class ftp(Enum):
    Lens = lambda x: set(x).__len__() == 3
    Ngolc = lambda x: sum([[0, 1][x >= 10] for x in x]) >= 2

    def __call__(self, T) -> bool:
        return self.value()(T)


class simu:
    def __init__(self) -> None:
        self.original: List[int] = way.keys.toV()
        self.suanshi = dict.fromkeys([x for x in range(1, 21)], '-')
        self.filt_T = [ftp.Lens, ftp.Ngolc]

    def raw_date(self) -> List[int]:
        while True:
            tmp = rDx.choices(self.original, k=3)
            ftx = [x(tmp) for x in self.filt_T]
            if False not in ftx:
                return tmp

    def reindex(self) -> int:
        xin = 0
        for k, v in self.suanshi.items():
            if v == '-':
                xin = k
                break
        return xin

    def buildup(self) -> None:
        def addsub(a, b, c) -> None:
            if a + b >= c:
                hes = f'{a:>2} + {b:>2} - {c:>2}'
                rx: bool = [False, True][eval(hes) in way.Jieguo.toV()]
                if rx:
                    self.suanshi.update({self.reindex(): hes})

        def subadd(a, b, c) -> None:
            if a - b >= 0:
                hes = f'{a:>2} - {b:>2} + {c:>2}'
                rx = [False, True][eval(hes) in way.Jieguo.toV()]
                if rx:
                    self.suanshi.update({self.reindex(): hes})

        def add2(a, b, c) -> None:
            hes = f'{a:>2} + {b:>2} + {c:>2}'
            rx = [False, True][eval(hes) in way.Jieguo.toV()]
            if rx:
                self.suanshi.update({self.reindex(): hes})

        def sub2(a, b, c) -> None:
            x = sorted([a, b, c], reverse=True)
            a, b, c = x
            hes = f'{a:>2} - {b:>2} - {c:>2}'
            rx = [False, True][eval(hes) in way.keys.toV()[2:11]]
            if rx:
                self.suanshi.update({self.reindex(): hes})

        while True:
            a, b, c = self.raw_date()
            switch = rDx.choice([0, 1, 2, 3])
            # TODO 选择工作模式
            if switch == 0:
                addsub(a, b, c)
            elif switch == 1:
                subadd(a, b, c)
            elif switch == 2:
                add2(a, b, c)
            elif switch == 3:
                sub2(a, b, c)
            if self.reindex() == 0:
                break

    def moni_sub(self):
        self.buildup()
        spc = ' ' * 4
        glos = []
        step = 4
        temp = [x for x in self.suanshi.items()]
        lent = self.suanshi.__len__()
        for i in range(0, lent, step):
            es = i + step
            ts = temp[i:es]
            strs = [f'{i:>2}: {x}' for i, x in ts]
            if len(ts) == step and es < lent:
                glos.extend(['    '.join(strs)+ '\n'])
            else:
                glos.extend(['    '.join(strs)])
        for x in glos:
            print(''.join(x))


if __name__ == '__main__':
    lx = simu()
    lx.moni_sub()