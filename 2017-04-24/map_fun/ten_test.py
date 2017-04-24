#! /bin/env python
# -*- coding:utf-8 -*-
def add(x, y):
	return x*10 + y

print reduce(add,[1,3,5,7,9])
