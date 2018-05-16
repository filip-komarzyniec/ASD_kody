#!/usr/local/bin/python3

from functions import * 
import time 
import random

numbers = []
timess = []
n = int(input("list length :"))			#ilość elementów w liście 
for i in range(0,100) :			#200 list 
	numbers = random.sample(range(1000000,-1,-1),n)			
	t = time.time()
	MSort(numbers)
	t1 = time.time()
	x = t1 - t
	timess.append(x)
# pprinting(timess)			#wypisywanie listy czasów sortowania 
print(max(timess), end='\t')			#najdłuższy czas sortowania 
print(min(timess), end='\t')			#najkrótszy czas sortowania 
sum = 0
for i in range(0,len(timess)) :
	sum+=timess[i]
aver = sum / len(timess)
print("overall sorting time is :" + str("%.10f" % sum), end='\t')			#sumaryczny czas sortowania 
print(aver)			#średni czas jednego sortowania 




