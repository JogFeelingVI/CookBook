# @Author: JogFeelingVi
# @Date: 2020-12-15 07:57:38
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2020-12-15 07:57:38
from threading import Thread
from timeit import Timer

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
    vx = [x for x in range(1000) if x % 3 == 1 and x % 4 == 3]


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


def show_repeat(funame: str, repeat:float) -> None:
    print(f'    {funame} -> {repeat:4.6f}')


if __name__ == '__main__':
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
