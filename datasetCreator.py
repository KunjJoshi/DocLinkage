import pandas as pd
from audioVideoProcessor import audio_process, video_process
from imageProcessor import image_processing
from pdfProcess import processpdf
from docsProcess import processText
import os

def datasetCreationFromFolder(datafolder,outputcsv):
    print(os.listdir(datafolder))
    files=[f"{datafolder}/{filename}" for filename in os.listdir(datafolder)]
    try:
        df=pd.read_csv(outputcsv)
    except:
        df=pd.DataFrame({"Path":[],"Text":[]})
    for file in files:
        extension=file.split('.')[-1]
        print(extension)
        if extension=='jpg' or extension=='jpeg' or extension=='png' or extension=='tiff':
            print(f"{file} processing")
            imageText=image_processing(file)
            new_row={'Path':[file], 'Text':[imageText]}
            row=pd.DataFrame(new_row)
            df=pd.concat([df,row], axis=0)
            print(f"{file} processed")
        elif extension=='txt':
            print(f"{file} processing")
            docText=processText(file)
            new_row={'Path':[file], 'Text':[docText]}
            row=pd.DataFrame(new_row)
            df=pd.concat([df,row], axis=0)
            print(f"{file} processed")
        elif extension=="pdf":
            print(f"{file} processing")
            pdfText=processpdf(file)
            new_row={'Path':[file], 'Text':[str(pdfText)]}
            row=pd.DataFrame(new_row)
            print(row)
            df=pd.concat([df,row], axis=0)
            print(f"{file} processed")
        elif extension=="mp4":
            print(f"{file} processing")
            vidText=video_process(file)
            new_row={'Path':[file], 'Text':[vidText]}
            row=pd.DataFrame(new_row)
            df=pd.concat([df,row], axis=0)
            print(f"{file} processed")
        elif extension=="wav" or extension=="mp3":
            print(f"{file} processing")
            audText=audio_process(file)
            new_row={'Path':[file], 'Text':[audText]}
            row=pd.DataFrame(new_row)
            df=pd.concat([df,row], axis=0)
            print(f"{file} processed")
        else:
            print(f"{file} skipped")
    df.to_csv(outputcsv, index=False)


def datasetCreationFromFile(file, outputcsv):
    try:
        df=pd.read_csv(outputcsv)
    except:
        df=pd.DataFrame({"Path":[],"Text":[]})
    extension=file.split('.')[-1]
    print(extension)
    if extension=='jpg' or extension=='jpeg' or extension=='png' or extension=='tiff':
        print(f"{file} processing")
        imageText=image_processing(file)
        new_row={'Path':[file], 'Text':[imageText]}
        row=pd.DataFrame(new_row)
        df=pd.concat([df,row], axis=0)
        print(f"{file} processed")
    elif extension=='txt':
        print(f"{file} processing")
        docText=processText(file)
        new_row={'Path':[file], 'Text':[docText]}
        row=pd.DataFrame(new_row)
        df=pd.concat([df,row], axis=0)
        print(f"{file} processed")
    elif extension=="pdf":
        print(f"{file} processing")
        pdfText=processpdf(file)
        new_row={'Path':[file], 'Text':[str(pdfText)]}
        row=pd.DataFrame(new_row)
        print(row)
        df=pd.concat([df,row], axis=0)
        print(f"{file} processed")
    elif extension=="mp4":
        print(f"{file} processing")
        vidText=video_process(file)
        new_row={'Path':[file], 'Text':[vidText]}
        row=pd.DataFrame(new_row)
        df=pd.concat([df,row], axis=0)
        print(f"{file} processed")
    elif extension=="wav" or extension=="mp3":
        print(f"{file} processing")
        audText=audio_process(file)
        new_row={'Path':[file], 'Text':[audText]}
        row=pd.DataFrame(new_row)
        df=pd.concat([df,row], axis=0)
        print(f"{file} processed")
    else:
        print(f"{file} skipped")
    df.to_csv(outputcsv, index=False)

