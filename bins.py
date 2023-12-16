# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2021-11-21 21:12:49
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-12-16 16:03:40
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2019/8/29 11:10 下午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: bins
class nbin:
    num, bins = 1, '0b1'

    def __init__(self, Ns: int = 1):
        self.num = Ns
        self.bins: str = bin(self.num)

    def BinsX(self, bit: int = 7) -> str:
        sr = '{{:0>{}}}'.format(bit)
        sr = sr.format(self.bins.replace('0b', ''))
        return sr

    def Str(self) -> str:
        return 'Nu {:>4} bin {}'.format(self.num, self.bins)

    def Dict(self) -> dict:
        return {'num': self.num, 'bins': self.bins}

    def List(self) -> list:
        return [self.num, self.bins]


def loads():
    for x in range(1, 101):
        nv = nbin(x)
        print('{:>4} is {}'.format(x, ' '.join(nv.BinsX(7))))


if __name__ == '__main__':
    loads()
