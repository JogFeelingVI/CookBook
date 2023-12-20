# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-12-18 09:14:06
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-12-18 09:47:13
import threading, time, random


class user:
    def __init__(self, money: int) -> None:
        self.__money = money

    def Withdraw_money(self, money: int):
        '''Withdraw money'''
        if self.__money >= money:
            self.__money -= money
            print(
                f'Withdraw money {money} balance {self.__money} time {time.time()}'
            )

    def save_money(self, money: int):
        '''save money'''
        self.__money += money
        print(f'Save money {money} balance {self.__money} time {time.time()}')

    def __str__(self) -> str:
        return f'Account Balance {self.__money}'


def draw(zhanghu: user):
    for _ in range(500):
        money = random.randint(800, 1500)
        zhanghu.Withdraw_money(money=money)
        time.sleep(0.5)


def save(zhanghu: user):
    for _ in range(500):
        money = random.randint(100, 1000)
        zhanghu.save_money(money=money)
        time.sleep(1)


def main():
    zhansan = user(money=3000)
    print(f'Hello, World! {zhansan}')
    tw = threading.Thread(name='withdraw', target=draw, args=(zhansan, ))

    ts = threading.Thread(name='save', target=save, args=(zhansan, ))
    tw.start()
    ts.start()
    ts.join()
    tw.join()


if __name__ == "__main__":
    main()
