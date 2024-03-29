# @Author: JogFeelingVi
# @Date: 2021-04-14 10:09:17
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-04-14 10:09:17
import itertools


class t3d:
    '''
        test 3d
    '''
    nlx = [3, 4, 5]

    def anlx(self):
        return itertools.product(range(0, 10), repeat=3)

    @staticmethod
    def xXx(n=nlx):
        z = set([abs(x - y) for x in n for y in n])
        dic = {
            1: lambda x: 0,  # baozi
            2: lambda x: 1,  # duizi
            3: lambda x: [3, 2][sum(x) == 3],  # shun zi 2, 3 不是顺子
            4: lambda x: [5, 4][0 in x and 1 in x],  # lian hao 4, 乱号5
        }
        return dic[len(z)](z)


def t3dt():
    '''
        xxx = 0 111 222     1
        xxx = [0,1,2] 456   2
        xxx = [0, [1,2,3,4,5,6,7]] 667 3
        xxx = [..] len is 4 
    '''
    t3 = t3d()
    for x in t3.anlx():
        xxx = t3.xXx(x)
        print(f'N {x} xXx {xxx}')


if __name__ == '__main__':
    t3dt()