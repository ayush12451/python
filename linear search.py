# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 22:29:49 2018

@author: Ayush
"""

a=[1,4,2,5,6,3,9,10,0]


x=int(input("enter element to search"))
for i in range(0,len(a)):
    if(a[i]==x):
        print "element fount at position",i+1