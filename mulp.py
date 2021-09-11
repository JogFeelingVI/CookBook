# @Author: JogFeelingVi
# @Date: 2021-09-10 23:06:53
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-09-10 23:06:53
import multiprocessing as mlp, itertools as iterT, functools as funs, os, time


class mTask:
    '''
        Bing xin renwu
    '''
    Produc, Count, Size = None, 0, 1000
    __stn, __psn = [0, 0]

    def __init__(self, Gps: list = None) -> None:
        self.Produc = iterT.product(*Gps)
        self.Count = funs.reduce(lambda x, y: x * y, [len(x) for x in Gps])
        self.Status = {'S': 0}
        self.__stn = time.time()

    def yidex(self):
        s = 0
        e = self.Count // self.Size + 1
        # zip (1, (1,2,3,4,5,6,7,8,9,))
        zjie = zip(iterT.count(), self.Produc)
        while s <= e:
            yield iterT.islice(zjie, 0, self.Size)
            s += 1


    def Comp_T(self, *xls):
        for i, j in xls:
            fmt = '{}' * len(j)
            fmts = fmt.format(*j)
        return f'{i}: {fmts}'

    def Save(self, info:list):
        with open(file='./log.log', mode='a+', encoding='utf-8') as wAs:
            info = ''.join((f'{i}\n' for i in info))
            wAs.write(info)

    def Pbar(self, res):
        self.Status['S'] += len(res)
        if time.time() - self.__psn >= 1.31:
            sav = self.Status['S']
            tmpt = round(time.time() - self.__stn, 2)
            speed = round(sav / tmpt, 2)
            timeleft = round((self.Count - sav) / speed, 2)
            progressv = f'[ {sav/self.Count*100:.2f} %]'
            print(f'\rProgress: {speed}kb/s {tmpt}s {timeleft}TLs {progressv}',
                  end='')
            self.__psn = time.time()

    def mTaskR(self):
        self.__psn = time.time()
        jie = self.yidex()
        with mlp.Pool(processes=mlp.cpu_count()) as p:
            for ji in jie:
                resaul = p.map(self.Comp_T, ji)
                if resaul != []:
                    self.Save(resaul)
                self.Pbar(resaul)


def main():
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    s = list('abcdefghijklmn')
    S = [x.upper() for x in s]
    mTs = mTask([d, d, d, S, s, d])
    mTs.mTaskR()


if __name__ == '__main__':
    main()