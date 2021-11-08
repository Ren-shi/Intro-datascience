# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:44:11 2021

@author: Brenden
TME match calculation using the residual
"""
TME1 = 0.2125
TME2 = 0.2126
r1= -12
r2 = 3

rdiff = abs(abs(r1) - abs(r2))
TMEdiff = abs(TME1-TME2)
step = rdiff

print(step)

if r1 < r2:
    move = abs(r1)
else:
    move = abs(r2)
count = 0
print(move)
while (move < 0.09): 
    move = move-step
    count =+1
    if count == 10:
        break
print(move,count)