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

def re_time():
	times = ['11/22/2020', 'Nov 27, 2012']
	compile_re = re.compile('\d+/\d+/\d+')
	for s in times:
		test = ['N','Y'][compile_re.match(s) is not None]
		print(f'{s:>15} Test {test}')

def re_group():
	txt = '010203040506070809101112'
	re_comp = re.compile('(\d{2})')
	group = re_comp.findall(txt)
	print(group)

def re_sub():
	def chang_m(m):
		M,D,Y = m.groups()
		M = [M, f'{M:0>2}'][len(M) == 1]
		D = [D, f'{D:0>2}'][len(D) == 1]
		return f'{Y}-{M}-{D}'
	text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
	print(text)
	text = re.sub(r'(\d+)/(\d+)/(\d+)', chang_m, text)
	print(text)

def re_ign():
	def chang(word:str):
		def subp(m):
			text = m.group()
			if text.isupper():
				return word.upper()
			elif text.islower():
				return word.lower()
			elif text[0].isupper():
				return word.capitalize()
			else:
				return word
		return subp
	txt = 'UPPER PYTHON, lower python, Mixed Python'
	print(txt)
	re_comp = re.compile(r'python', flags=re.IGNORECASE)
	finds = re_comp.sub(chang('snake'), txt)
	print(finds)

def text_just():
	text = 'Ni Hao feelingVI'
	lj = text.center(40, '-')
	print(f'[{lj}]')

if __name__ == '__main__':
	text_just()