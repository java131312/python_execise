#!/bin/env python
# -*- coding:utf-8 -*-
from enum import Enum
if __name__=='__main__':
	Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Aug','Sep','Oct','Nov','Dec'))
	for name,member in Month.__members__.items():
		print(name,'=>',member,',',member.value)

