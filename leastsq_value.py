#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:16:57 2018

@author: tonyteng
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:17:10 2018

@author: tonyteng
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import math
import random

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

#a=[3,3,4,5,6,2,1,4,2,3,3,3,3,3,4,6,7,3,2,4,3,55,-10]
#t=[3,3,4,5,6,2,1,4,2,3,3,3,3,3,4,6,7,3,2,4,3,55,-10]
#Y=np.array(a)
#X=np.linspace(1,len(Y),len(Y))
#
#y_original=random.sample(a,2)
#p1=kb_original(y_original)
#para=leastsq(error,p1,args=(X,Y))
#k,b=para[0]

#plt.scatter(X,Y,color='red')
#x=np.linspace(1,len(X),len(X))
#y=k*x+b
#plt.plot(x,y,color='orange')
#plt.legend()
#plt.show()

def dist_x(t,p):##t为一个点（x，y）
    x1=t[0]
    y1=t[1]
    k,b=p
    return (abs(y1-k*x1-b))*math.cos(math.atan(abs(k)))

def best_choice_value(a,dist=10):#dist为选择点的阈值
    Y=np.array(a)
    X=np.linspace(1,len(Y),len(Y))
    y_original=random.sample(a,2)
    p1=kb_original(y_original)
    para=leastsq(error,p1,args=(X,Y))
    kb=para[0]
    sumy=0
    t=1e-8
    for i in range(len(X)):
        if dist_x((X[i],Y[i]),kb)<dist:
            t=t+1
            sumy=sumy+Y[i]
           
    return sumy/t
    