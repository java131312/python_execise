#!/bin/env python
# -*- coding:utf-8 -*-
try:
	f=open('/root/python1/python_execise/2017-04-2-4/modules/1.txt','r')
	print f.read()
finally:
	if f:
		f.close()

