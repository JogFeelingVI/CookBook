# @Author: JogFeelingVi
# @Date: 2021-09-10 23:06:53
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-09-10 23:06:53
import multiprocessing as mlp, itertools as iterT, functools as funs, os, time
from functools import partial


class mTask:
    '''
        Bing xin renwu
    '''
    Produc, Count, Size = None, 0, 1000
    __stn, __psn = [0, 0]

    def log(func):
        @funs.wraps(func)
        def shell(*args, **kwargs):
            STN = time.time()
            rx = func(*args, **kwargs)
            ut = f'{time.time() - STN:.4f}'
            print(f'Time: {func.__name__} use time {ut}')
            return rx

        return shell

    def __init__(self, Gps: list = None) -> None:
        self.Produc = iterT.product(*Gps)
        self.Count = funs.reduce(lambda x, y: x * y, [len(x) for x in Gps])
        self.Status = {'Q': 0, 'cbflag': 0}
        self.__stn = time.time()

    def yidex(self):
        s = 0
        e = self.Count // self.Size + 1
        # zip (1, (1,2,3,4,5,6,7,8,9,))
        while s <= e:
            yield zip(iterT.count(), iterT.islice(self.Produc, 0, self.Size))
            s += 1

    def splitz(self):
        e = self.Count // self.Size + 1
        bji = lambda x: x * self.Size / self.Count * 100
        tmp = [[x, bji(x),
                tuple(iterT.islice(self.Produc, self.Size))]
               for x in range(0, e)]
        return tmp

    def Save(self, info: list):
        with open(file='./log.log', mode='a+', encoding='utf-8') as wAs:
            info = ''.join((f'{i}\n' for i in info))

            wAs.write(info)

    def Pbar(self, res):
        self.Status['Q'] += len(res)
        if time.time() - self.__psn >= 1.31:
            sav = self.Status['Q']
            tmpt = round(time.time() - self.__stn, 2)
            speed = round(sav / tmpt, 2)
            timeleft = round((self.Count - sav) / speed, 2)
            progressv = f'[ {sav/self.Count*100:.2f} %]'
            print(f'\rProgress: {speed}kb/s {tmpt}s {timeleft}TLs {progressv}',
                  end='')
            self.__psn = time.time()

    @log
    def mTaskR_yied(self):
        self.__psn = time.time()
        jie = self.yidex()
        with mlp.Pool(processes=mlp.cpu_count()) as p:
            for ji in jie:
                resaul = p.map(self.Comp_T, ji)
                if resaul != []:
                    self.Save(resaul)
                self.Pbar(resaul)

    def Comp_T(self, *xls):
        for i, j in xls:
            fmt = '{}' * len(j)
            fmts = fmt.format(*j)
            #print(f'{i}, {fmts}')
        return f'{i}: {fmts}'

    def show(self, r):
        #i, lens = r
        self.Status['cbflag'] = 1

    @log
    def mTaskR_dict(self):
        self.__psn = time.time()
        jie = self.splitz()
        with mlp.Pool(processes=mlp.cpu_count()) as p:
            resaul = p.map(self.Comp_D, jie)
            print('\r')
            print(f'Done~ {self.Status["Q"]}')

    def Comp_D(self, item):
        '''
        item = [1949, [...]]
        '''
        i, B, L = item
        buf = []
        for xl in L:
            fmt = '{}' * len(xl)
            fmts = fmt.format(*xl)
            buf.append(f'{fmts}')
        print(f'\rProgress: [{B:.2f}%]', end='')
        if buf != []:
            self.Save(buf)
        return i, buf.__len__()


def main():
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    s = list('abcdefghijklmn')
    S = [x.upper() for x in s]
    mTs = mTask([d, d, d, S, s, d])
    #mTs.mTaskR_yied()
    mTs.mTaskR_dict()


if __name__ == '__main__':
    main()