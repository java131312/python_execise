#!/bin/env python
# -*- coding:utf-8 -*-
#@unique装饰器可以帮助我们检查保证没有重复值。
#Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
from enum import Enum,unique
@unique
class Weekday(Enum):
	Sun=0
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sat=6
if __name__=='__main__':
	day1=Weekday.Mon
	print day1
	print Weekday['Tue']
	print Weekday.Tue.value
	print(day1 == Weekday.Mon)
