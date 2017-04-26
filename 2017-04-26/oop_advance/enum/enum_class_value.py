#!/bin/env python
# -*- coding:utf-8 -*-
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
	for name, member in Weekday.__members__.items():
		print(name, '=>', member)
