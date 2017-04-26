#!/bin/env python
# -*- coding:utf-8 -*-
class Student(object):
	__slots__=('name','age')
class GraduateStudent(Student):
	pass
if __name__=='__main__':
	s=Student()
	s.name='Michael'
	s.age=25
	g=GraduateStudent()
	g.score=99
	print g.score
