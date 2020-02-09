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
	print(min(prices, key=lambda k:prices[k]))
	print(pric_sort)


if __name__ == '__main__':
	dicts()
