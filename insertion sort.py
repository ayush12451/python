# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 09:36:06 2018

@author: Ayush
"""
#insertion sort

a = [16, 19, 11, 15, 10, 12, 14]


for i in range(len(a)):
    j = i

    while j>0:

        if a[j-1] > a[j]:
            temp=a[j-1]
            a[j-1]=a[j]
            a[j]=temp
       
        j = j-1
print (a)