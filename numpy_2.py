# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:43:46 2019

@author: ThinkPad
"""
#numpy数组基本操作
import numpy as np

#数组属性
np.random.seed(0)#使每次生成的随机数不变

a=np.random.random((2,3,3))
print(a,'\n')

print('dim:',a.ndim)#维度
print('shape:',a.shape)#各维度大小
print('size:',a.size)#数组总大小
print('type:',a.dtype)#数据类型


#数组索引：获取单个数组(同列表索引操作)
print(a[0][0][0],a[0][0][1])
b=np.array([1,2,3,4,5])
print('\n',b[2],b[-1])


#数组切片
#获取方式：x[start,stop,step]
#一维数组：x1
x1=np.arange(10)
print('\n',x1)
print(x1[:5],x1[6:],x1[2:5],x1[1::2],x1[::-1])

x2=np.random.random((3,4))
print(x2,'\n')
print(x2[:2,:3],'\n',x2[:2,2])

#获取某行某列
print(x2[:,1])

#获取数组切片视图和副本
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)

b_st=b[:2,:2]
b_fb=b[:2,:2].copy()
print(b_st,'\n',b_fb,'\n')

b_st[0][0]=9
print(b)
b_fb[0][0]=4
print(b)

#数组的变形
c=b.reshape((1,9))
print(c)
d=b.reshape((9,1))
print(d)

#拼接和分裂
#拼接
#np.concatenate()
#np.vstack()
#np.hstack()

#分裂
#np.split()
#np.vsplit()
#np.hsplit()









