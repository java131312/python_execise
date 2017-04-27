#!/bin/env python
# -*- coding:utf-8 -*-
class Runnable(object):
	def run(self):
		print('Running...')
class Flyable(object):
	def fly(self):
		print('Running...')
class Animal(object):
	pass
class Mannal(Animal):
	pass
class Bird(Animal):
	pass
class Dog(Mammal, Runnable):
	pass
class Bat(Mammali,Flyable):
	pass
class Parrot(Bird):
	pass
class Ostrich(Bird):
