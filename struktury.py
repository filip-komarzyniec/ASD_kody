#!/usr/local/bin/python3

import random

def frange(start, stop, step) :
	i = start
	while i < stop: 
		yield i
		i += step

	
n = int(input("root length is: "))



arr = []

arr.append(0.45)
print (arr)
a = frange(0.5,10000,1)
arr.append(random.choice(a))



print(arr) 