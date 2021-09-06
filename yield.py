#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2020/10/18 9:26 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: yield.py

from itertools import product, islice

def listx():
	d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	return product(d, d, d, d, d)

def gengs(xls):
	for x in xls:
		print(x)
	print('end')

def yields(index:int=0, xls=None):
	while index <=10:
		yield islice(xls, 10)
		index += 1

def main():
	d = [1, 2 ,3 ,4 ,5 ,6 ,7, 8, 9, 0]
	x = product(d, repeat=5)
	jie = yields(xls=x)
	for j in jie:
		gengs(j)

if __name__ == '__main__':
	main()