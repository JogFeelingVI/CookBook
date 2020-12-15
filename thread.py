# @Author: JogFeelingVi
# @Date: 2020-12-11 08:04:46
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2020-12-11 08:04:46
import time, sys
from timeit import Timer
from threading import Thread, Event
from typing import Any, Literal, Union


class outs:
    ''' sys.stdout '''
    def __init__(self) -> None:
        self._stw = sys.stdout

    def write(self, code: Any, flush: bool = True) -> None:
        self._stw.write(code)
        if flush is True:
            self._stw.flush()

    def move(self, n: int, efc: Literal['u', 'd', 'l', 'r']) -> None:
        efcd = {
            'u': '\x1b[{n}A',
            'd': '\x1b[{n}B',
            'r': '\x1b[{n}C',
            'l': '\x1b[{n}D',
        }
        self.write(efcd.get(efc, '\x1b[{n}A').format(n=n), False)

    def wrap(self) -> None:
        self.write('\n')


class progress:
    ''' show progress bar '''
    _title: str = 'progress'
    _length: int = 60
    E: str = ' '
    F: str = '-'
    S: outs = outs()

    def __init__(self,
                 max: Union[float, int],
                 title: str = 'progress',
                 length: int = 60) -> None:
        self._max = max
        self._title = title
        self._length = 60

    @property
    def length(self) -> int:
        return self._length

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    def value(self, val: Union[float, int]) -> None:
        bx: float = val / self._max + 0.01
        pv: int = int(bx * self._length)
        bar = f'{self.title}: [{self.F*pv}{(self._length-pv)*self.E}] {bx:>4.0%}'
        self.S.move(bar.__len__(), 'l')
        self.S.write(bar)


class Tasks:
    def __init__(self, even: Event) -> None:
        self._run = True
        self._out = outs()
        self._eve = even

    def close(self) -> None:
        self._run = False

    def countdown(self, ns: int) -> None:
        self._out.write('countdown start\n')
        self._eve.set()
        addx: int = 0
        for i in range(0, ns):
            if self._run:
                addx = addx + i
                self._out.move(25, 'l')
                # T-times -> 100 4950  99
                self._out.write(f'T-times -> {ns:>3} {addx:>5} {i:>3}')
                time.sleep(0.1)
            else:
                self._out.wrap()
                self._out.write(f'{self._run} close task')
                break
        self._out.write('\ncountdown over\n')


def T_work() -> None:
    E = Event()
    C = Tasks(E)
    P = progress(100)
    #T = Thread(target=C.countdown, args=(100, ))
    #T.start()
    for x in range(0, 100):
        P.value(x)
        time.sleep(0.1)


if __name__ == '__main__':
    t = Timer('T_work()', 'from __main__ import T_work')
    print(t.repeat(repeat=1, number=1))