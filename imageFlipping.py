# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 17:36:24 2023

@author: Prathvish Shetty
"""

#flipping the image
from PIL import Image
#opening the image
img=Image.open(r"C:\Users\Prathvish Shetty\Downloads\pexels-anh-nguyen-17785487.jpg")
transposedImg=img.transpose(Image.FLIP_LEFT_RIGHT)
#Save it to a file in human understandable format
transposedImg.save("CorrectedImg.jpg")
print("Flipping done")