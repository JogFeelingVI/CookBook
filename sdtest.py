# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-10-01 07:34:51
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-10-07 21:37:18

from asyncio import SafeChildWatcher
from cProfile import label
import csv
from math import exp
from typing import List


class Candidate_database:
    '''待选数据库'''
    def __init__(self, row: int, col: int) -> None:
        self.row = row if 0 <= row < 9 else 0
        self.col = col if 0 <= col < 9 else 0
        self.nums = []
        self.ID = f'R{self.row+1}C{self.col+1}'
        self.exp = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.__diff_set = None

    def setNums(self) -> set[int]:
        return set(self.nums)

    def addnum(self, V: int) -> None:
        '''向 nums 添加数据'''
        if 1 <= V <= 9:
            self.nums.append(V)

    def get_rcv(self) -> List[int]:
        return [self.row, self.col, list(self.Candidate())[0]]

    def addnums(self, V: List[int]) -> None:
        self.nums.extend(V)

    def Candidate(self, force: bool = False) -> set[int]:
        '''待选数字'''
        if self.__diff_set == None or force == True:
            self.__diff_set = self.exp - self.setNums()
        return self.__diff_set

    def SetCandidate(self, value: set):
        self.nums = [x for x in self.exp if x not in value]
        self.Candidate(force=True)

    def __len__(self) -> int:
        return len(self.Candidate())

    def __str__(self) -> str:
        Candidate = ', '.join(map(str, self.Candidate()))
        return f'R{self.row+1}C{self.col+1} Candidate {{{Candidate}}}'


class ListCD:
    ''' Candidate_database 管理类 '''
    __rows: List[Candidate_database] = []

    def add(self, item: Candidate_database) -> None:
        '''add 添加数据 并返回索引'''
        self.__rows.append(item)

    @property
    def itemLen(self) -> int:
        return self.__rows.__len__()

    def filters(self, funcx) -> List[Candidate_database]:
        self.temp = [r for r in self.__rows if funcx(r)]
        return self.temp

    def getid(self, r: int, c: int) -> Candidate_database | None:
        '''where is row and col'''
        for cd in self.__rows:
            if cd.ID == f'R{r+1}C{c+1}':
                return cd
        return None

    def echo(self, T: str = 'Test') -> None:
        '''
        T Title
        '''
        if self.temp != None:
            for r in self.temp:
                print(f'{T}: {r}')


class board:
    '''数独 数字结构'''
    def __init__(self, checksize: int = 9) -> None:
        '''checksize 格子大小 最小为 9'''
        self.check = checksize if checksize in [9] else 9
        self.__array = [[0 for _ in range(self.check)]
                        for _ in range(self.check)]

    @property
    def Array(self) -> list:
        return self.__array

    def loadcsv(self) -> None:
        '''装载CSV文件'''
        with open('ShuDou - IQ139.csv') as read:
            _csvf = csv.reader(read)
            for index, row in enumerate(_csvf):
                for col, value in enumerate(row):
                    if value != '':
                        self.set(index, col, int(value))

    def set(self, row: int, col: int, value: int) -> None:
        ''' 设置坐标的数值 '''
        if self.__check_set_args(row, col, value):
            self.__array[row][col] = value
        else:
            raise IndexError(f'Row & Col Error POS {row},{col},{value}')

    def get(self, row: int, col: int) -> int:
        '''获取坐标的数值'''
        if self.__check_set_args(row, col, 9):
            return self.__array[row][col]
        else:
            raise IndexError(f'Row & Col Error POS {row},{col}')

    def __check_set_args(self, r: int, c: int, v: int) -> bool:
        ''' 检查 fun set 参数是否合理 '''
        rec = []
        rec.append([False, True][0 <= v <= self.check])
        rec.append([False, True][0 <= r < self.check])
        rec.append([False, True][0 <= c < self.check])
        return [False, True][False not in rec]

    def echo(self):
        '''显示 self.__array'''
        # for r in self.__array:
        #     col = ''.join([f'[{c}]' for c in r])
        #     print(f'{col}')
        for r in range(self.check):
            if r % 3 == 0 and r != 0:
                print('-' * (self.check + 2) * 2)
            for c in range(self.check):
                if c % 3 == 0 and c != 0:
                    print('| ', end='')
                if c == self.check - 1:
                    print(f'{self.get(r,c)}')
                else:
                    print(f'{self.get(r,c)} ', end='')


