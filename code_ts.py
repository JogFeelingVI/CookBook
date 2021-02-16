# @Author: JogFeelingVi
# @Date: 2020-12-15 07:57:38
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2020-12-15 07:57:38
from threading import Thread
from timeit import Timer, timeit
from itertools import islice, combinations
from typing import Counter, Iterable, List
import os

# https://juejin.cn/post/6844903574774759437
# https://codertw.com/程式語言/693491/


class T_class(Thread):
    ''' Thread [ RUN ] '''
    def run(self):
        func_test()


class F_class:
    ''' NO Thread [ RUN ] '''
    def run(self):
        func_test()


def func_test() -> None:
    ''' Test Code the here '''


def y_threaded(count: int = 1) -> None:
    ''' Yes  Thread '''
    func: list = [T_class() for x in range(count)]
    for st in func:
        st.start()
    for jo in func:
        jo.join()


def n_threaded(count: int = 1) -> None:
    ''' No  Thread '''
    func: list = [F_class() for x in range(count)]
    for ru in func:
        ru.run()


def show_repeat(funame: str, repeat: float) -> None:
    print(f'    {funame} -> {repeat:4.6f}')


def code() -> None:
    repeat: int = 100
    number: int = 1
    counts: list = [1, 2, 4, 8]
    print(f'START TEST')
    for c in counts:
        n_t = Timer(f'n_threaded({c})', 'from __main__ import n_threaded')
        n_repeat = min(n_t.repeat(repeat=repeat, number=number))
        show_repeat(f'n_threaded {c}', n_repeat)
        y_t = Timer(f'y_threaded({c})', 'from __main__ import y_threaded')
        y_repeat = min(y_t.repeat(repeat=repeat, number=number))
        show_repeat(f'y_threaded {c}', y_repeat)
        print(f'Test {c} ---')


def old_list():
    """ 新方法效率提高不少 """
    _sz = 1000
    nl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
          20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33)
    Lp = combinations(nl, 6)
    return (list(islice(Lp, _sz)) for x in range(0, 1107568, _sz))


def new_list():
    cb = yieldcombin()
    lp = cb.readpage()
    return lp


def code_ts2() -> None:
    t1 = timeit('old_list()', 'from __main__ import old_list', number=10000)
    print(f'old_list {t1}')
    t2 = timeit('new_list()', 'from __main__ import new_list', number=10000)
    print(f'new_list {t2}')


class yieldcombin:
    min, max = 0, 1107568
    nl = 0

    def __init__(self) -> None:
        self.combin_list = self.__combin()
        self.cpuc = os.cpu_count()
        self.psize = self.max // self.cpuc + 1

    def seting_psize(self, sz: int = 1000):
        self.psize = sz

    def __combin(self) -> Iterable:
        '''
            [1, 2, 3, 4, 5, 6]...
        '''
        nl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
              19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33)
        return combinations(nl, 6)

    def readpage(self) -> list:
        while self.min <= self.max:
            yield islice(self.combin_list, self.psize)
            self.min += self.psize

    def fibonacci(n: int) -> List[int]:
        a, b, counter = 0, 1, 0
        while True:
            if counter > n:
                return
            yield a
            a, b = b, a + b
            counter += 1


if __name__ == '__main__':
    # code_ts2()
    code_ts2()
    
