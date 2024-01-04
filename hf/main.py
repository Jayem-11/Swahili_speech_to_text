from fastapi import FastAPI, UploadFile
from moviepy.editor import *
from transformers import AutoTokenizer , AutoModelForSeq2SeqLM , pipeline
from transformers import WhisperForConditionalGeneration, WhisperProcessor
from transformers import WhisperFeatureExtractor, WhisperTokenizer
import librosa
import numpy as np
import torch 



app = FastAPI()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device  

feature_extractor = WhisperFeatureExtractor.from_pretrained("openai/whisper-small")
tokenizer = WhisperTokenizer.from_pretrained("openai/whisper-small", language="Swahili", task="transcribe")
processor = WhisperProcessor.from_pretrained("Jayem-11/whisper-small-swahili-3")
asr_model = WhisperForConditionalGeneration.from_pretrained('Jayem-11/whisper-small-swahili-3')
forced_decoder_ids = processor.get_decoder_prompt_ids(language="sw", task="transcribe")


@app.get("/")
async def read_root():
    return {"Successful"}


def extract_and_resample_audio(file):

    with open('audio.wav', 'wb') as f:
    
        f.write(file)   

    # Load the temporary audio file
    audio_data, sr = librosa.load("audio.wav")

    # Resample the audio to 16000Hz
    audio_resampled = librosa.resample(audio_data, orig_sr = sr, target_sr=16000)
    
    print("Done resampling")

    return audio_resampled

@app.post("/predict")
async def predict(file: UploadFile):
    audio_resampled = extract_and_resample_audio(await file.read())


    input_feats = feature_extractor(audio_resampled, sampling_rate = 16000).input_features[0]


    input_feats = np.expand_dims(input_feats, axis=0)


    input_feats = torch.from_numpy(input_feats)


    output = asr_model.generate(input_features=input_feats.to(device),max_new_tokens=255,).cpu().numpy()


    sample_text = tokenizer.batch_decode(output, skip_special_tokens=True)

    return {'Text': sample_text}