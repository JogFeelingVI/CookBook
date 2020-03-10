#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	   : 2020/2/9 10:24 上午
# @Author  : Lifelse (Lifelse@outlook.com)
# @Name	   : usre.py
import re, collections

token = collections.namedtuple('token', ['type', 'value'])
token_command = [
		('NAME', r'[a-zA-Z][a-zA-Z0-9]*'),
		('NUM', r'[0-9.]+'),
		('PLUS', r'\+'),
		('MINUS', r'\-'),
		('TIMES', r'\*'),
		('DIVIDE', r'\\'),
		('LPAREN', r'\('),
		('RPAREN', r'\)'),
		('EQ', r'\='),
		('WS', r'\s+')
	]
mast_pat = '|'.join(f'(?P<{x[0]}>{x[1]})' for x in token_command)

def generate_tokens(text):
	for mo in re.finditer(mast_pat, text):
		ty = mo.lastgroup
		va = mo.group()
		if type != 'WS':
			tka = token(ty, va)
			yield tka

class ExpressionEvaluator:
	'''
	Implementation of a recursive descent parser. Each method
	implements a single grammar rule. Use the ._accept() method
	to test and accept the current lookahead token. Use the ._expect()
	method to exactly match and discard the next token on on the input
	(or raise a SyntaxError if it doesn't match).
	'''
	def parse(self, text):
		self.tokens = generate_tokens(text)
		self.tok, self.ntok = None, None
		self._advance()
		self.expr()

	def _advance(self):
		self.tok = self.ntok
		self.ntok = next(self.tokens)
		print(self.ntok.type)

	def _accept(self, token_type):
		if self.ntok and self.ntok.type == token_type:
			self._advance()
			return True
		else:
			return False

def descent_parser():
	print(' Test start '.center(70, '-'))
	e = ExpressionEvaluator()
	test_a = e.parse('2+3')

if __name__ == '__main__':
	descent_parser()