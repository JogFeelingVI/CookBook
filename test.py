# @Author: JogFeelingVi
# @Date: 2021-04-14 08:10:12
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-04-14 08:10:12
def bin_search(xlis: list, x: int) -> int:
    lo, hi = 0, xlis.__len__()
    while lo < hi:
        mi = (lo + hi) // 2
        if xlis[mi] < x:
            lo = mi + 1
        else:
            hi = mi
    return lo


nlx = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # len 10
dcs = bin_search(nlx, 7)
print(f'index {dcs} VA {nlx[dcs]}')