import pandas as pd
from textblob import TextBlob

def processText(textfile):
  with open(textfile,'r') as f:
    data=f.read()
  data=str(data)
  return data