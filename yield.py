#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2020/10/18 9:26 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: yield.py

import itertools, time
import multiprocessing as mlp
from itertools import product, islice, repeat
from typing import Iterable


def listx():
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return product(d, d, d, d, d)


def gengs(xls: Iterable):
    i, z = xls
    func = lambda x: ''.join(map(str, x))
    z = [func(x) for x in z]
    iz = f'{i}: {z}'
    return iz

def gengs_s(*z):
    func = lambda x: ''.join(map(str, x))
    z = [func(x) for x in z]
    iz = f'Debug: {z}'
    return iz


def yields(max: int = 0, size=10, xls=None):
    index = 0
    while index <= max:
        yield islice(xls, 0, size)
        index += 1


def grouper(inputs, n, fillvalue=None):
    iters = [iter(inputs)] * n
    return itertools.zip_longest(*iters, fillvalue=fillvalue)


def zip_index(lis: list):
    return zip(itertools.count(), lis)

def log(func):
    print(f'Run {func.__name__}')
    def run(*args, **kwargs):
        __s =time.time()
        ex = func(*args, **kwargs)
        print(f'Use time {time.time() - __s:.2}s')
        return ex
    return run

def maps():
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    x = product(d, repeat=4)
    jie = yields(5001, 2, x)
    zjie = zip_index(jie)
    print(isinstance(zjie, Iterable))
    resn = map(gengs, zjie)
    for rs in resn:
        print(rs)

@log
def pool_map():
    '''
	pool map
	'''
    d = [1, 2, 4, 5, 6, 7, 8, 9, 0, 3]
    pr = product(d, repeat=4)
    po = mlp.Pool(processes=4)
    jie = yields(5000, 100, pr)
    for y in jie:
        resn = po.map(gengs_s, y)
        for r in resn:
            print(f'{r}')


if __name__ == '__main__':
    pool_map()
