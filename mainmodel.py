#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:14:23 2018

@author: tonyteng
"""
import math
import tensorflow as tf
tf.reset_default_graph()
import numpy as np
import matplotlib.pyplot as plt
import cv2
from leastsq_value import best_choice_value
from ransac_value import ransac
from ransac_test import ransac_test
######读取图像
T={}
img0=cv2.imread("1.JPG")
T[0]=img0
img1=cv2.imread('2.JPG')
T[1]=img1
img2=cv2.imread('3.JPG')
T[2]=img2
img3=cv2.imread('4.JPG')
T[3]=img3
img4=cv2.imread('5.JPG')
T[4]=img4
img5=cv2.imread('6.JPG')
T[5]=img5
img6=cv2.imread('1.JPG')
T[6]=img6
img7=cv2.imread('1.JPG')
T[7]=img7
img8=cv2.imread('1.JPG')
T[8]=img8
img9=cv2.imread('1.JPG')
T[9]=img9
img10=cv2.imread('1.JPG')
T[10]=img10
#转化为灰度图
for i in range(11):
    T[i]=cv2.cvtColor(T[i],cv2.COLOR_BGR2GRAY)
    T[i]=cv2.resize(T[i],(300,300))

##构造搜索
img0=cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
img0=cv2.resize(img0,(300,300))
    
###寻找突出噪点
t=len(T)
m,n=np.shape(T[0])
W=np.zeros((m,n,t),dtype=int)#存总的遍历矩阵
w=np.zeros((m,n),dtype=int)#存最小二乘输出
w1=np.zeros((m,n),dtype=int)#存RANSAC输出
for s in range(t):
    W[:,:,s]=T[s]
for i in range(m):
    for j in range(n):
        
        ww=[]
        for s in range(1,t):
            ww.append(W[i,j,s])#每次一循环了7遍
        #最小二乘法
        w[i,j]=best_choice_value(ww,1.5)#取100减少1000-1500区域，但是其他区域效果极差
        #RANSAC
        w1[i,j]=ransac(ww)
  #      w1[i, j] = ransac_test(ww,0.7)
    print('已完成：',100*i/m,'%')
            
            
            
#np.save('w0.0015_leastsq.npy',w)
#np.save('w0.015_ransac.npy',w1)
#print('保存成功！')
            
#a=np.load('w0.0015_leastsq.npy')
#a1=np.load('w0.015_ransac.npy')
#a=cv2.resize(a,(302,302))
#imgshow=np.load('1.npy')

#cv2.imshow('hh',a)
#cv2.waitKey(0)
#img1=cv2.imread("IMG_0592.JPG")
#imgshow=cv2.cvtColor(imgshow,cv2.COLOR_BGR2GRAY)
#cv2.imwrite("11.jpg",imgshow)
a=w
a1=w1

a = a.astype(np.uint8)
a1 = a1.astype(np.uint8)
#plt.imshow(a)

#cv2.imwrite('vanished_leastsq.jpg',a)
#cv2.imwrite('vanished_ransac.jpg',a1)
cv2.imwrite('original.jpg',img0)
#cv2.imwrite('p0.7.jpg',a1)
#cv2.imshow('T',a)
#cv2.waitKey(0)

   
        

#cv2.imshow('hh',T[0])
##cv2.waitKey(0)