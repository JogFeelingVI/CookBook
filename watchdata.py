# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-03-23 14:13:58
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-04-05 11:34:49
import dataclasses, pathlib
import asyncio, random, time, csv
from typing import List

csv_path = pathlib.Path('dataFream.csv')

@dataclasses.dataclass
class row:
    qiaho: str
    r: str
    b: str
    fgz: str
    lrw: str
    glc: str
    dzx: str
    mod3: str
    dx: str
    jo: str
    zh: str

def Load_csv_to_rows(filename: pathlib.Path = csv_path) -> List[row]:
    '''Load_csv('ShuDou - dataFream csv') '''
    temp = []
    if filename.exists() != True:
        return temp
    with filename.open(mode='r') as read:
        _csvf = csv.reader(read)
        for _r in _csvf:
            temp.append(row(*_r))
    return temp

class OutputManager:
    def __init__(self, rows: List[row]):
        if rows != []:
            if isinstance(rows[0], row):
                self.rows: List[row] = rows

    def out(self, name: str, operation:str=''):
        values = [getattr(_c, name) for _c in self.rows]  # 获取指定属性的值列表
            
        match operation:
            case 'str':
                result = values
            case 'int':
                result = [self.convert_to_numeric(x) for x in values]
            case _:
                result = values
        
        return result
    
    def convert_to_numeric(self, _v:str):
        match _v:
            case str() as v if ',' in v:
                return [int(x) for x in v.split(',')]
            case str() as v if ':' in v:
                return [int(x) for x in v.split(':')]
            case str() as v:
                return [int(v)]


def main():
    print("Hello, World!")
    rows = Load_csv_to_rows()
    outManager = OutputManager(rows)
    cols = outManager.out(name='r', operation='int')
    sums = [sum(x) for x in cols]
    print(f'{max(sums)=} {min(sums)=}')
    for _c in sums[-20::]:
        print(f' {_c =}')
    


if __name__ == "__main__":
    main()