# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 13:05:17 2018

@author: Ayush
"""

import turtle
t=turtle.Pen()
a=20
for k in range(5):
    for i in range(6):
        for j in range(4):
            t.forward(a)
            t.left(90)
        t.right(60)
    a=a*2
t.done()