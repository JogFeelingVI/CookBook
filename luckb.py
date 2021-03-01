# @Author: JogFeelingVi 
# @Date: 2021-03-01 07:56:23 
# @Last Modified by:   By JogFeelingVi 
# @Last Modified time: 2021-03-01 07:56:23

from typing import NoReturn


def mlc() -> NoReturn:
    arr = [3,5,2,7,3,8,1,2,4,8,9,3]
    fco = [x for x in set(arr) if x == arr.count(x)]
    print(fco)

mlc()

