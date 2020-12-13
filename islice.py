# @Author: JogFeelingVi
# @Date: 2020-12-13 16:23:08
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2020-12-13 16:23:08
import itertools


def nouadd(number: int) -> int:
    while number <= 1000:
        yield number
        number = number + 1


if __name__ == '__main__':
    nadd = nouadd(5)
    # islice(xxx, start stop, step)
    # for x in itertools.islice(nadd, 50, 60):
    #     print(x)
    rsplit = (itertools.islice(nadd, 10) for x in range(0, 100, 10))
    for x in rsplit:
        print(list(x))