import pandas as pd
from datasetCreator import datasetCreationFromFolder
from audioVideoProcessor import video_process
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

df=pd.read_csv('fileData.csv')
paths=df['Path']
texts=list(df['Text'])


for text in texts:
    tokens=word_tokenize(str(text))
    tags=pos_tag(tokens)
    print(tags)




