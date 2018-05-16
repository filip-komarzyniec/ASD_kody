#!/usr/local/bin/python3 

import time

def CcharF(FILE) :	#liczę rozmiar linii w tablicy
	N=0
	for lines in FILE :
		N = len(lines)
	return N

def Krab2D (FILE, TEMPL) :			# definicja Karp-Rabin algorithm 
	m = len(TEMPL)
	n = CcharF(FILE)
	LINES = sum(1 for lines in FILE)	# liczba linii w FILE
	d = 16
	q = 101
	p, ts, p2, ts2, count = 0, 0, 0, 0, 0
	h = (d**(m-1))%q
	for i in range (0, m) :					# liczę hashe dla TEMPL
		p = (d*p + ord(TEMPL[0][i]))%q
		p2 = (d*p2 + ord(TEMPL[i][0]))%q
	for i in range(0, n-m+1) :				# przechodzę w kolumnie
		for j in range(0, LINES-2) :			# przechodzę w wierszu
			if j == 0:
				ts2 = 0
				for M in range(0,m) :			# liczę początkowy hash dla kolumny 
					ts2 = (d*ts2 + ord(FILE[M][i]))%q
				if ts2 == p2 :
					#print(j,i, sep=' ')
					#print("HELLO", ts2, end=' ')
					for k in range(0,m) :		# liczę hash poziomy -> coś mega skopane, liczy na 0 zawsze
						ts = (d*ts + ord(FILE[0][i+k]))%q
					#print(ts)
					if ts == p :
						if TEMPL[0][0:m] == FILE[0][i:i+m] and TEMPL[1][0] == FILE[1][i] and TEMPL[2][0] == FILE[2][i] :
							#print("template is moved :", i, sep='\t')
							count+=1
			if j < LINES-3 and j!=0 :
				ts = 0
				#print (G)
				ts2 = (d*(ts2 - ord(FILE[j-1][i])*h) + ord(FILE[j+2][i]))%q		#rolluję hash poziomy w dół
				if ts2 == p2 :
					#print(j,i, sep=' ')
					#print("HELLO", ts2, end=' ')
					for k in range(0,m) :
						ts = (d*ts + ord(FILE[j][i+k]))%q
					#print(ts, end=' ')
					if ts == p :
						#print(j,i,sep=' ')
						#print(FILE[j][i:i+m], FILE[j+1][i], FILE[j+2][i], sep=' ')
						if TEMPL[0][0:m] == FILE[j][i:i+m] and TEMPL[1][0] == FILE[j+1][i] and TEMPL[2][0] == FILE[j+2][i] :
							POI = (j+1)*n - (n-i)
							#print("template is moved :", POI, sep='\t')
							count+=1
			if j == LINES-3  :
				ts = 0
				ts2 = (d*(ts2 - ord(FILE[j-1][i])*h) + ord(FILE[j+2][i]))%q
				if ts2 == p2 :
					#print(ts2)
					for k in range(0,m) :
						ts = ts = (d*ts + ord(FILE[j][i+k]))%q
					#print(ts)
					if ts == p:
						if TEMPL[0][0:m] == FILE[j][i:i+m] and TEMPL[1][0] == FILE[j+1][i] and TEMPL[2][0] == FILE[j+2][i] :
							POI = (j+1)*n - (n-i)
							#print("template is moved :", POI, sep='\t')
							count+=1
	return "template number is: " + '\t'+ str(count)
							
				


TEMPL = ['ABC','B','C']
# PROBA = ['ABC', 'BAC', 'KOT','CAP','KRA','GAR','TOL']
"""for M in range(0,3) :
	for L in range(1,4) :
		G = L + 3
		#print(PROBA[G][M], end='')"""
		
with open("1000_pattern.txt","r") as f :
	f = f.readlines()					#zapisuję linie do listy				
	FILE = [lines.strip('\n') for lines in f]
ts = 0
for i in range(4,7) :
	ts = (16*ts + ord(FILE[0][i]))%51
#print(ts)
	
#print("n równe :",CcharF(FILE))

t1 = time.time()
print(Krab2D(FILE, TEMPL))
t2 = time.time()
print("overall time is :", t2-t1, sep='\t')
#print()

