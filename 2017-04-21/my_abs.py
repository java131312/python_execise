#!/bin/env python
# -*- coding:utf-8 -*-
print u'函数的自定义'
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
re1 = my_abs(-9)
print re1
re2 = my_abs(2)
print re2
