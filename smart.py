# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:17:10 2020

@author: HASEE
"""


#import the libraries
import numpy as np
import pandas as pd
#read the dataset
dataset=pd.read_csv(r"D:\python\train.csv")
#text cleaning
import re 
import nltk
#remove stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords
#stemming 
from nltk.stem.porter import PorterStemmer
ps =PorterStemmer()
#remove punctuation and numbers
data=[]
for i in range(0,5970): 
     tweet=dataset["Tweet"][i]
     tweet=re.sub('[0-9]',' ',tweet)
     tweet=re.sub('[.]',' ',tweet)
     tweet=re.sub('[,]',' ',tweet)
     tweet=re.sub('[?]',' ',tweet)
     tweet=tweet.lower()
     tweet=tweet.split()
     tweet=[ps.stem(word) for word in tweet if not word in set(stopwords.words('english'))]
     tweet=' '.join(tweet)
     data.append(tweet)