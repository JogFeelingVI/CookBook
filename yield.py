#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2020/10/18 9:26 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: yield.py

def list():
	list = [x*x for x in range(10)]
	for x in list:
		print(x, end=' ')

def gengs():
	lists = (x*x for x in range(10))
	for x in lists:
		print(x, end=' ')

def yields(index:int=0):
	print(f'index [ {index:^3} ]')
	while index <= 10:
		yield index
		print('x')
		index += 1
	print(f'edx [ {index:^3} ]')

if __name__ == '__main__':
	for x in yields():
		print(x)