#!/bin/env python
# -*- coding:utf-8 -*-
def now():
	print('2017-04-25')
f=now
f()
print now.__name__
print f.__name__

def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper
@log
def now():
	print('2017-04-25')
if __name__=='__main__':
	now()
