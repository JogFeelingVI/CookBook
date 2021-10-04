# @Author: JogFeelingVi 
# @Date: 2021-10-04 12:17:01 
# @Last Modified by:   By JogFeelingVi 
# @Last Modified time: 2021-10-04 12:17:01
from functools import cache

@cache
def fbi(n:int=100):
    if n < 2:
        return n
    return fbi(n-1) + fbi(n-2)

def main():
    for i in range(100):
        print(f'Debug Fbi {i}, FBI {fbi(i)}')

if __name__ == '__main__':
    main()