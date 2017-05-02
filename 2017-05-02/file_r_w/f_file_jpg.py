#!/bin/env python
# -*- coding:utf-8 -*-
try:
	with open('/root/python275/python_execise/2017-05-02/file_r_w/timg.jpg','rb') as f:
		for line in f.readlines():
			print(line.strip())
finally:
	if f:
		f.close()
