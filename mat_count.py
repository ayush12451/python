# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:13:36 2018

@author: Ayush
"""

a=[[0,0,0],
   [0,0,0],
   [0,0,0]]

b=[]
count=[0,0,0,0,0,0,0,0,0]

print "enter elements of matrix:\n"
for i in range(0,3):
    for j in range(0,3):
        a[i][j]=int(input("enter element"))

for i in range(0,3):
    b=b+a[i]

for k in range(0,9):            
    for i in range(0,3):
        for j in range(0,3):
            if(b[k]==a[i][j]):
                count[k]=count[k]+1
                
print "matrix is\n"
for q in a:
    print q
                
for i in range(0,9):
    print "Element ",b[i],"appears ",count[i],"times."
