# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-10-01 07:34:51
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-10-01 21:19:44

import csv


class board:
    '''数独 数字结构'''
    def __init__(self, checksize: int = 9) -> None:
        '''checksize 格子大小 最小为 9'''
        self.check = checksize if checksize in [4, 6, 9] else 9
        self.__array = [[0 for _ in range(self.check)]
                        for _ in range(self.check)]

    @property
    def Array(self) -> list:
        return self.__array

    def loadcsv(self) -> None:
        '''装载CSV文件'''
        with open('ShuDou - IQ180.csv') as read:
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


class shudu:
    '''
    解算数独
    '''
    def __init__(self, Board: board) -> None:
        ''' 解算数独的运算单位 '''
        self.Boar = Board

    def find_empty(self) -> tuple[int, int] | None:
        '''查找需要填写数字的坐标'''
        for r in range(self.Boar.check):
            for c in range(self.Boar.check):
                if self.Boar.Array[r][c] == 0:
                    return (r, c)  # row, col
        return None

    def solve(self) -> bool:
        '''解题核心'''
        find = self.find_empty()
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
        # for field in range(len(bo[0])):
        #     if bo[pos[0]][field] == num and pos[1] != field:
        #         return False
        for field in range(self.Boar.check):
            if self.Boar.get(row, field) == num and col != field:
                return False

        # Check column
        # for line in range(len(bo)):
        #     if bo[line][pos[1]] == num and pos[0] != line:
        #         return False
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


def main():
    print("Hello, World!")
    board_def = board(checksize=11)
    board_def.loadcsv()
    board_def.echo()
    sd_sov = shudu(board_def)
    sd_sov.solve()
    print(f'Solve ShuDu.....')
    board_def.echo()


if __name__ == "__main__":
    main()