#!/bin/env python
# -*- coding:utf-8 -*-
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('2017-04-25')
if __name__=='__main__':
	now()
