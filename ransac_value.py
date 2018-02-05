#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:04:10 2018

@author: tonyteng
"""

import numpy as np
import random 
import math
from sklearn.metrics import mean_squared_error


#a=[3,3,4,5,6,2,1,4,2,3,3,3,3,3,4,6,7,3,2,4,3,55,-10]
#t=[3,3,4,5,6,2,1,4,2,3,3,3,3,3,4,6,7,3,2,4,3,55,-10]

def func(p,x):
    k,b=p
    return k*x+b

def error(p,x,y):
    return func(p,x)-y

def kb_original(y):#x为index，y为真实值
    x1=1
    x2=2
    y1=y[0]
    y2=y[1]
    k=(y2-y1)
    b=y1-k*x1
    return k,b


def dist_x(t,p):##t为一个点（x，y）
    x1=t[0]
    y1=t[1]
    k,b=p
    return (abs(y1-k*x1-b))*math.cos(math.atan(abs(k)))



def ransac(data,dist=0.001,bestfit=0.6,eps=1e-8,p=0.7):
    #p代表算法有结果的概率
    #计算迭代次数k=log(1-p)/log(1-w^n)
    w=bestfit
    k=(math.log(1-p))/(math.log(1-w**len(data)))
    k=math.floor(k)
    max_inliers=math.floor(bestfit*len(data))
    for i in range(k):
        random.shuffle(data)
#        y_original=(data[0],data[1])
        output=[]
        output.append(data[0])
        output.append(data[1])
        kb_1st=kb_original(output)
        for j in range(2,len(data)):
            if abs(func(kb_1st,j)-data[j])<=dist:   ##判定点是否在1st直线附近
                output.append((data[j]))
                #删除多余元素
            while len(output)>max_inliers & len(output)>1:
                output.remove(max(output))
        #calculate error use 标准差
        eps_cal=np.std(output,ddof=1)
        if eps_cal<eps:
            break
    return sum(output)/len(output)





        
        
        
        
        
        
    