#!/usr/local/bin/python3

from functions import MSort, filluniqrand
import time 
import random 


class Node:
	def __init__(self,info): #constructor of class
		self.info = info  #information for node
		self.left = None  #left leef
		self.right = None #right leef
		self.level = None #level none defined
 
	def __str__(self):
		return str(self.info) #return as string
 
 
class searchtree:
	def __init__(self): #constructor of class
		self.root = None
		
	def create(self,val):  #create binary search tree nodes
		if self.root == None:
			self.root = Node(val)
		else:
			current = self.root
			while 1:
				if val < current.info:
					if current.left:
						current = current.left
					else:
						current.left = Node(val)
						break;      
				elif val > current.info:
					if current.right:
						current = current.right
					else:
						current.right = Node(val)
						break;      
				else:
					break 
					
	def inorder(self,node):
		if node:              
			self.inorder(node.left)
			print (node.info)
			self.inorder(node.right)
 
	def find(self, node, val):
		if node is None:
			return None
		elif val < node.info:
			return self.find(node.left, val)
		elif val > node.info:
			return self.find(node.right, val)
		else:
			return node.info
 
	def findMin(self,node):
		while (node.left) :
			node = node.left
		return node.info
 
	def findMax(self,node):
		while (node.right) :
			node = node.right
		return node.info
 
	def insert(self, val):
		new_node = Node(val)
		parent = None
		node = self.root
		while (node) :
			parent = node
			if (val > node.info) :
				node = node.right
			else : 
				node = node.left
		new_node.level = parent
		if (not parent): 
			self.root = new_node
		else : 
			if parent.info < val :
				parent.right = new_node 
			else: 
				parent.left = new_node


	def delete(self, node, val):
		temp = None
		if not node :
			return
		elif val < node.info :
			node.left =  self.delete(node.left, val)
		elif val > node.info : 
			node.right = self.delete(node.right, val)
		elif node.right and node.left : 
			temp = self.findMin(node.right)
			node.info = temp.info
			node.right = delete(node.right, val)
		else : 
			temp = node
			if not node.left : 
				node = node.right
			elif not node.right :
				node = node.left
			del temp 
		return node 
		
		









tree = searchtree()     #obiekt klasy searchtree
arr = []
arr = filluniqrand(arr)
for i in range(1,10**6) :
	 if i not in arr :
	 	a = i
	
for i in arr :  		# utworzenie drzewa BST z obiektu klasy searchtree
	tree.insert(i)
	
t0 = time.time()
tree.insert(a)
t01 = time.time() 
tree.inorder(tree.root)
#D = int(input("delete this D : "))
#F = int(input("find this F : " ))
#print(tree.find(tree.root, 7))
print("insertin : ",a)
t1 = time.time()
tree.findMin(tree.root)
t2 = time.time()
tree.findMax(tree.root)
t3 = time.time()
print("deleted : ", tree.delete(tree.root,random.choice(arr)))
t4 = time.time()
tree.find(tree.root, random.choice(arr) )
t5 = time.time()



#dla nieposortowanej tablicy """
print("creating tree time is : ", t01-t0, sep='\t')
print("finding Min time is : ", t2-t1, sep='\t')
print("finding Max time is : : ", t3-t2, sep='\t')
print("deleting node time is : ", t4-t3, sep='\t')
print("finding node time is : ", t5-t4, sep='\t')