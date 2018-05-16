#!/usr/local/bin/python3

import time 

SOR, DEST, BUFF = ([] for i in range(3))
count = 0
def Hanoi(n, sor, dest, buff) :
	if n == 1 :
		Move_disk(sor, dest)
		return
	Hanoi(n-1, sor, buff, dest)
	Move_disk(sor, dest)
	Hanoi(n-1, buff, dest, sor)
	return
	
	
	
	
def Move_disk(sor, dest) :
	global count
	if count == 0 : 
		dest.append(sor.pop())
		tsor = tuple(sor)
		tdest = tuple(dest)
		dict = { tuple(SOR) : 1 , tuple(DEST) : 3, tuple(BUFF) : 2 } 
		print("moving from : ",dict[tsor], "to : ", dict[tdest] , sep='\t ')
	else :
		tsor = tuple(sor)
		tdest = tuple(dest)
		dict = { tuple(SOR) : 1 , tuple(DEST) : 3, tuple(BUFF) : 2 }
		print("moving from : ",dict[tsor], "to : ", dict[tdest] , sep='\t ')
		dest.append(sor.pop())
	count+=1
	return



n = int(input("podaj liczbę krążków :"))
SOR.extend(range(1,n+1))
sor = SOR
dest = DEST
buff = BUFF
print (sor)
t1 = time.time()
Hanoi(n, sor, dest, buff)
t2 = time.time()
print("move count :", count, sep='\t')
print ("czas rekurencji :", t2-t1)

