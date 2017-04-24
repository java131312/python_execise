#!/bin/env python
# -*- coding:utf-8 -*-
L=[x*x for x in range(10)]
print L
g=(x*x for x in range(10))
print g
#建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

#我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：

next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
