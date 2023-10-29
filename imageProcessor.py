import easyocr
from PIL import Image
import pandas as pd
from textblob import TextBlob

def get_image_text(image_path):
  reader=easyocr.Reader(['en'], gpu=True)
  text=reader.readtext(image_path)
  fulltext=''
  for t in text:
    t=list(t)
    fulltext=fulltext+t[1].lower()+ ' '
  return fulltext

def autocorrect(txt):
  correct_text=TextBlob(txt).correct()
  correct_text=str(correct_text)
  return correct_text


def image_processing(image_path):
  img_text=get_image_text(image_path)
  corrected_text=autocorrect(img_text)
  return corrected_text
