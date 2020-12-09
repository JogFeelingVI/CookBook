# @Author: JogFeelingVi
# @Date: 2020-12-07 11:10:56
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2020-12-07 11:10:56

import sys, time
from typing import Literal, Optional

Black = 30
Red = 31
Green = 32
Yellow = 33
Blue = 34
Magenta = 35
Cyan = 36
White = 37
Reset = 0
Bg_Black = 40
Bg_Red = 41
Bg_Green = 42
Bg_Yellow = 43
Bg_Blue = 44
Bg_Magenta = 45
Bg_Cyan = 46
Bg_White = 47

Terminal = 0
Bold = 1
Underline = 4
Blinking = 5
Reversed = 7
Invisible = 8


Up = '\x1b[{n}A'
Down = '\x1b[{n}B'
Right = '\x1b[{n}C'
Left = '\x1b[{n}D'


def echo(msg: str) -> None:
    sys.stdout.write(msg)


def color_code(mt: int = None,
               fc: int = None,
               bg: int = None,
               msg: str = 'None') -> str:
    ''' \033[显示方式;前景色;背景色m '''
    fmat = '\033[{code}{msg}\033[0m'
    switch = {
          0: '',
          1: '{}m',
          2: '{};{}m',
          3: '{};{};{}m'
    }
    code = [x for x in [mt, fc, bg] if x != None and x != 0]
    code_len = code.__len__()
    code_f = switch.get(code_len).format(*code)
    msg = f'{msg}'
    return fmat.format(code=code_f, msg=msg)


def full_color() -> None:
    ''' print full color '''
    for m in range(0, 10):
        for f in range(30, 37):
            for b in range(40, 48):
                code = f' {m};{f};{b} '
                echo(color_code(mt=m, fc=f, bg=b, msg=code))
            echo('\n')
        echo('\n')
    echo('\n')


def loads():
    msg = color_code(bg=32, msg='loading...')
    echo(msg=msg)
    for x in range(0, 100):
        _st = f'{x+1}%'
        time.sleep(0.1)
        sys.stdout.write(Left.format(n=_st.__len__()))
        sys.stdout.flush()
        #time.sleep(1)
        code = color_code(msg=_st, fc=Red)
        sys.stdout.write(code)
        sys.stdout.flush()


if __name__ == '__main__':  
    full_color()
    #loads()
