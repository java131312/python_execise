#!/usr/bin/env python
def cont():
	for i in range(1,6):
		if i == 3:
			continue
		else:
			print i
if __name__ =="__main__":
	print("main")
	cont()

