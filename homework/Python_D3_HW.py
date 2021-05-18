#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 10:55:31 2021

@author: hewanhua
"""

import numpy as np

# 1.請比較 np.zeros 和 np.empty 產生出來的陣列有何差異？為什麼要設計兩種方法？
print('Q1')
print(np.zeros((2, 3)))
print(np.empty((2, 3)))
# np.zeros 是建立元素全為0的陣列
# np.empty 是建立給定形狀的陣列，元素值則會隨機給定。

# 2.在不用「整數亂數方法」的限制下，如何將包含小數的轉換整數？
# 請將給定的 a 陣列當中的元素變成去掉小數變成整數。
print('\nQ2')
a = np.random.rand(2, 3)
print(a)
for ii in range (2):
    for jj in range(3):
        a[ii, jj] = int(a[ii,jj])
print(a)        
    
# 3.承上題，怎樣可以限制整數的範圍介於 m - n 之間？
# 請將給定的 a 陣列當中的元素的範圍調整成 m - n 之間
from numpy.random import default_rng
rng = default_rng()
print('\nQ3')
m = 20
n = 40
a = np.random.randint(m,n,size=(2,3))
print(a)