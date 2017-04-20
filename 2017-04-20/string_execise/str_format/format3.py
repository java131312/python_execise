#!/bin/env python
#-*- coding:utf-8 -*-
print '%2d-%02d' % (3,1)
print '%.2f' % 3.1415926
print 'Age:%s. Gender:%s' % (25,True)
#对于Unicode字符串，用法完全一样，但最好确保替换的字符串也是Unicade字符串。
print u'Hi, %s' % u'Michael'
#有时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print 'growth rate: %d %%' % 7
