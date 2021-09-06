# @Author: JogFeelingVi
# @Date: 2021-06-13 16:44:35
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-06-13 16:44:35
import time
from typing import Union


class pertest:
    def __init__(self, funx:callable) -> None:
        self.funx = funx

    def Tx(self):
        start = time.perf_counter()
        self.funx()
        done = time.perf_counter()
        sdon = done - start
        print(f'{sdon * 10**6} ms')


def code():
    xlis = [x for x in range(1000)]
    xlis.sort()

if __name__ == '__main__':
    pts = pertest(code)
    pts.Tx()