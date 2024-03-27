# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-03-27 08:06:09
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-03-27 10:08:41
from enum import IntEnum, Enum
import random


class YinYang(IntEnum):
    YIN = 0
    YANG = 1


class BaGua(Enum):
    QIAN = ('☰', 'tian', YinYang.YANG, YinYang.YANG, YinYang.YANG)
    DUI = ('☱', 'ze', YinYang.YIN, YinYang.YANG, YinYang.YANG)
    LI = ('☲', 'huo', YinYang.YANG, YinYang.YIN, YinYang.YANG)
    ZHEN = ('☳', 'lei', YinYang.YIN, YinYang.YIN, YinYang.YANG)
    XUN = ('☴', 'fen', YinYang.YANG, YinYang.YANG, YinYang.YIN)
    KAN = ('☵', 'shui', YinYang.YIN, YinYang.YANG, YinYang.YIN)
    GEN = ('☶', 'shan', YinYang.YANG, YinYang.YIN, YinYang.YIN)
    KUN = ('☷', 'di', YinYang.YIN, YinYang.YIN, YinYang.YIN)

    @property
    def symbol(self):
        return self.value[0]

    @property
    def name(self):
        return f'{self.value[1]:<4}'

    @property
    def yinyang(self):
        return ''.join(str(yy) for yy in self.value[2:])
    

dictmap = {
    BaGua.QIAN:'乾为天：元亨，利贞。',
    BaGua.KUN: '坤为地：元亨，利牝马之贞。君子有攸往，先迷后得主，利西南得朋，东北丧朋。安贞，吉。',
    BaGua.KAN: '坎为水：习坎，有孚，维心亨，行有尚。',
    BaGua.LI: '离为火：利贞，亨。畜牝牛，吉。',
    BaGua.ZHEN: '震为雷：亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯。',
    BaGua.GEN: '艮为山：艮其背，不获其身，行其庭，不见其人，无咎。',
    BaGua.XUN: '巽为风：小亨，利攸往，利见大人。',
    BaGua.DUI: '兑为泽：亨，利贞。'
}


def main():
    bGua = random.choices(list(BaGua), k=6)
    print(f'Hello, World! ☯️')
    temp = []
    for bg in bGua:
        
        match bg:
            case BaGua.KAN:
                print(f'{bg.symbol} {bg.name} {bg.yinyang} {dictmap.get(bg)}')
            case _ as cc if cc in [BaGua.QIAN, BaGua.KUN, BaGua.ZHEN]:
                print(f'+ {bg.symbol} {bg.name} {bg.yinyang} {dictmap.get(bg)}')
            case BaGua.LI | BaGua.DUI as cc:
                print(f'{cc.symbol} {dictmap.get(cc)}') 
            case _:
                print(f'{bg.symbol} {bg.name} {bg.yinyang}')
        
        yycode = [int(x) for x in bg.yinyang]
        match yycode:
            case [0,0,*_]:
                print(f'_{yycode=}')
                temp.append({'name':'ZHEN, KUN'})
            case [0,1,_]:
                print(f'_-{yycode=}')
                temp.append({'name':'dui','BG':bg})
            case [1,1,_]:
                print(f'--{yycode=}')
                temp.append({'name':'QIAN','KN':'XUN','BG':bg})
            case [1,0,_]:
                print(f'-_{yycode=}')
                temp.append({'GEN':bg})
                
    for t in temp:
        match t:
            case {'name': name, 'BG':bg, **qita} if not qita:
                print(f'{name =} {bg =}')
            case {'name': name} if ',' in name:
                print(f'--------{name =}')
            case {'GEN': name,**qita} if not qita:
                print(f'---qita not-----{name =}')
        


if __name__ == "__main__":
    main()
