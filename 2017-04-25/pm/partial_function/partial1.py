#!/bin/env python
# -*- coding:utf-8 -*-
import functools
if __name__=='__main__':
	int2=functools.partial(int,base=2)
	print int2('1000000')
	print int2('1010101')
