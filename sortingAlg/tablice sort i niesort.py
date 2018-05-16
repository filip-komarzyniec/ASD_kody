#!/usr/local/bin/python3


from functions import filluniqrand, MSort
import sys
import random 
import time 

def findMax(list) :
	return max(list)
	
def findMin(list) : 
	return min(list)
	
def find(list, val) : 
	i = 0
	while (val != arr[i]) :
		i+=1
		if val == arr[i] :
			break
	return arr[i]
	
def delete(list, val) :
	b = find(list, val)
	del b
	return list
def NPinsert(list,val) :
	list.append(val)
	
def Pinsert(list,val) :
	for i in range(0, len(list) + 1) : 
		if list[i] > val : 
			index = i 
			break
	new_list = []
	new_list = list[:i] + [val] + list[i:]
	return new_list
			

# Nieposortowana tablica 10^6 elementów
 
"""arr = []
arr = filluniqrand(arr)


t01 = time.time()
NPinsert(arr,5)
t0 = time.time()
findMin(arr)
t2 = time.time()
findMax(arr)
t3 = time.time()
delete(arr,random.choice(arr))
t4 = time.time()
find(arr,random.choice(arr))
t5 = time.time()

print("inserting time is : ", t0-t01, sep='\t')
print("finding Min time is : ", t2-t0, sep='\t')
print("finding Max time is : : ", t3-t2, sep='\t')
print("deleting node time is : ", t4-t3, sep='\t')
print("finding node time is : ", t5-t4, sep='\t')"""

# Posortowana tablica

arr = []
arr = filluniqrand(arr)

#for i in range(1, 10**6) :
#	if i not in arr :
#		b = i
arr = MSort(arr)
t01 = time.time()
Pinsert(arr,5)
t0 = time.time()
findMin(arr)
t2 = time.time()
findMax(arr)
t3 = time.time()
delete(arr,random.choice(arr))
t4 = time.time()
find(arr,random.choice(arr))
t5 = time.time()

print("inserting time is : ", t0-t01, sep='\t')
print("finding Min time is : ", t2-t0, sep='\t')
print("finding Max time is : : ", t3-t2, sep='\t')
print("deleting node time is : ", t4-t3, sep='\t')
print("finding node time is : ", t5-t4, sep='\t')
