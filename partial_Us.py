# @Author: JogFeelingVi
# @Date: 2021-09-17 21:45:23
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-09-17 21:45:23
from functools import partial
from itertools import count, repeat, product


def add(*n: int, isz=True) -> int:
    print(f'Debug: {", ".join(map(str, n))}')
    return sum(n)

def products():
    d = [1, 3, 4, 6, 7, 9, 0]
    prs = product(d, repeat=3)
    zip_item = zip(count(), prs)
    for zi in zip_item:
        i, p = zi
        print(f'{i},{i/342*100:.2f}%: {p}')


def main():
    print(add(1, 2, 3))
    func = partial(add, 100)
    print(func(1, 2, 3))
    products()


if __name__ == '__main__':
    main()