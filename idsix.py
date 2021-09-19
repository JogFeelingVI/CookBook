# @Author: JogFeelingVi
# @Date: 2021-09-19 22:38:39
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-09-19 22:38:39
import csv, pathlib
from functools import partial


class idx:
    '''
    name, idsix [\d]{6}
    '''
    __data = None
    __debug = False

    def __init__(self) -> None:
        self.__data = self._load_data()

    def look_date(self):
        for n, idx in self.__data:
            print(f'Data: Na {n}, Idx {idx}')
    
    def debug(self):
        self.__debug = True

    def find(self, idx: int = 661400, l: int = 0, r: int = 0):
        '''
        idx = 4 m = 6
        1,2,3,4,5,6,7,8,9,10,11,12
        '''
        r = len(self.__data) if r == 0 else r
        m = (l + r) // 2
        na, idsix = self.__data[m]

        if self.__debug:
            print(f'Debug: L {l}, R {r}, M {m}, Na {na}, ID {idsix}')

        if idsix == idx:
            return na
        if abs(r - l) == 1:
            return 'NoFind'
        elif idx < idsix:
            return self.find(idx, l, m)
        elif idx > idsix:
            return self.find(idx, m, r)

    @staticmethod
    def _load_data():
        '''
        load csv file
        '''
        p = pathlib.PosixPath('./IDSIX.csv')
        if p.exists() == False:
            return None
        else:
            with p.open(mode='r', encoding='utf-8') as pd:
                csvr = csv.reader(pd, ('name', 'idsix'))
                tmp = [[na, int(idx)] for na, idx in csvr]
                return sorted(tmp, key=lambda x: x[1])
                #return tmp


if __name__ == '__main__':
    ix = idx()
    print(ix.find(661400))