#!/usr/local/bin/python3


def Naive_Matcher(FILE, TEMPL) : 
	s = 0
	count = 0
	n = len(FILE)
	m = len(TEMPL)
	for i in range (s, n-m+1) :
		if TEMPL[0:m] == FILE[i:i+m] :
			print("template is moved :", i, sep='\t')
			count+=1
	return count
	

FILE = "ABCDEFHGABCJHDUFABCF"
TEMPL = "ABC"
print(TEMPL[0])

print(TEMPL[0:2])

print(Naive_Matcher(FILE, TEMPL))


# wrzucanie do tablicy jednowymiarowej tekstu z pliku 

"""FILE = [i for i in open("TRIAL.txt","r").read() if i!=' ' if i!='\n']
TEMPL = ["e","l","o"]
print (FILE)
print (Naive_Matcher(FILE, TEMPL))"""
		
