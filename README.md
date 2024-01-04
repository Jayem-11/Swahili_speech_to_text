<<<<<<< HEAD
# INSTRUCTIONS
## Loading model from hugging face

## Libraries to install
!pip install --upgrade datasets accelerate
!pip install transformers jiwer evaluate

## Imports
from transformers import WhisperForConditionalGeneration, WhisperProcessor
from transformers import WhisperFeatureExtractor, WhisperTokenizer

## Feature_extractor
feature_extractor = WhisperFeatureExtractor.from_pretrained("openai/whisper-small")

## Tokenizer
tokenizer = WhisperTokenizer.from_pretrained("openai/whisper-small", language="Swahili", task="transcribe")

## Processor
processor = WhisperProcessor.from_pretrained("/content/drive/MyDrive/mozilla_hackathon/whisper-small")

## Model
model = WhisperForConditionalGeneration.from_pretrained("/content/drive/MyDrive/mozilla_hackathon/whisper-small")
forced_decoder_ids = processor.get_decoder_prompt_ids(language="sw", task="transcribe")
=======
# Swahili Speech to text

Finetuning whisper-small for sahili speech to text.

![car](https://github.com/Jayem-11/Used_Car_Prices/blob/main/car.jpg)
photo credits: [Pixabay](http://pixabay.com/)  

## Description: 
This project uses the [small version of Whisper](https://huggingface.co/openai/whisper-small), a general-purpose speech recognition model created by OpenAI, to convert Swahili audio to text. Whisper is pretrained for ASR (Automatic speech Recognition) and speech translation on 680k hours of labelled data

## Author
- Github [@JM_Rono](https://github.com/Jayem-11)
- Linked_in [@John Michael Rono](https://www.linkedin.com/in/john-michael-rono-26a2b6183/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BGItpY4FbT0mUzd4XQz%2FwxQ%3D%3D)

## Table of Contents
[A Data](#dt) <br>
[B Machine learning](#ml) <br>
[C Deploying](#dp) <br>

## Tech Stack
- Beautiful soup
- Power BI
- PostgreSQL
- Scikit-learn
- Tensorflow
- Keras
- Streamlit

## Design

![Design](https://github.com/Jayem-11/Used_Car_Prices/blob/main/design.jpg)


## <span id="dt">A. Data </span>
>>>>>>> e57a8c60e4c29c418abb59a8edbf97136daacceb
