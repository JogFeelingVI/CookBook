# @Author: JogFeelingVi
# @Date: 2021-07-02 09:39:20
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-07-02 09:39:20
import datetime


def fstring():
    da = datetime.datetime(2021, 7, 4, 7, 30)
    db = datetime.datetime(2021, 7, 4, 18, 30)
    now_f = f'{da} - {db} = {db - da}'
    print(now_f)


if __name__ == '__main__':
    fstring()