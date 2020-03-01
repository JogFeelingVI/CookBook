#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	   : 2020/2/9 10:24 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Name	   : usre.py

from collections import namedtuple
import re, fnmatch

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

def sumx():
	lis = [1, 2, 5 , 7, 3, 9]
	print(sum(x * 10 for x in lis))
	dic = [{'v': 122, }, {'v': 34}, {'v': 78}]
	print(sum(x.get('v') for x in dic))
	dicc = namedtuple('dic', 'v')
	dicx = [dicc(x['v']) for x in dic]
	print(sum(x.v for x in dicx))
	print(max(x.v for x in dicx))

def split_re():
	line = 'ling x   wind,tmp* dex'
	rex = re.split(r'[\s*,]\s*', line)
	print(rex)
	url = 'https://www.google.com'
	print(url.startswith('https://'))
	sta = ['01,03,06,18,19,20', '07,12,16,19,32,33', '03,04,06,19,27,32', '09,12,16,23,27,29']
	stv = [x for x in sta if fnmatch.fnmatch(x, '*03*06*')]
	print(stv)



if __name__ == '__main__':
	split_re()