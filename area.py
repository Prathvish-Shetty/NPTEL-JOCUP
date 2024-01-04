# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 18:10:04 2023

@author: Prathvish Shetty
"""

import numpy as np
from PIL import Image
width=5
height=4
array=np.zeros([height,width,3],dtype=np.uint8)
img=Image.fromarray(array)
img.save('test.png')
array1=np.zeros([100,200,3],dtype=np.uint8)
array[:,:100]=[225,128,0]#orange
array1[:,100:]=[0,0,225]#blue color
img=Image.fromarray(array1)
img.save('test1.png')
