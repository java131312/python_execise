#!/bin/env python
# -*- coding:utf-8 -*-
def fn(x,y):
	return x*10 + y
if __name__=='__main__':
	r=reduce(fn,[1,3,5,7,9])
	print r
