# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 18:43:47 2023

@author: Prathvish Shetty
"""
#punjab is located in india as grey color and india as black
import scipy.misc
from PIL import Image
import numpy as np
import random

img=scipy.misc.imread("map-01.png")
count_pun=0
count_in=0
count=0
while(count<=100000):
    x=random.randint(0,2735)#x-vertical
    y=random.randint(0,2480)#y-horizontal
    #dimensions are reversed in python
    #x is depth y is length
    #as image is 2d there is no need of z-dimension
    z=0
    if(img[x][y][z]==60):
        count_in=count_in+1
        count+=1
    elif(img[x][y][z]==80):
        count_pun+=1
        count+=1
area_pun=(count_pun/count_in)*3287263
print(area_pun)
#area will be approximately close to real one