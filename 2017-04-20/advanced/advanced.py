#!/bin/env python
# -*- coding:utf-8 -*-i

L=['AA','FF','EE','RR','WW']
r=[]

n=3
for i in range(n):
	r.append(L[i])

#print f
#切片操作 Slice 通过： 实现L[0:3]表示，从索引0开始，一直到索引3
#为止，但不包含索引3，即索引0，1，2， 正好是3，个元素。
print L
print 'L[0:3]--',L[0:3]  # 取索引为 0，1，2
print 'L[:3]--',L[:3]
print 'L[1:3]--',L[1:3]

print 'L[-1]--',L[-1]
print 'L[-2:]--',L[-2:]

print 'L[-2:-1]--',L[-2:-1]

'''
'''
