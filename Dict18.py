#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	   : 2020/2/9 10:24 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Name	   : Dict18.py
import runtime, collections, random, operator


@runtime.rtime('dicts', 1)
def dicts():
	prices = {
		'ACME': 45.23,
		'AAPL': 612.78,
		'IBM': 205.55,
		'HPQ': 37.20,
		'FB': 10.75
	}
	mypric = zip(prices.values(), prices.keys())
	pric_sort = sorted(mypric)
	print(prices)
	print(min(prices, key=lambda k: prices[k]))
	print(pric_sort)


@runtime.rtime('xtong', 1)
def dictxiangtong():
	a = {
		'a': 1,
		'b': 3,
		'c': 5
	}
	b = {
		'a': 4,
		'b': 2,
		'c': 5
	}
	print(a.keys() & b.keys())
	print(a.keys() - b.keys())
	print(a.items() & b.items())

	print({key: a[key] for key in a.keys() - {'z', 'b'}})

@runtime.rtime('dictsord', 1)
def dictsord():
	dsort = collections.OrderedDict()
	dsort['foo'] = 1
	dsort['look'] = 3
	dsort['SSd'] = 7
	for k,v in dsort.items():
		print(f' dsort key {k}, value {v}')

def slices():
	iterm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	sl = slice(2, 4)
	xr = iterm[sl]
	print(f'Slice {sl} item {xr}')
	strx = 'liasdjkkjkjkdeuhsdi'
	print(strx)
	a = slice(0, len(strx))
	print(a)
	for x in range(*a.indices(len(strx))):
		print(strx[x])

def counters():
	ran = random.Random()
	ces = [str(ran.randint(1, 16)) for x in range(1, 1000)]
	print(ces[-15:])
	ces_conter = collections.Counter(ces)
	print(ces_conter)

def dictsordx():
	rows = [
		{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
		{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
		{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
		{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
	]
	ite_key = operator.itemgetter
	s_rows = sorted(rows, key=ite_key('fname'))
	for x in s_rows:
		f, l, u = x.values()
		print(f'Name {f:>6} {l:<10} UID {u:>5}')

if __name__ == '__main__':
	dictsordx()
	print('okk')