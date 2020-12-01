# @Author: JogFeelingVi
# @Date: 2020-11-24 10:13:34
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2020-11-24 10:13:34
from typing import List, Literal, Union
from enum import Enum


class keys(Enum):
    dx = ['d', 'x']
    jo = ['j', 'o']


class t_key:
    name: str = ''
    value: Union[str, int] = ''

    def __init__(self, name: str, value: Union[str, int]) -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f'Nmae: {self.name} Value {self.value}'

    def __repr__(self) -> str:
        return f'N {self.name} V {self.value}'

    def __format__(self, format_spec: Literal['v', 's', 'r', 'vs']) -> str:
        print(f'This run __format__ spec{format_spec}')
        vsco = {
            's': lambda: self.__str__(),
            'r': lambda: self.__repr__(),
            'v': lambda: f'arges -v {self.name} is value {self.value}',
            'vs': lambda: f'{self.name} is value {self.value}',
        }
        return vsco.get(format_spec, 'error')()


def formk(key: t_key):
    print(f'type {key:vs}')


def test() -> None:
    formk(t_key('dx', 'd'), )


if __name__ == '__main__':
    test()