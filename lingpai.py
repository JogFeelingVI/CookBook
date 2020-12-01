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
		return self.expr()

	def _advance(self):
		self.tok = self.ntok
		self.ntok = next(self.tokens, None)

	def _accept(self, token_type):
		if self.ntok and self.ntok.type == token_type:
			self._advance()
			return True
		else:
			return False

	def _expect(self, token_type):
		if not self._accept(token_type):
			raise SyntaxError(f'Expected {token_type}')

	def expr(self):
		'''
		num +|- other
		expression ::= term { ('+'|'-') term }*
		:return:
		'''
		exprval = self.term()
		while self._accept('PLUS') or self._accept('MINUS'):
			op = self.tok.type
			r_item = self.term()
			if op == 'PLUS':
				exprval += r_item
			elif op == 'MINUS':
				exprval -= r_item
		return exprval

	def term(self):
		termval = self.factor()
		while self._accept('TIMES') or self._accept('DIVIDE'):
			op = self.tok.type
			r_item = self.factor()
			if op == 'TIMES':
				termval *= r_item
			elif op == 'DIVIDE':
				termval /= r_item
		return termval

	def factor(self):
		'''
		factor ::= NUM | ( expr )
		:return:
		'''
		if self._accept('NUM'):
			return float(self.tok.value)
		elif self._accept('LPAREN'):
			exprval = self.expr()
			self._expect('RPAREN')
			return  exprval
		else:
			raise SyntaxError('NUM and LPAREN')

def descent_parser(text:str):
	print(' Test start '.center(70, '-'))
	e = ExpressionEvaluator()
	formula = (f'{text}')
	result = f'{e.parse(text)}'
	strs = f'Formula {formula}\n result {result}'
	print(strs)

if __name__ == '__main__':
	descent_parser('2+(2*23)')