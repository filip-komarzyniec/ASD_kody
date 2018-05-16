#!/usr/local/bin/python3
import time
count = 0
def Hanoi (n,sor,dest,buff) :
	if n%2==1 :
		i=1
	else : 
		i=2**n-1
	while (sor or buff): 
		if i%3==1 :
			Move_disk1(sor, dest)
		if i%3==2 :
			Move_disk2(sor, buff)
		if i%3==0 :
			Move_disk0(buff, dest)
		i+=1
		


def Move_disk1 (sor, dest) :
	global count
	if (sor and dest) :
		if dest[len(dest)-1] > sor[len(sor)-1] :
			sor.append(dest.pop())
			count+=1
			print ("moving from :", dest, "to : ", sor, sep='\t')
		else :
			dest.append(sor.pop())
			count+=1
			print ("moving from :", sor, "to : ", dest, sep='\t')
		return
	if sor :
		dest.append(sor.pop())
		count+=1
		print ("moving from :", sor, "to : ", dest, sep='\t')
		return
	if dest :
		sor.append(dest.pop())
		count+=1
		print ("moving from :", dest, "to : ", sor, sep='\t')
def Move_disk2(sor, buff) :
	global count
	if (sor and buff) :
		if sor[len(sor)-1] > buff[len(buff)-1] :
			buff.append(sor.pop())
			count+=1
			print ("moving from :", sor, "to", buff, sep='\t')
		else :
			sor.append(buff.pop())
			count+=1
			print ("moving from :", buff, "to", sor, sep='\t')
		return
	if sor :
		buff.append(sor.pop())
		count+=1
		print ("moving from :", sor, "to", buff, sep='\t')
		return
	if buff :
		sor.append(buff.pop())
		count+=1
		print ("moving from :", buff, "to", sor, sep='\t')
def Move_disk0(buff,dest) :
	global count
	if (buff and dest) : 
		if buff[len(buff)-1] > dest[len(dest)-1] :
			dest.append(buff.pop())
			count+=1
			print ("moving from :", buff, "to", dest, sep='\t')
		else :
			buff.append(dest.pop())
			count+=1
			print("moving from :", dest, "to", buff, sep='\t')
		return
	if buff :
		dest.append(buff.pop())
		count+=1
		print ("moving from :", buff, "to", dest, sep='\t')
		return
	if dest : 
		buff.append(dest.pop())
		count+=1
		print("moving from :", dest, "to", buff, sep='\t')
	
n = int(input("disks number is : "))
sor, dest, buff = ([] for i in range(3))
sor.extend(range(1,n+1))
print(sor)
t1 = time.time()
Hanoi (n,sor,dest,buff)
t2 = time.time()
print (dest)
print (buff)
print (sor)
print("move count :",count)
print ("czas iteracji :", t2-t1)