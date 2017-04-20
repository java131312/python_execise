#!/bin/env python
# -*- coding:utf-8 -*-

#测测能用中文吗

#声明一个列表

names = ['Sean','Mirs','Index']

for name in names:
	print name

sum = 0
for x in range(101):
	sum = sum+x

print sum

sum =0
n=99
while n>0:
	sum = sum + n
	n = n - 2

print sum

#raw_input()读取的内容永远以字符串的形式返回，如果为int需要使用int('str')
