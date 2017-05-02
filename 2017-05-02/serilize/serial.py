#!/bin/env python
# -*- coding:utf-8 -*-
try:
	import cPickle as pickle
except ImportError:
	import pickle
d =dict(name='Bob', age=20, score=88)
f = open('/root/python275/python_execise/2017-05-02/serilize/dump.txt','wb')
pickle.dump(d,f)
f.close()
