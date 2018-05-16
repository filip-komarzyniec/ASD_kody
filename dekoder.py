#!/usr/local/bin/python3

import hashlib

name = input("write your name without polish letter, starting from the big one : ")

code =""
for i in name : 
	code+=str(ord(i))

	
print (code)

print("your code is : ",hashlib.md5(code.encode('utf-8')).hexdigest(), sep='\t')