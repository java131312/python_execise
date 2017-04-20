#!/bin/env python
# -*- coding:utf-8 -*-
__author__ = '康晓宇'

class Fib(object):
	def __getitem__(self,item):
		if isinstance(item,int):
			a,b=1,1
		for x in range(item):
			a,b = b, a+b
		return n
		
		if isinstance(item,slice):
			start = item.start
			stop = item.stop
			a,b = 1,1
			
			L = []

			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b, a+b
			return L
f = Fib()

#print f[5:10]

class Student(object):
	def __init__(self):
		self.name = "Mirs"

	def __getattr__(self,item):
		if item == 'score':
			return 99
		if item == 'age':
			return lambda:25

	def __call__(self):
		print("My name is %s..."%self.name)
ss = Student()
print ss.score
print ss.age()

#---------------__call__------------------
#instance,method, 可不可以， 类似于 instance()本身上调用呢， 在Python中， 是肯定的

#只要定义一个__call__() 就可以多实例进行调用

ss()
