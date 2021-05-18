#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:34:41 2021

@author: hewanhua
"""
import numpy as np
#name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
#sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
#weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
#rank_list = [8,1,5,4,7,6,2,3]
#myopia_list = [True,True,False,False,True,True,False,False]

#1. 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array
# 並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
print('Q1')
dt = np.dtype({'names':('Name', 'sex', 'weight', 'rank', 'myopia'), 
               'formats':('U3', 'U3', float, int, bool)})
c = np.zeros(8, dtype=dt)
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

c['Name'] = name_list
c['sex'] = sex_list
c['weight'] = weight_list
c['rank'] = rank_list
c['myopia'] = myopia_list
print(c)

#2. 呈上題，將array中體重(weight)數據集取出算出全部平均體重
print('\nQ2')
Ave_weight = sum(c['weight'])/c['weight'].size
print('Ave_weight = ', Ave_weight)

#3. 呈上題，進一步算出男生(sex欄位是boy)平均體重、女生(sex欄位是girl)平均體重
print('\nQ3')
Boy = 0
Girl = 0
NB = 0
NG = 0
for ii in range(8):
    if c['sex'][ii] == 'boy':
        Boy = Boy + c['weight'][ii]
        NB = NB + 1
    elif c['sex'][ii] == 'gir':   
        Girl = Girl + c['weight'][ii]
        NG = NG + 1
Boy_Ave = Boy/NB
Girl_Ave = Girl/NG
print('Boy_Ave = ', Boy_Ave)
print('Girl_Ave = ', Girl_Ave)


