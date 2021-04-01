# @Author: JogFeelingVi
# @Date: 2021-04-01 15:27:32
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-04-01 15:27:32
import itertools

b = [4, 3, 1, 0, 2]
abhz = [9, 12, 6, 15, 14, 0, 18]
bchz = [9, 10, 8, 7, 6, 11, 5, 12, 13] 
hz = [11, 15, 13, 9, 17, 19, 7, 21, 5, 23, 3, 25, 1, 27]
hzw = [1, 7, 5, 3]
dh = [12, 11, 15, 14, 9, 8, 17, 6, 18, 5, 3, 2, 0]
zh = [9, 8, 10, 7, 11, 12, 6, 13, 5]
xh = [4, 5, 6, 7, 8, 3, 9, 2, 10, 11, 1]
dc = [4, 3, 2, 1, 0]
zc = [3, 4, 2, 1]
xc= [1, 0, 2]
dijn=[1, 3, 5, 7]
ssd = itertools.repeat(10)
index = itertools.count(0, 1)
pro = itertools.product(b, abhz, bchz, hz, hzw, dh, zh, xh, dc, zc, xc, dijn)
zpro = zip(index, pro, ssd)
for zp in zpro:
    print(zp)