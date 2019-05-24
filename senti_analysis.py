# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 02:00:30 2018

@author: Shashank Gupta
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as ss
nltk.downloader.download('vader_lexicon')
file='data.xlsx'      #File loaded
xl=pd.ExcelFile(file) # Read From excel
dfs=xl.parse(xl.sheet_names[0]) #parsing  excel sheet to dataframe
dfs=list(dfs['Shashank Gupta']) #removes the blank rows from dataframe
print(dfs)
sid=ss()
month=":"
for data in dfs:
    a = data.find(month)
    if(a==-1):
        s=sid.polarity_scores(data)
        print(data)
        for k in s:
            print(k,s[k])