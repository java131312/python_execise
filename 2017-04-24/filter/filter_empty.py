#!/bin/env python
# -*- coding:utf-8 -*-
def not_empty(s):
	return s and s.strip()
print filter(not_empty,['A','','B',None,'C',''])
