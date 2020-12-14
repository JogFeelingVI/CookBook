# @Author: JogFeelingVi
# @Date: 2020-12-09 17:09:00
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2020-12-09 17:09:00
from itertools import combinations, islice
from typing import Generator, Iterable, Iterator


def combin(count: int = 6) -> Iterable:
    """[summary]

    Args:
        count (int, optional): [description]. Defaults to 6.

    Returns:
        Iterable: [description]
    """    ''' '''
    nl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
          20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33)
    tp: Iterator = combinations(nl, count)
    ls: Iterator = (islice(tp, 1000) for x in range(0, 1107568, 1000))
    #ls = (x for x in islice(tp, 0, 1107568, 1000))
    return ls


if __name__ == '__main__':
    cx = combin(6)
    vix = 0
    for x in cx:
        for c in x:
            print(f'index {vix:>7} {c}')
            vix +=1
            #  10  45   9
