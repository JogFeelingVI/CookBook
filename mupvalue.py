import multiprocessing, itertools


class mups:
    @staticmethod
    def ites():
        lisx = itertools.combinations((x for x in range(1, 34)), 6)
        return lisx

    @staticmethod
    def funx(p: tuple) -> float:
        z = 1
        for pi in p:
            z = z * pi
        return z**(1 / p.__len__())

    @staticmethod
    def caule_p(p: tuple) -> str:
        L = p.__len__()
        fstr = '{:02}'
        strx = ' '.join(map(fstr.format, p))
        pfunx = mups.funx(p)
        if 13 <= pfunx <= 14:
            strx = f'{strx} / {mups.funx(p):.0f}'
        else:
            strx = 'NONE'
        return strx


if __name__ == '__main__':
    main_mps = mups()
    with multiprocessing.Pool(processes=8) as pls:
        rx = pls.imap(main_mps.caule_p, main_mps.ites(), chunksize=10000)
        for ir in rx:
            print(ir)
