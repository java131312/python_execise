#!/bin/env python
# -*- coding:utf-8 -*-
def is_odd(n):
	return n % 2 == 1
def not_empty(s):
	return s and s.strip()
if __name__=='__main__':
	print filter(is_odd,[1,2,4,5,6,9,10,15])
	print filter(not_empty,['A','','B',None,'C',' '])
