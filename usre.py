#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	   : 2020/2/9 10:24 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Name	   : usre.py
import random, operator

class user:
	def __init__(self, name:str):
		self.user_name = name
		self.user_id = self.maske_id(name)

	def __repr__(self):
		return f'User {self.user_name}, ID {self.user_id}'

	@staticmethod
	def maske_id(name:str):
		ASC = 'AsdWqeCzx'
		DEC = '123567890'
		VFD = 'UoIpLkGhM'
		RND = random.Random()
		ID = [RND.choice(name)]
		for inx in range(1, 16):
			Switch = RND.randint(1, 2)
			if  Switch % 3 == 0:
				ID.append(RND.choice(ASC))
			elif Switch %3 == 1:
				ID.append(RND.choice(DEC))
			else:
				ID.append(RND.choice(VFD))
		return ''.join(ID)

def loads():
	Users = [user(f'{x:0>4}') for x in range(1000, 1020)]
	for u in Users:
		print(u)
	suser = sorted(Users, key=operator.attrgetter('user_id'))
	print('Sort Users')
	for u in suser:
		print(u)

if __name__ == '__main__':
	loads()
