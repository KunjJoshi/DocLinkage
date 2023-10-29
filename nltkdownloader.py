import nltk
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

model_name="jonatasgrosman/wav2vec2-large-xlsr-53-english"
model=Wav2Vec2ForCTC.from_pretrained(model_name)
processor=Wav2Vec2Processor.from_pretrained(model_name)

nltk.download('words')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')