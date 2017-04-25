#!/bin/env python
# -*- coding:utf-8 -*-
def f(x):
	return x*x
if __name__=='__main__':
	L=[]
	for n in [1,2,3,4,5,6,7,8,9]:
		L.append(f(n))
	print L


