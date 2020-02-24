#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	   : 2020/2/9 10:24 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Name	   : usre.py

from collections import namedtuple

def filter_a():
	def insx(Na):
		try:
			int(Na)
			return True
		except:
			return False
	lis = [1, 2, -3, 4, 6, 7, -8, None, 'L', '-9']
	print([x for x in lis if type(x) is int])
	print(list(filter(insx, lis)))

def nametuple():
	old = {'r1': 1, 'r2': 5, 'r3': 7, 'b':9}
	print(old, old['r1'])
	Nums = namedtuple('Nums', ['r1', 'r2', 'r3', 'b'])
	nOld = Nums(1, 5, 7, 9)
	print(nOld.r1)
	r1x, *_ = nOld
	print(r1x)

if __name__ == '__main__':
	nametuple()