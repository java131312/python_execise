#!/bin/env python
# -*- coding:utf-8 -*-
class Student(object):
	name='Student'
	def __init__(self, name):
		self.name=name
if __name__=='__main__':
	s=Student('Bob')
	s.score=90
	print s.score
	print s.name
	del s.name
	print s.name
	#print Student.name
