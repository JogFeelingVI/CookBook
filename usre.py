#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	   : 2020/2/9 10:24 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Name	   : usre.py
import random, operator, itertools


def maske_id(name: str):
	ASC = 'AsdWqeCzx'
	DEC = '123567890'
	VFD = 'UoIpLkGhM'
	RND = random.Random()
	ID = [RND.choice(name)]
	for inx in range(1, 16):
		Switch = RND.randint(1, 2)
		if Switch % 3 == 0:
			ID.append(RND.choice(ASC))
		elif Switch % 3 == 1:
			ID.append(RND.choice(DEC))
		else:
			ID.append(RND.choice(VFD))
	return ''.join(ID)


def aged(a: int, b: int) -> int:
	RND = random.Random()
	return RND.randint(a, b)


class user:
	def __init__(self, name: str):
		self.user_name = name
		self.user_id = maske_id(name)

	def __repr__(self):
		return f'User {self.user_name}, ID {self.user_id}'


class usergy:
	def __init__(self, name: str):
		self.data = {'name': name, 'age': aged(30, 70), 'add': aged(420, 430), 'mid': maske_id(name)}

	def __repr__(self):
		name, age, add, mid = self.data.values()
		return f'{name} -> {age}, {add}, {mid}'



def loads():
	Users = [user(f'{x:0>4}') for x in range(1000, 1020)]
	for u in Users:
		print(u)
	suser = sorted(Users, key=operator.attrgetter('user_id'))
	print('Sort Users')
	for u in suser:
		print(u)


def loadsx():
	users = [usergy(f'{x:>05}') for x in range(1000, 1150)]
	users.sort(key=lambda x:[x.data['age'], x.data['add']])
	for date, items in itertools.groupby(users, key=lambda x:[x.data['age'], x.data['add']]):
		print(date)
		for i in items:
			print(' ', i)


if __name__ == '__main__':
	loadsx()
