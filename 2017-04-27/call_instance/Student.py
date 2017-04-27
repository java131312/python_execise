#!/bin/env python
# -*- coding:utf-8 -*-
# 测试中文
#把函数看成对象，因为这两者之间本来就没啥根本的区别。
class Student(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s.' % self.name)
if __name__=='__main__':
	s=Student('Michael')
	s()
	print callable(Student('test'))
	print callable(max)
	print callable([1,2,3])
	print callable(None)
	print callable('str')
