#!/usr/local/bin/python3

import time

def CcharF(FILE) :	#liczę rozmiar linii w tablicy
	N=0
	for lines in FILE :
		N = len(lines)
	return N
	


def Naive_Matcher(FILE, TEMPL) : 
	s, count = 0, 0 
	n = CcharF(FILE)
	m = len(TEMPL)
	C = sum(1 for k in FILE)	#liczę linie w FILE
	for i in range (s, n-m+1) :	#iteruję po ilości znaków w FILE
		for j in range(0,C-2)	:	#iteruję po wierszach w FILE
			if TEMPL[0][0:m] == FILE[j][i:i+m] and TEMPL[1][0] == FILE[j+1][i] and TEMPL[2][0] == FILE[j+2][i] :
				if j==0:
					#print("template is moved :", i , sep='\t')
					count+=1
				else :
					#POI = n*(j+1) - (n-i)
					#print("template is moved :", POI ,j, i, sep='\t')	#można sprawdzić wiersz i kolumnę
					count+=1
	return "template number is" + '\t' + str(count)
	


#TEMPL = ["elo","l","o"]

TEMPL = ["ABC", "B", "C"]


"""with open("TRIAL.txt","r") as f :
	f = f.readlines()		#zapisuję linie do listy				
	FILE = [letter.strip('\n') for letter in f]"""
	
with open("5000_pattern.txt","r") as f :
	f = f.readlines()		#zapisuję linie do listy				
	FILE = [letter.strip('\n') for letter in f]


"""print(FILE[6][308:311])	# sprawdzanie czy wzorce rzeczywiście tam są
for i in range(0,3) :
	print( FILE[6+i][308])"""


t1 = time.time()
print(Naive_Matcher(FILE,TEMPL))
t2 = time.time()
print("overall time is: ", t2-t1, sep='\t')


#FILE = [[list.append(j) for j in f while j!='\n'] for i in f while i!='\n' ]
#tworzenie 2D array z dwóch 
"""A = ["a","b","v"]
B = ["c","f","h"]

d = [A,B]
print(d)
str = ["ABCDE","FGHIJ"]
print(str)"""
	

