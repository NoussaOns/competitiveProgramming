# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 00:11:48 2019

@author: Noussa
"""

a = input()

x = []

for i in a:
    if i not in x:
        x.append(i)

if (len(x) % 2 == 0):
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')