#!/bin/env python
# -*- coding:utf-8 -*-
def reversed_cmp(x,y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0
if __name__=='__main__':
	print sorted([36,21,12,9,21],reversed_cmp)
