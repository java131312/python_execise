#!/bin/env python
# -*- coding:utf-8 -*-
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score= score
def process_student(name):
	std = Student(name)
	do_task_1(std)
	do_task_2(std)

def do_task_1(std):
	do_subtask_1(std)
	do_subtask_2(std)
def do_task_2(std):
	do_subtask_2(std)
	do_subtask_2(std)
global_dict = {}
def std_thread(name):
	std = Student(name)
	global_dict[threading.current_thread()] = std
	do_task_1()
	do_task_2()
def do_task_1():
	std = global_dict[threading.current_thread()]
def do_task_2():
	std = global_dict[threading.current_thread()]
import threading

local_school=threading.local()
def process_student():
	print 'Hello. %s (in %s)' % (local_school.student,threading.current_thread().name)
def process_thread(name):
	local_school.student = name
	process_student()
t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread_A')
t2 = threading.Thread(target=process_thread, args=('Bob',),name='Thread_B')

t1.start()
t2.start()
t1.join()
t2.join()

