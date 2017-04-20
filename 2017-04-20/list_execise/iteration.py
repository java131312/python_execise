# -*- coding:utf-8 -*-
 
d = {'a':1,'b':2,'c':3}
 
for key in d: #打印结果并不是按写的顺序， 默认迭代key
	 print key
     
     #迭代 value
 
for value in d.itervalues():
	 print value
     
for k,v in d.iteritems():
	print k,',',v
for ch in 'ABC':
	 print ch

 #判断对象是否可迭代

from collections import Iterable

print isinstance('abc',Iterable)
#整数不可迭代
#list实现， java类似的下表循环， 使用内置函数enumrate

for i,value in enumerate(['A','B','C']):
	 print i,value

#在Python 中同时迭代两个值是非常常见的
for x,y in [(1,1),(2,4),(3,9)]:
	print x,y
#列表生产式： 内置 用来创建list的生成式
print range(1,11)
 
#但是要生成[1x1,2x2,...]时怎么办1，循环L.append(ixi) 2, 列表生成式
    
print [x*x for x in range(1,11)]

#写列表生成式式， 把要生成的元素x*x放到前面， 后面跟for 循环。
# for 循环后面还可以加上if判断， 这样我们就可以筛选出仅偶数的平方：
print [x*x for x in range(1,11) if x%2==0]
print [m+n for m in 'ABC' for n in 'XYZ'] #双重循环生成全排列。

#列表生成式样也可以使用两个参数。
d = {'x':'A','y':'B','z':'C'}
    
print [k+'='+v for k,v in d.iteritems()]
    
L = ['Hello','World','IBM','Apple' ]
print [s.lower() for s in L ]

print isinstance(1,str) #判断是否式字符串。
