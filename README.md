# Swahili Speech to text

Finetuning whisper-small for swahili speech to text.

![car](https://github.com/Jayem-11/Swahili_speech_to_text/blob/main/sw.jpg)
photo credits: [Devonyu](https://www.istockphoto.com/portfolio/Devonyu?mediatype=photography)  

## Description: 
This project uses the [small version of Whisper](https://huggingface.co/openai/whisper-small), a general-purpose speech recognition model created by OpenAI, to convert Swahili audio to text. Whisper is pretrained for ASR (Automatic speech Recognition) and speech translation on 680k hours of labelled data

## Author
- Github [@JM_Rono](https://github.com/Jayem-11)
- Linked_in [@John Michael Rono](https://www.linkedin.com/in/john-michael-rono-26a2b6183/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BGItpY4FbT0mUzd4XQz%2FwxQ%3D%3D)

## Table of Contents
[A Data](#dt) <br>
[B Machine learning](#ml) <br>
[C Deploying](#dp) <br>

## Design

![Design](https://github.com/Jayem-11/Swahili_speech_to_text/blob/main/workflow.png)


## <span id="dt">A. Data </span>
The data consist of about 82K instances of swahili audio form Mozilla common voice. I got the dataset from participating in a [Zindi competition](https://zindi.africa/competitions/mozilla-foundation-mozilla-common-voice-hackathon-i-nairobi/data). Join the completed competiotion to get acces to the data. 

## <span id="ml">B. Machine Learning </span>

- Check-out notebook:  [@notebook](https://github.com/Jayem-11/Swahili_speech_to_text/blob/main/swahili-whisper-finetuning.ipynb)


### Evaluation
The model had a WER score of 8.365
[wandb](https://api.wandb.ai/links/ronojohnmichael/8bafteyt)

## <span id="dp"> C. Deploying </span>

- Deployed at: https://jayem-11-used-car-prices-main-77qw4p.streamlit.app/

![Jupyter notebook example](https://github.com/Jayem-11/Used_Car_Prices/blob/main/deployed1.png)

## 

- Hit the predict button to input the data to the model. The outcome is as shown below.
![Jupyter notebook example](https://github.com/Jayem-11/Used_Car_Prices/blob/main/deployed2.png)




