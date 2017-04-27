#! /bin/env python3
# -*- coding:utf-8 -*-
from urllib import request
#这是python3的模块 如果有错误，请使用python3运行
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
