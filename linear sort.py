# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 22:29:49 2018

@author: Ayush
"""

a=[1,4,2,5,6,3,9,10,0]

for j in range(0,len(a)):
    for i in range(0,len(a)-1):
        if(a[i]>a[i+1]):
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
x=int(input("enter element to search"))
for i in range(0,len(a)):
    if(a[i]==x):
        print "element fount at position",i