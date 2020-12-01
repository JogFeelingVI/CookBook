#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	   : 2020/2/9 10:27 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Name	   : runtime.py
import time

def RunTime(fun, coun):
	"""
	计算代码执行时间
	:param fun: 执行函数
	:param coun: 执行次数
	"""
	s = time.time()
	for x in range(coun):
		fun()
	e = time.time()
	print(f'Case:{fun.__name__:^5} Run Time {e - s:>10.8f}')


def rtime(tx: str = 'time', co: int = 1):
	"""
	@zhuang shi qi
	:param tx:
	:return:
	"""

	def fc(fun):
		def work(*a, **ka):
			print(f'Text {tx} Count {co}')
			s = time.time()
			for x in range(co):
				fun(*a, **ka)
			e = time.time()
			print(f'Case:{fun.__name__:^5} Run Time {e - s:>10.8f}')

		return work

	return fc