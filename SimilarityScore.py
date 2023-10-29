from textPreprocess import preprocess_text, getroots
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from docprocess import documentprocess
import pandas as pd
import nltk


def similarityscore(text1, text2):
    similarity_score=0
    english_words=nltk.corpus.words.words()
    common_items=[]
    text1=preprocess_text(str(text1))
    text2=preprocess_text(str(text2))
    words1=word_tokenize(str(text1))
    words2=word_tokenize(str(text2))
    postags1=pos_tag(words1)
    postags2=pos_tag(words2)
    wordlist1=[]
    taglist1=[]
    wordlist2=[]
    taglist2=[]
    for words, tags in postags1:
        wordlist1.append(words.lower())
        taglist1.append(tags)
    for words, tags in postags2:
        wordlist2.append(words.lower())
        taglist2.append(tags)
    if len(wordlist1)>len(wordlist2):
        iterlen=len(wordlist1)
        iterwlist=wordlist1
        itertlist=taglist1
        altwlist=wordlist2
        alttlist=taglist2
    else:
        iterlen=len(wordlist2)
        iterwlist=wordlist2
        itertlist=taglist2
        altwlist=wordlist1
        alttlist=taglist1
    for i in range(len(altwlist)):
        altwlist[i]=getroots(altwlist[i], alttlist[i])
    #print('ALTWLIST MADE')
    for i in range(iterlen):
        #print(similarity_score)
        word=iterwlist[i]
        tag=itertlist[i]
        if "NN" in tag or "JJ" in tag:
            #print('PROPER NOUN ENCOUNTERED')
            if word in altwlist:
                wordind=altwlist.index(word)
                if "NN" in alttlist[wordind] or "JJ" in alttlist[wordind]:
                    similarity_score=similarity_score+1
                    common_items.append(word)
                    #print(word)
                else:
                    similarity_score=similarity_score+0.5
        else:
            root=getroots(word, tag)
            if root in altwlist:
                similarity_score=similarity_score+1
    similarity_ratio=similarity_score/iterlen
    common_items=[word for word in common_items if word.lower() not in english_words]
    return similarity_ratio, list(set(common_items))

df=pd.read_csv('fileData.csv')
texts=list(df['Text'])
text1=texts[0]
text2=texts[1]
print(similarityscore(text1, text2))
