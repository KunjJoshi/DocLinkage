import pandas as pd
from datasetCreator import datasetCreationFromFolder
from audioVideoProcessor import video_process
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

df=pd.read_csv('fileData.csv')
paths=df['Path']
texts=df['Text']
print(paths, texts)

with open('writed.txt','r') as f:
    text=f.read()

tokens=word_tokenize(text)
tags=pos_tag(tokens)
print(tags)




