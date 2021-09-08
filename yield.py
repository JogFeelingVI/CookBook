#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2020/10/18 9:26 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: yield.py

import itertools
import multiprocessing
from itertools import product, islice
from typing import Iterable

def listx():
	d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	return product(d, d, d, d, d)

def gengs(xls:Iterable):
	i, z = xls
	z = [f'{x}' for x in z]
	iz = f'{i}: {z}'
	return iz

def yields(max:int=0, xls=None):
	index = 0
	while index <= max:
		yield islice(xls, 0, 2)
		index += 1

def grouper(inputs, n, fillvalue=None):
	iters = [iter(inputs)] * n
	return itertools.zip_longest(*iters, fillvalue=fillvalue)

def zip_index(lis:list):
	return zip(itertools.count(), lis)

def main():
	d = [1, 2 ,3 ,4 ,5 ,6 ,7, 8, 9, 0]
	x = product(d, repeat=9)
	jie = yields(100000, x)
	zjie = zip_index(jie)
	print(isinstance(zjie, Iterable))
	resn = map(gengs, zjie)
	print(list(resn))

if __name__ == '__main__':
	main()