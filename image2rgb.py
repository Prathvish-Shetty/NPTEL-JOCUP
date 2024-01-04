# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 18:33:44 2023

@author: Prathvish Shetty
"""

from PIL import Image
im=Image.open("test1.png")
rgb_im=im.convert('RGB')
r,g,b=rgb_im.getpixel((150,1))#x and y coordinates
print(r,g,b)