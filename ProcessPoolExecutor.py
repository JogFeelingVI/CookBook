# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-03-27 10:26:32
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-03-27 15:13:55

from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager
from time import sleep
from typing import Any

values = [3, 4, 5, 6, 9, 10]


def cube(x,):
    return x * x * x * 3.14


def cubex(x,):
    return x * 3 * 3.14


def done(future):
    print(f'Done. {future.result() =}')


def main():
    print("Hello, World!")
    result = []
    with ProcessPoolExecutor(max_workers=5) as exe:
        futel = exe.submit(cubex, 2)
        # Maps the method 'cube' with a iterable
        result = exe.map(cube, values)
        futel.add_done_callback(done)
    for r in result:
        print(r)

# 共享数据版本

def cubem(x, ser):
    n = x * x * x * 3.14
    ser.put(n)
    return n


def cubemx(ser):
    while 1:
        print(f'{ser.empty() = }')
        sleep(3)
        if ser.empty():
            break
        else:
            n = ser.get()
            print(f'write {n = }')


def donem(future):
    print(f'Done. {future.result() =}')

def mainx():
    print("Hello, World!")
    futel = []
    with Manager() as mdict:
        share = mdict.Queue()
        with ProcessPoolExecutor(max_workers=5) as exe:
            
            futel.append(exe.submit(cubemx, share).add_done_callback(donem))
            futel = [
                exe.submit(cubem, i, share).add_done_callback(donem) for i in range(25)
            ]
        


if __name__ == "__main__":
    mainx()
