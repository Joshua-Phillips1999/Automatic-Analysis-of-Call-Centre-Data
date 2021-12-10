import librosa
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import librosa.display
import os
import glob
import audio_metadata
from pydub import AudioSegment,silence
from MediaInfo import MediaInfo
import operator
import re
import nltk
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

'''
####For now, assumption is that we're only taking .wav files
####To convert to .wav:
def convertToWav(filename):
	os.system(f"""ffmpeg -i {file} -acodec pcm_u8 -ar 22050 audio/{file[:-4]}.wav""")
    
####We need ffmpeg, ffplay, ffprobe in the working directory. 
'''

def getAudioDetails(filename):
    metadata = audio_metadata.load(filename)
    return(metadata)
    
def waveform(filename):
    data, sampling_rate = librosa.load("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/static/audio/"+filename, sr=16000)
    plt.title(filename)
    plt.figure(figsize=(12,4))
    librosa.display.waveplot(data, sampling_rate,color='black')
    url = "C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/static/images/"+filename+'.png'
    print("AUDIO DESC: ",url)
    plt.savefig(url)
    plt.close()
    #return(url)
    
def silences(filename):
    myaudio = intro = AudioSegment.from_wav(filename)
    dBFS=myaudio.dBFS

    fileduration = len(intro)/60000
    #print(type(myaudio))
    silence_interval = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=dBFS-16)

    silence_interval_2 = [((start/1000),(stop/1000)) for start,stop in silence_interval] #in sec

    total=0
    totalthres=0
    threshold=5
    thresholdarray=[]
    #print("\n------silence interval------")
    for i in silence_interval_2:
        print(i)
        total+=i[1]-i[0]
        if((i[1]-i[0])>threshold):
            totalthres+=i[1]-i[0]
            thresholdarray.append(i)

    print("\n------total silence------")
    print(total)
    print("\n------total silence after threshold------")
    print(totalthres)
    print("\n------silence interval after threshold------")
    print(thresholdarray)
    print("\n\n")
    return([silence_interval_2,total,totalthres,thresholdarray])
    
    