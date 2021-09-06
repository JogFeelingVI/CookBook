# @Author: JogFeelingVi 
# @Date: 2021-09-03 11:32:37 
# @Last Modified by:   By JogFeelingVi 
# @Last Modified time: 2021-09-03 11:32:37
import itertools

d = [1, 2, 3, 4, 5, 'a', 7, 8, 'j', 'z'] # len 10
xlis = itertools.product(d,d)
Done = False

def load():
    for i, x in enumerate(xlis):
        print(x)
        yield [i, [f'{xs}' for xs in x ]]
    return [-1, 'Done']

def main():
    for i, l in load():
        tmp = '{}{}'.format(*l)
        print(f'index {i} - {tmp}')

if __name__ == '__main__':
    main()