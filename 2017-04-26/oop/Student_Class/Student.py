#!/bin/env python
# -*- coding:utf-8 -*-
class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
if __name__=='__main__':
	bart=Student('Bart Simpson',59)
	print bart
	print bart.name
