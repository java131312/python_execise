#!/bin/env python
# -*- coding:utf-8 -*-
L=list(range(100))
print L
print L[:10]
print L[-10:]
print L[10:20]
print L[:10:2]
print L[::5]
#甚至什么都不写， 只写[:]就可以原样复制一个list
print L[:]
#tuple也是一种list,唯一区别式tuple不可变，因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print (0,1,2,3,4,5)[:3]

