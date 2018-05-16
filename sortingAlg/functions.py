#!/usr/local/bin/python3

import random

def ISort(list) :
	for i in range(0,len(list)) :
		x = list[i]
		j = i - 1
		while j >= 0 and list[j] > x :
			list[j+1] = list[j]
			j = j - 1
		list[j+1] = x
	return list


def filluniqrand(list) : 
	n = int(input("enter list length : "))
	list = random.sample(range(10**10,-1, -1),n)
	return list
	
	
def pprinting(list) :
	for i in range(0,len(list)) :
		snumb = str(list[i])
		if i!= 0 and i%10 == 0 :
			print('\n')
		print(snumb, end="\t")
	print('\n')
	return 
	
	
def MSort(list) :	
	res = []
	middle = int(len(list)/2)
	if len(list) < 2 :
		return list
	Lhalf = MSort(list[:middle])
	Rhalf = MSort(list[middle:])
	i = 0
	j = 0
	while i < len(Rhalf) and j < len(Lhalf) :
		if Rhalf[i] > Lhalf[j] :
			res.append(Lhalf[j])
			j += 1
		else :
			res.append(Rhalf[i])
			i += 1
	res += Rhalf[i:]
	res += Lhalf[j:]
	return res
