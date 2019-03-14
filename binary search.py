# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 13:10:06 2018

@author: Ayush
"""

a=[]

x=int(input("enter the lenght of list:\t"))

for i in range(0,x):
    a.append(int(input("enter element")))
 
b=int(input("enter element to search"))    
    
for j in range(0,x):
    for i in range(0,x-1):
        if(a[i]>a[i+1]):
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
        
beg=0
end=x
found=0

while(found==0):
    mid=(beg+end)//2
    if(a[mid]==b):
        found=1
    elif(a[mid]<b):
        beg=mid
    elif(a[mid]>b):
        end=mid

if (found==1):
    print "element found at position", mid