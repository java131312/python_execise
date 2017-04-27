#!/bin/env python
# -*- coding:utf-8 -*-
class MyClass():
	x=100
	def func(self,name):
		return "Hi %s!" % name
	def func2(self):
		return self.x
if __name__=='__main__':
	mc = MyClass()
	print mc.x
	print mc.func('xiaoqiang')
	print mc.func2()

