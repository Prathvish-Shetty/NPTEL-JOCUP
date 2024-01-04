# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:12:10 2023

@author: Prathvish Shetty
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file=r"C:\Users\Prathvish Shetty\.spyder-py3\PyPrograms\fbsentimentanalysis.xlsx"
try:
    df = pd.read_excel(file, engine='openpyxl')
except ValueError:
    # If 'openpyxl' doesn't work, try 'xlrd'
    df = pd.read_excel(file, engine='xlrd')
xl=pd.ExcelFile(file)
dfs=xl.parse(xl.sheet_names[0])#parsing excel sheet into data frame
#dfs=list(dfs['Timeline'])-->remove blank rows from dataframe
print(dfs)
'''
str1="UTC+05:30"
for data in dfs:
    a=data.find(str1)
    if a==-1:
        ss=sid.plarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])
'''
            
sentiment_scores = []
sid=SentimentIntensityAnalyzer()
for data in dfs:
    ss=sid.polarity_scores(data)
    print(data)
    for k in ss:
        print(k,ss[k])
        
