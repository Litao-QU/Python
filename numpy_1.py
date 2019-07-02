# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:39:53 2019

@author: ThinkPad
"""

#Numpy创建数组的两种方式
import numpy as np

#1从列表生成数组
a=np.array([1,2,3,4,5])
#如果数组中类型不同则向上转换
b=np.array([1.0,2,3,4,5])
print(a,b,'\n')

#用dtype关键字可设置数组数据类型
c=np.array([1,2,3,4,5],dtype='float32')
print(c,'\n')

#用列表的列表初始多维数组
d=np.array([[1,2,3],[4,5,6],[7,8,9]])
#嵌套列表构成的多维数组
e=np.array([range(i,i+3) for i in [2,4,6]])
print(d)
print(e,'\n')

#2从头创建数组
#f=np.zeros(10,dtype='int8')
f=np.zeros((3,4),dtype='int8')
print(f,'\n')

g=np.ones((3,2),dtype='int8')
print(g,'\n')

h=np.full((2,2),2.33)
print(h,'\n')
#np.arange类似python中的range函数
j=np.arange(0,10,2)
print(j,'\n')

#(0,1)均匀分布的随机数组
l=np.random.random((3,3))
print(l,'\n')

#均值为0，标准差为1的正太分布数组
p=np.random.normal(0,1,(2,2))
print(p,'\n')

#[0,10)区间内的随机整型数组
q=np.random.randint(0,10,(3,3))
print(q,'\n')

#创建n阶单位矩阵
w=np.eye(4,dtype='int')
print(w,'\n')






