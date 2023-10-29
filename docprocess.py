from audioVideoProcessor import audio_process, video_process
from imageProcessor import image_processing
from pdfProcess import processpdf
from docsProcess import processText

def documentprocess(doc):
        extension=doc.split('.')[-1]
        print(extension)
        if extension=='jpg' or extension=='jpeg' or extension=='png' or extension=='tiff':
            print(f"{doc} processing")
            imageText=image_processing(doc)
            return imageText
        elif extension=='txt':
            print(f"{doc} processing")
            docText=processText(doc)
            return docText
        elif extension=="pdf":
            print(f"{doc} processing")
            pdfText=processpdf(doc)
            return pdfText
        elif extension=="mp4":
            print(f"{doc} processing")
            vidText=video_process(doc)
            return vidText
        elif extension=="wav" or extension=="mp3":
            print(f"{doc} processing")
            audText=audio_process(doc)
            return audText
        else:
             return "File Skipped"