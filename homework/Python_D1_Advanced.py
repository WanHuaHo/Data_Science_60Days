#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 08:58:25 2021

@author: hewanhua
"""

# Q1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
print('-'*5, 'Q1', '-'*5)
print('生成一個等差數列，首數為0，尾數為20，公差為1的數列。')
import numpy as np
L = np.linspace(0, 20, 21, dtype = int)
print('L =', L)

# Q2.呈上題，將以上數列取出偶數。
print('\n', '-'*5, 'Q2', '-'*5)
print('呈上題，將以上數列取出偶數。')
even_list = []
for n in range(22):
    if n % 2 == 0:
        even_list.append(L[n])                
print(even_list)
            
    
# Q3.呈1題，將數列取出3的倍數。
print('\n', '-'*5, 'Q3', '-'*5)
print('呈1題，將數列取出3的倍數。')
T_list = []
for n in range(1, 21):
    if L[n] % 3 == 0:
        T_list.append(L[n])                
print(T_list)