class shuduku:
    '''
    解算数独
    '''
    def __init__(self, Board: board) -> None:
        ''' 解算数独的运算单位 '''
        self.Boar = Board

    def find_zero(self) -> tuple[int, int] | None:
        '''查找需要填写数字的坐标'''
        for r in range(self.Boar.check):
            for c in range(self.Boar.check):
                if self.Boar.Array[r][c] == 0:
                    return (r, c)  # row, col
        return None

    def solve(self) -> bool:
        '''解题核心'''
        find = self.find_zero()
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, self.Boar.check + 1):
            if self.valid(num, row, col):
                self.Boar.set(row, col, num)
                if self.solve():
                    return True
                self.Boar.set(row, col, 0)
        return False

    def valid(self, num: int, row: int, col: int) -> bool:
        '''验证所填数字是否符合规范'''
        # Check row
        for field in range(self.Boar.check):
            if self.Boar.get(row, field) == num and col != field:
                return False

        # Check column
        for line in range(self.Boar.check):
            if self.Boar.get(line, col) == num and row != line:
                return False
        # Check box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.Boar.get(i, j) == num and (i, j) != (row, col):
                    return False
        return True


class difficulty:
    '''评级题目的难度'''
    def __init__(self, Board: board) -> None:
        self.Boar = Board
        self.ListCD = ListCD()
        self.__zero()

    def FixBoard(self) -> None:
        ''' Fix Board for one '''
        Funx = lambda x: x.__len__() == 1
        Fixs = self.ListCD.filters(Funx)
        for F in Fixs:
            r, c, v = F.get_rcv()
            self.Boar.set(r, c, v)

    def __zero(self) -> None:
        for r in range(self.Boar.check):
            for c in range(self.Boar.check):
                if self.Boar.Array[r][c] == 0:
                    self.__initialization(r, c)  # row, col

    def __initialization(self, row: int, col: int) -> None:
        '''落单查询'''
        cData = Candidate_database(row, col)
        # Check row
        for c in range(self.Boar.check):
            if (n := self.Boar.get(row, c)) != 0:
                cData.addnum(n)
        # Check col
        for r in range(self.Boar.check):
            if (n := self.Boar.get(r, col)) != 0:
                cData.addnum(n)
        # Check box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if (n := self.Boar.get(i, j)) != 0:
                    cData.addnum(n)
        self.ListCD.add(cData)

    def Naked_Singles(self) -> None:
        '''Naked Singles'''
        Ns_func = lambda x: len(x) == 1
        self.ListCD.filters(Ns_func)
        self.ListCD.echo('Naked Singles')

    def Hidden_Singles(self) -> None:
        '''
        Find Hidden Singles  
        When a digit is already present in a house, 
        none of the empty cells in that house can contain that digit
        '''
        step_a = self.ListCD.filters(lambda x: x.__len__() > 1)
        for sa in step_a:
            Sai = sa.Candidate()
            #Check row
            for r in range(self.Boar.check):
                getid = self.ListCD.getid(r, sa.col)
                if getid != None and getid != sa:
                    Sai = Sai - getid.Candidate()
                    if len(Sai) == 0:
                        break
            if len(Sai) == 1:
                print(f'Hidden Singles: {sa} -> {Sai} From Row')
                sa.SetCandidate(Sai)
                continue

            Sai = sa.Candidate()
            #Check col
            for c in range(self.Boar.check):
                getid = self.ListCD.getid(sa.row, c)
                if getid != None and getid != sa:
                    Sai = Sai - getid.Candidate()
                    if len(Sai) == 0:
                        break
            if len(Sai) == 1:
                print(f'Hidden Singles: {sa} -> {Sai} From Col')
                sa.SetCandidate(Sai)
                continue

            Sai = sa.Candidate()
            # Check box
            box_x = sa.col // 3
            box_y = sa.row // 3
            for i in range(box_y * 3, box_y * 3 + 3):
                for j in range(box_x * 3, box_x * 3 + 3):
                    getid = self.ListCD.getid(i, j)
                    if getid != None and getid != sa:
                        Sai = Sai - getid.Candidate()
                        if len(Sai) == 0:
                            break
            if len(Sai) == 1:
                print(f'Hidden Singles: {sa} -> {Sai} From Box')
                sa.SetCandidate(Sai)
                continue


def main() -> None:
    board_def = board(checksize=9)
    board_def.loadcsv()
    diff_set = difficulty(board_def)
    diff_set.Naked_Singles()
    diff_set.Hidden_Singles()
    diff_set.FixBoard()
    sodu_solve = shuduku(board_def)
    sodu_solve.solve()
    print(f'Solve ShuDu.....')
    board_def.echo()


if __name__ == "__main__":
    main()
