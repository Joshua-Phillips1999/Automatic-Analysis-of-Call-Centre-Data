import librosa
import torch
import os
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import mutagen
from mutagen.wave import WAVE
def STT(filename):
	audio = WAVE(filename)
#contains all the metadata about the wavpack file
	audio_info = audio.info
	length = int(audio_info.length)
	tokenizer = Wav2Vec2Tokenizer.from_pretrained("C:/Users/Dell/Desktop/notes/sem6/Capstone/Wav2Vec/models/")
	model = Wav2Vec2ForCTC.from_pretrained("C:/Users/Dell/Desktop/notes/sem6/Capstone/Wav2Vec/models/")
	transcription=[]
	for i in range(0,length,15):
		audio, rate = librosa.load(filename, sr = 16000,duration=15,offset=i)
		input_values = tokenizer(audio, return_tensors = "pt").input_values
		logits = model(input_values).logits
		prediction = torch.argmax(logits, dim = -1)
		transcription.append(tokenizer.batch_decode(prediction)[0])
		print(i,transcription)
	print(transcription)
	return(" ".join(transcription))