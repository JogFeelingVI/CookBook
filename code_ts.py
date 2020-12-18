# @Author: JogFeelingVi
# @Date: 2020-12-15 07:57:38
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2020-12-15 07:57:38
from threading import Thread
from timeit import Timer, timeit
from itertools import islice

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

class tsp2:
    def __init__(self) -> None:
        self.map = {}
    
    def p_map(self, Qc=[4,5,6]) -> dict:
        for c in Qc:
            self.fx(c)
        return self.map

    def fx(self, c:int) -> None:
        self.map[c] = [x for x in range(c, c * 100, c)]

def Nadd(min:int, max:int, sz: int = 10) -> list:
    while min <= max:
        yield [x for x in range(min, min + sz) if x <= max]
        min += sz

def Nadd2(min: int, max:int) -> int:
    while min <= max:
        yield min
        min += 1


def code_ts1() -> None:
    def p1():
        for x in Nadd(4,32):
            print(x)

    def p2():
        ml = (list(islice(Nadd(4, 32), 10)) for x in range(4, 32, 10))
        for x in ml:
            print(x)
        
    t1 = timeit(p1, number=10)
    print(f'T1 {t1}')
    t2 = timeit(p2, number=10)
    print(f'T2 {t2}')


if __name__ == '__main__':
    code_ts1()
