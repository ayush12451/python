# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 12:44:13 2018

@author: Ayush
"""

arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
a=int(input("enter size of array"))
for i in range(0,a):
    arr[i]=int(input("enter element"))


for i in range(0,a):
    for j in range(0,a-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print arr[:a]