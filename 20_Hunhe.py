# @Author: JogFeelingVi
# @Date: 2023-03-01 15:32:07
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2023-03-01 15:32:07

import random as rDx
from enum import Enum
from typing import List


class way(Enum):
    keys = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,5,6,7,]
    Jieguo = [22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]

    def toV(self):
        return self.value


class ftp(Enum):
    Lens = lambda x: set(x).__len__() == 3
    Ngolc = lambda x: sum([[0, 1][x >= 15] for x in x]) == 1

    def __call__(self, T) -> bool:
        return self.value()(T)


class simu:
    def __init__(self) -> None:
        self.original: List[int] = way.keys.toV()
        self.suanshi = dict.fromkeys(way.keys.toV(), '-')
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
                hes = f'{a} + {b} - {c}'
                rx: bool = [False, True][eval(hes) in way.Jieguo.toV()]
                if rx:
                    self.suanshi.update({self.reindex(): hes})

        def subadd(a, b, c) -> None:
            if a - b >= 0:
                hes = f'{a} - {b} + {c}'
                rx = [False, True][eval(hes) in way.Jieguo.toV()]
                if rx:
                    self.suanshi.update({self.reindex(): hes})

        def add2(a, b, c) -> None:
            hes = f'{a} + {b} + {c}'
            rx = [False, True][eval(hes) in way.Jieguo.toV()]
            if rx:
                self.suanshi.update({self.reindex(): hes})

        def sub2(a, b, c) -> None:
            x = sorted([a, b, c], reverse=True)
            a, b, c = x
            hes = f'{a} - {b} - {c}'
            rx = [False, True][eval(hes) in way.keys.toV()[2:11]]
            if rx:
                self.suanshi.update({self.reindex(): hes})

        while True:
            a, b, c = self.raw_date()
            switch = rDx.choice([0, 1])
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
        spc = ' '*4
        for i, x in self.suanshi.items():
            print(f'{x}{spc} ', end='')


if __name__ == '__main__':
    lx = simu()
    lx.moni_sub()