#!/usr/local/bin/python3 



def CcharF(FILE) :	#liczę rozmiar linii w tablicy
	N=0
	for lines in FILE :
		N = len(lines)
	return N


def Krab1D (FILE, TEMPL) :			# definicja Karp-Rabin algorithm 
	m = len(TEMPL)
	n = len(FILE)
	d = 16
	q = 23
	p, ts, count = 0, 0, 0
	h = (d**(m-1))%q
	for i in range (0, m) :			# patter i 1. substring
		p = (d*p + ord(TEMPL[i]))%q
		ts = (d*ts + ord(FILE[i]))%q
	for i in range(0, n-m+1) : 
		if p == ts :
			if TEMPL[0:m] == FILE[i:i+m] :
				print("template is moved :", i)
				count+= 1	
		if i < n-m :
				ts = (d*(ts - ord(FILE[i])*h) + ord(FILE[i+m]))%q
		if ts < 0 : 
				ts = ts+q
	return count
	
with open("TRIAL1.txt","r") as f :
	f = f.readline()		#zapisuję linie do listy				
	FILE = str(f).strip('\n')
			
#TEMPL = ['ABC', 'B', 'C']
#Alf = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

TEMPL = 'ABC'


print(Krab1D(FILE, TEMPL))