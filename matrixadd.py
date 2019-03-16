# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:03:19 2018

@author: Ayush
"""

a=[[0,0,0],
   [0,0,0],
   [0,0,0]]

b=[[0,0,0],
   [0,0,0],
   [0,0,0]]

c=[[0,0,0],
   [0,0,0],
   [0,0,0]]

d=[[0,0,0],
   [0,0,0],
   [0,0,0]]

m=[[0,0,0],
   [0,0,0],
   [0,0,0]]

print "enter elements of first matrix:\n"
for i in range(0,3):
    for j in range(0,3):
        print "enter element a[",i+1,",",j+1,"]:"
        a[i][j]=int(input())

print "enter elements of second matrix:\n"
for i in range(0,3):
    for j in range(0,3):
        print "enter element b[",i+1,",",j+1,"]:"
        b[i][j]=int(input())

#addition
for i in range(0,3):
    for j in range(0,3):
        c[i][j]=a[i][j]+b[i][j]

#subtraction
for i in range(0,3):
    for j in range(0,3):
        d[i][j]=a[i][j]-b[i][j]

#multiplication
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            m[i][j]=m[i][j]+a[i][k]*b[k][j]

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            a[i][j]=a[i-1][j]+a[i+1][j]+a[i][j-1]+a[j+1]

print "Sum:\n"
for i in range(0,3):
    for j in range(0,3):
        print c[i][j],
    print "\n"

print "difference:\n"   
for i in range(0,3):
    for j in range(0,3):
        print d[i][j],
    print "\n"

print "product:\n"
for i in range(0,3):
    for j in range(0,3):
        print m[i][j],
    print "\n"
    
print "transpose\n"
for i in range(0,3): 
     for j in range(0,3):
         print a[j][i],
     print "\n"

