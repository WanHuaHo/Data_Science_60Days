#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 22:24:24 2021

@author: hewanhua
"""

import numpy as np

# show the correct module and version
print('module :', np)
print('version :', np.__version__)


# Q1:請問下列兩種將 Array 轉換成 List 的方式有何不同？
print('\n', '-'*10, 'Q1', '-'*10)
a = np.arange(30).reshape(5, 6)
print('a_Matrix :\n')
print(a)

# list(a) 只會把第一層的元素轉換成 List，多層的話只有第一層會轉
print('\n單層或多層矩陣中，list(a)只能將第一層的元素轉換成 List')
print('list(a) :', list(a))

# tolist() 能達成多層的型態轉換
print('\ntolist() 能達成多層的型態轉換')
print('tolist() :', a.tolist())


# Q2：請試著在程式中印出以下三個 NdArray 的屬性並且解釋結果？
print('\n', '-'*10, 'Q2', '-'*10)
a = np.random.randint(10, size = 6)
print("a = np.random.randint(10, size=6)")
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(len(a))
print(type(a))

b = np.random.randint(10, size = (3, 4))
print("\nb = np.random.randint(10, size = (3,4))")
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)
print(b.itemsize)
print(len(b))
print(type(b))

c = np.random.randint(10, size = (2, 3, 2))
print("\nc = np.random.randint(10, size = (2, 3, 2))")
print(c)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)
print(c.itemsize)
print(len(c))
print(type(c))


# Q3：如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
print('\n', '-'*10, 'Q3', '-'*10)

a = np.random.randint(10, size=6) 
print("a = np.random.randint(10, size=6)")
print(a.tolist())
print(list(a))

b = np.random.randint(10, size=(3,4)) 
print("\nb = np.random.randint(10, size = (3,4))")
print(b.tolist())
print(list(b))

c = np.random.randint(10, size=(2,3,2)) 
print("\nc = np.random.randint(10, size = (2, 3, 2))")
print(c.tolist())
print(list(c))

# definition for list()
def list(matrix):
    return matrix.tolist()
print('with a new definition for list() :')
print('a\n', list(a))
print('b\n', list(b))
print('c\n', list(c))









