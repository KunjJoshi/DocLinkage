import easyocr
from PIL import Image
import pandas as pd
from textblob import TextBlob
import pytesseract
from PIL import Image

def get_image_text(image_path):
  image=Image.open(image_path)
  fulltext=pytesseract.image_to_string(image)
  return fulltext



def image_processing(image_path):
  img_text=get_image_text(image_path)
  return img_text
