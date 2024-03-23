# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-03-23 14:13:58
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-03-23 14:49:33
import dataclasses
import asyncio, random, time, csv
from typing import List

csv_path = 'dataFream.csv'

@dataclasses.dataclass
class crow:
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

def Load_csv(filename: str = csv_path) -> List[crow]:
    '''Load_csv('ShuDou - dataFream csv') '''
    temp = []
    with open(filename) as read:
        _csvf = csv.reader(read)
        for row in _csvf:
            temp.append(crow(*row))
    return temp

def main():
    print("Hello, World!")
    Load_csv()


if __name__ == "__main__":
    main()