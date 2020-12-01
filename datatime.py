#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2020/3/26 8:37 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: datatime.py
from decimal import Decimal, localcontext
import math, cmath, random, sys
from fractions import Fraction
from datetime import timedelta, datetime


def sishewuru():
	numb = 34.345323
	print(f'Num {numb}, round {round(numb, 2)}')
	na, nb = [Decimal('1.3'), Decimal('1.7')]
	print(f'a + b = {na + nb}')
	re = [False, True][na + nb == Decimal('3.0')]
	print(f'a + b ?= 6.3 {re}')
	chu = na / nb
	print(f'a / b is {chu}')
	with localcontext() as ctx:
		ctx.prec = 6
		print(f'a / b is {na / nb} is ctx.prec')
	nums = [1.23e+8, 1.23, -1.23e+8]
	print(f'sum {sum(nums)} math.fsum {math.fsum(nums)}')

def format_p():
	fnu = 123.4567890
	print(f'float nums [{fnu}]')
	print(f'format [{format(fnu, "0.2f")}]')
	print(f'format [{format(fnu, "10.2f")}]')
	print(f'format [{format(fnu, "^10.2f")}]')
	print(f'format [{format(fnu, ",.2f")}]')
	print(f'format [{format(fnu, ".2e")}]')

def bin_oct():
	num = 129
	print(f'Num {format(2**20+num, "b")}')
	print(int('0o755', 8))
	print(f'bytes [{num.to_bytes(16, "little")}]')

def strTobytes():
	txt = 'feelingVi is iZombie'
	bytesx = bytes(txt, encoding='utf-8')
	intby = int.from_bytes(bytesx, 'big')
	print(intby)

def scomplex():
	fus = complex(2, 4)
	fud = 3 - 4j
	print(fus + fud)
	print(cmath.sin(fud))
	fa = float('inf')
	print(math.isinf(fa))
	fsa = Fraction(3, 6)
	print(float(fsa))

def randchios():
	nums = [1, 2, 3, 4, 7, 4, 3.9, 6]
	rans = random.sample(nums,3)
	print(f'random.choice {rans}')

def datename():
	ta = datetime(2020, 3, 25)
	tb = timedelta(minutes=16, hours=6)
	print(ta.isoweekday())

def ssq2():
	red = [x for x in range(1,34)]
	blue = [x for x in range(1, 17)]
	coa = random.sample(red, 6)
	cob = random.sample(blue, 1)
	str_co = f'{coa} + {cob}'
	print(str_co)

def daletou():
	red = [x for x in range(1,34)]
	blue = [x for x in range(1, 17)]
	coa = random.sample(red, 5)
	cob = random.sample(blue, 2)
	str_co = f'{coa} + {cob}'
	print(str_co)

def fucai3d():
	nums = list('0123456789')
	a = random.sample(nums, 3)
	print(a)

def year():
	inps = 'y'
	while inps == 'y' or inps == 'Y':
		in_y = int(input('input year?'))
		run_y = f'{in_y} Run Nian' if in_y % 4 == 0 and in_y % 100 != 0 else 'No'
		print(run_y)
		inps = input('ji xu? [ y/n ]')

def syspath():
	ex, pa, pr = sys.executable, sys.path, sys.prefix
	print(f'executable {ex} path {pa} prefix {pr}')



if __name__ == '__main__':
	syspath()
