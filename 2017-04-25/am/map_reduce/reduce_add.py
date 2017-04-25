#!/bin/env python
# -*- coding:utf-8 -*-
def add(x,y):
	return x + y
if __name__=='__main__':
	r=reduce(add,[1,3,5,7,9])
	print r
