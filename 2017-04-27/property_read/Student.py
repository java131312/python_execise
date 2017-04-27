#!/bin/env python
# -*- coding:utf-8 -*-
class Student(object):
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth = value

	@property
	def age(self):
		return 2017 -self._birth
if __name__=='__main__':
	s=Student();
	s.birth=1989
	print s.age
	s.age=11
