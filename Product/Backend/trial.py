from flask import Flask, render_template

import librosa
import matplotlib.pyplot as plt
import librosa.display
import os
import glob
import audio_metadata
from pydub import AudioSegment,silence

from MediaInfo import MediaInfo
import requests
import operator
import re
import nltk

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import audiofiledescp as audsc
from senti import *
from stt import *
from emo import * 
from preprocess_transcripts import *
from greetingverification import *
from frequencyanalysis import *

app = Flask(__name__)

import sqlite3

con=sqlite3.connect("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/data.db",check_same_thread=False)

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("one.html")

@app.route("/dashboard",methods=['GET','POST'])
def dashb():
    if request.method == 'POST':
        f = request.files['audiofile']
        f.save("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/static/audio/"+f.filename)
        sound = AudioSegment.from_wav("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/static/audio/"+f.filename)
        sound = sound.set_channels(1)
        sound.export("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/static/audio/"+f.filename, format="wav")
        #f.save("static/audio/"+f.filename)
        #f.save(os.path.join("static/audio", f.filename))
        #f.save("C:/Users/hp/Desktop/Capstone/static/audio/"+f.filename)
        
        ######Emotional
        emotionalvalue = emotion("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/static/audio/"+f.filename).upper()
        metadata = audsc.getAudioDetails("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/static/audio/"+f.filename)
        
        ########Waveplot
        audsc.waveform(f.filename)
        img_url = "images/"+f.filename+".png" 
        
        #######Silence
        s =  audsc.silences("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/static/audio/"+f.filename) #silence_intervals,total,totalthres,thresholdarray =
        s.append(len(s[3]))

        ######STT
        transcript = STT("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/static/audio/"+f.filename)
        #transcript="vnjfnaji njdsnja nwvidnrv nsajdnf"

        #####keyword
        swr = stopwordremoval(transcript)
        #sp = spelling_correction(transcript)
        st = stemming(transcript)
        greetings=['hello','welcome','company','hi','hey','morning','evening','afternoon','good','kids','by']
        gv = greeting_verification(transcript.lower(),greetings)
        fw = frequent_words(transcript,f.filename)
        print(fw)
        url_freq="freq/"+f.filename+".png"
        url_cloud="cloud/"+f.filename+".png"

        ######Sentiment
        sentiment = bert(transcript,f.filename).upper()
        url_pie = "piecharts/"+f.filename+".png"
        

        


        cur = con.cursor()
        cur.execute("INSERT INTO voicelogs(FileName,FileDur,Total_Silence,No_of_Frequent_Words,Sentiment,Emotion) VALUES (?,?,?,?,?,?)", (f.filename,metadata['streaminfo']['duration'],s[2],len(fw),sentiment,emotionalvalue))
        cur.execute("SELECT * FROM voicelogs")
        con.commit()
        #con.close()

    return render_template("index.html",url_cloud=url_cloud,url_freq=url_freq,greeting=gv, freqword=fw, emoval=emotionalvalue,sentiment = sentiment, url_pie = url_pie, filename = f.filename, url=img_url, metadata=metadata , silences = s,transcript = transcript) 



@app.route("/voicelogger",methods=['GET','POST'])
def voicelog():
    cur = con.cursor()
    cursor = cur.execute('SELECT * FROM voicelogs')
    items = cursor.fetchall()
    #return render_template('print_items.html', items=items)
    print(items)
    return render_template("voicelogger.html", items=items)




print("DB")
if __name__ == "__main__":
    app.run(debug=True)

