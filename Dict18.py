#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	   : 2020/2/9 10:24 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Name	   : Dict18.py
import runtime


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


if __name__ == '__main__':
	dictxiangtong()
