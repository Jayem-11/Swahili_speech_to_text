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