import fitz
import pandas as pd
from textblob import TextBlob

def get_pdf_text(pdf_path):
  pdftext=[]
  pdf=fitz.open(pdf_path)
  for pageno in range(len(pdf)):
    page=pdf.load_page(pageno)
    text=page.get_text("blocks")
    for block in text:
     pdftext.append(block)
  #print(pdftext)
  return pdftext



def create_pdf_text(textlist):
  textstring=""
  for t in list(textlist):
    #print(t)
    text=t[4]
    textstring=textstring+text
  return textstring




def autocorrect(text):
  correct_text=TextBlob(text).correct()
  correct_text=str(correct_text)
  return correct_text

def rempunc(text):
  puncstr="~`!@#$%^&*()_-+=}{[]:;|\\\"'<>,./?\n\t"
  for punc in puncstr:
    numpunc=text.count(punc)
    for i in range(numpunc):
      text=text.replace(punc,'')
  return text
def processpdf(pdf_path):
  textlist=get_pdf_text(pdf_path)
  wholetext=create_pdf_text(textlist)
  #corrected_text=rempunc(wholetext)
  #print(corrected_text)
  return wholetext