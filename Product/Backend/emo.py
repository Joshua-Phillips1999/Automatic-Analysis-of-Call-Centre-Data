import librosa
import soundfile
import os, glob, pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from pydub import AudioSegment
import mutagen
from mutagen.wave import WAVE

def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
        result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
    return result

x_call=[]

def emotion(filename):
    audio=WAVE(filename)
    audio_info=audio.info
    length=int(audio_info.length)
    feature=extract_feature(filename, mfcc=True, chroma=True, mel=True)
    x_call.append(feature)
    loaded_model = pickle.load(open("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/emomodel/mlp_classifier.model", 'rb'))
    result = loaded_model.predict(x_call)
    return(result[0])
    #return (" ".join(result))


