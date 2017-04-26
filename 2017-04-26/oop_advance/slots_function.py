#!/bin/env python
# -*- coding"utf-8 -*-
class Student(object):
	pass
def set_age(self,age):
	self.age=age
from types import MethodType
if __name__=='__main__':
	s=Student()
	s.name='Michael'
	print s.name
#	s.set_age=MethodType(set_age,s)
	Student.set_age=set_age
	s.set_age(25)
	print s.age
	s2=Student()
	s2.set_age(25)
