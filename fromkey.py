# @Author: JogFeelingVi
# @Date: 2020-11-24 10:13:34
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2020-11-24 10:13:34
from typing import List, Literal, Union
from enum import Enum


def look(m, *args: Union[int, float]) -> None:
    if (Ln := args.__len__()) <=3:
        print(f'Message {m} {sum(args)}')
    else:
        print(f'Error max Lan 3 Lan {Ln}')

def pimer(N:int) -> None:
    if N > 1:
        for n in range(2, N):
            if N % n == 0:
                print(f'{N} is not P')
                print(f'{n} times {N//n} is {N}')
                break
            else:
                print(f'{13} is P')
    else:
        print(f'N > 1 min N is 2')


def Tests() -> None:
    look(5, 6, 7)
    pimer(3)


if __name__ == '__main__':
    Tests()