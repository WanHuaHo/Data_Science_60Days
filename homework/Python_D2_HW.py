#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 08:37:29 2021

@author: hewanhua
"""

import numpy as np
print(np)
print(np.__version__)

# 基礎題
# 1. 請問 type(...) 跟 a.dtype 這兩個語法有什麼不同？
print('Q1')
a = np.arange(15).reshape(3, 5)
print('a', '\n', a)
print('type(a) : ', type(a))
print('a.dtype : ', a.dtype)
# type(a) 是得到a的型態
# a.dtype 是得到a陣列中的資料型態

# 2. 請撰寫一個判斷a的元素是否等於指定資料型態的函式
print('\nQ2')
def a_type(a, T):
    return a.dtype is np.dtype(T)
a = np.arange(15)
print(a_type(a,np.dtype('int64')))

# 3. 承上題，請判斷下列三種寫法為何不正確？
print('\nQ3')
print('type(a) : ', type(a))
print('a.dtype : ', a.dtype)

def is_dtype(a, t):
    return a.dtype is t
print(is_dtype(a, 'int64'))
# is 是強比較，必須要所有規格都相同，包含是哪一種物件
# 使用 is 的話就必須要跟 np.dtype 物件來相比。

def is_dtype(a, t):
    return type(a) == np.dtype(t)
print(is_dtype(a, np.int64))

def is_dtype(a, t):
    return type(a) is np.dtype(t)
print(is_dtype(a, 'int64'))
# type(a) 是得到a的型態
# a.dtype 是得到a陣列中的資料型態
# 上述兩者不同，因此return必定為False


