#!/bin/env python
# -*- coding:utf-8 -*-
class Student(object):
	def __init__(self):
		self.name = 'Michael'
#动态返回属性
	def __getattr__(self, attr):
		if attr=='score':
			return 99
		if attr=='age':
			return lambda:25
if __name__=='__main__':
	s = Student()
	print s.name
	print s.score
	print s.age()
