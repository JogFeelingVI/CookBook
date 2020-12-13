# @Author: JogFeelingVi
# @Date: 2020-12-11 08:04:46
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2020-12-11 08:04:46
import time, sys
from threading import Thread, Event
from typing import Any, Literal


class outs:
    ''' sys.stdout '''
    def __init__(self) -> None:
        self._stw = sys.stdout

    def write(self, code: Any, flush:bool = True) -> None:
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


class Tasks:
    def __init__(self, even:Event) -> None:
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
                self._out.move(22, 'l')
                #T-times ->  10  45   9
                self._out.write(f'T-times -> {ns:>3} {addx:>3} {i:>3}')
                time.sleep(0.1)
            else:
                print(f'{self._run} close task')
                break
        self._out.write('\ncountdown over\n')


def T_work() -> None:
    E = Event()
    C = Tasks(E)
    T = Thread(target=C.countdown, args=(10, ))
    T.start()
    while (T.is_alive()):
        time.sleep(0.1)
        #cT.close()
    print('T is Over')


if __name__ == '__main__':
    T_work()