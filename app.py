from flask import Flask, render_template, request
from documentsimilarity import document_similarity
from docprocess import documentprocess
from datasetCreator import datasetCreationFromFile
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index',methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/find-similar', methods=['POST'])
def find_similar():
  file=request.files['filename']
  print(file)
  filename=os.path.join('tempMedia', file.filename)
  file.save(filename)
  outputres=document_similarity(filename)
  print(outputres)
  os.remove(filename)
  return render_template("graph.html",results=outputres, filename=file.filename)

@app.route('/add-to-database', methods=['POST'])
def upload_file():
  file=request.files['uploadfile']
  print(file)
  docloc=os.path.join('documents_data',file.filename)
  file.save(docloc)
  try:
    datasetCreationFromFile(docloc, 'fileData.csv')
    message={'msg':'File Upload Successful'}
  except:
    message={'msg':'File Upload Failed'}
  return render_template('index.html', msg=message)

@app.route('/view-common', methods=['POST'])
def view_common():
  commondata=request.form['content']
  #print(commondata)
  purelist=[]
  commondata=commondata.split(',')
  #print(commondata)
  for data in commondata:
    datitem=''
    for item in data:
      if item not in "'[]":
        datitem=datitem+item
    purelist.append(datitem)
  #print(purelist)
  filename=request.form['filepath']
  score=request.form['score']
  ogfile=request.form['ogfile']
  return render_template('common-data.html',commondata=purelist, file=filename, ogfile=ogfile, score=score)













if __name__ == '__main__':
  app.run(host='0.0.0.0',port='5000',debug=True)

