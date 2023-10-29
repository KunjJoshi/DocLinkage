import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
import pandas as pd

def preprocess_text(text):
    stop_words=set(stopwords.words('english'))
    word_tokens=word_tokenize(text)
    filtered_words=[word for word in word_tokens if word.lower() not in stop_words]
    puncstr="~`_-!@#$%^&*()+={}[]|\\:;\"'<>,.?/"
    puncless_words=[word for word in filtered_words if word.lower() not in puncstr]     
    return " ".join(puncless_words)
def getroots(word, postag):
    lemmatizer=WordNetLemmatizer()
    lemtags=['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP','RB', 'RBR', 'RBS', 'VB', 'VBP', 'VBD', 'VBG', 'VBN', 'VBZ']
    if postag in lemtags:
        if postag[0]=="J":
            lemac='a'
        elif postag[0]=="N":
            lemac='n'
        elif postag[0]=="R":
            lemac='r'
        elif postag[0]=="V":
            lemac='v'
        return lemmatizer.lemmatize(word, lemac)
    else:
        return word

