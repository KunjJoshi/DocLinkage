from docprocess import documentprocess
from SimilarityScore import similarityscore
import pandas as pd

def document_similarity(filepath):
    allres=[]
    filetext=documentprocess(filepath)
    print(f"Text On File: {filetext}")
    try:
     df=pd.read_csv('fileData.csv')
    except:
       df=pd.DataFrame({"Path":[],"Text":[]})
    allpaths=list(df['Path'])
    alltexts=list(df['Text'])
    for i in range(len(alltexts)):
        text1=filetext
        text2=alltexts[i]
        simscore, commoncontent=similarityscore(text1, text2)
        resdict={}
        resdict['score']=simscore
        resdict['content']=commoncontent
        allpaths[i]=str(allpaths[i])
        numslashes=allpaths[i].count('\\')
        for slashes in range(numslashes):
           allpaths[i]=allpaths[i].replace('\\','/')
        resdict['file']=allpaths[i]
        allres.append(resdict)
    return allres


"""
filepath="TathyaPDF.pdf"
allres=document_similarity(filepath)
print(allres)
"""
