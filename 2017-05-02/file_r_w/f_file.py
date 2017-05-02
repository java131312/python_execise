#!/bin/env python
# -*- coding:utf-8 -*-
try:
	with open('/root/test.txt','r') as f:
		for line in f.readlines():
			print(line.strip())
finally:
	if f:
		f.close()
