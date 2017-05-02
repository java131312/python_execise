#!/bin/env python
# -*- coding:utf-8 -*-
import json
def student2dict(std):
	return{
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
s = student2dict({'name':'kxy','age':80,'score':77})
print(json.dumps(s,default=student2dict))

