#!/bin/env python
# -*- coding:utf-8 -*-
'''
dict 是用空间换取时间的方法， key 必须是不可变对象

set 也是一组key的集合，但是不存储value在set中没有重复的key, 要创建set
需要提供一个list作为输入集合。
'''
d={'Sean':22,'Mirs':55,'Tom':66}

print d['Mirs']
d['Zming'] = 35
print d

if 'Mirs' in d:
	print d['Mirs']

print d.get('Mits')
print d.get('Mits',-1) #不存在时自己指定值。
#pop(key)删除对应的key 对应的values也会从dict中删除
d.pop('Mirs') #删除不存在的key时也会报错

s = set([1,1,2,3,3,3,3]) #重复元素会自动过滤。

print s
s.add(9)
s.remove(1)
print s
