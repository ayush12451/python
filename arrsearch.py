# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 09:08:50 2018

@author: Ayush
"""

a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

x=int(input("enter number of elements:"))
for i in range(0,x):
    a[i]=int(input("enter element"))
b=int(input("enter element to search"))
for j in range(0,x):
    if(a[j]==b):
        print "element found at position",j
        flag=1
if(flag!=1):
    print "element not found"