# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:50:43 2023

@author: Prathvish Shetty
"""

import csv
from gmplot import gmplot

'''
with open("sample.csv",'r') as f:
    reader=csv.reader(f)
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        print(lat)
        print(long)
        print(" ",lat+long)
'''

gmap=gmplot.GoogleMapPlotter(18.5136, 73.8552,17)
gmap.coloricon="http://www.googlemapsmarkers.com/v1/009900/"
with open("sample.csv",'r') as f:
    reader=csv.reader(f)
    k=0
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        if k==0:
            gmap.marker(lat,long,"yellow")
            k=1
        else:
            gmap.marker(lat,long,"blue")
gmap.marker(lat,long,"red")
gmap.draw("mymap.html")
        