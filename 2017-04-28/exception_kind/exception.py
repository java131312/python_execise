#!/bin/env python
# -*- coding:utf-8 -*-
if __name__=='__main__':

    try:
        print 'try...'
        r = 10 /0
        print 'result:',r
    except ZeroDivisionError,e:
        print 'except:',e
        print 'hello'
    finally:
        print 'finally...'
    print 'END'


