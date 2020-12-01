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

def yields():
	def ysc(max:int=10):
		for x in range(max+1):
			if x %2 ==0:
				yield x
	print(ysc(10))
	eysc = ysc(10)
	for x in eysc:
		print(x, end=' ')

if __name__ == '__main__':
	yields()