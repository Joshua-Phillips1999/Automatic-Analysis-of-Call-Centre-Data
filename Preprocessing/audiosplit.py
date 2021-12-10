from pydub import AudioSegment
from pydub.utils import make_chunks
folder="C:/Users/Dell/Downloads/"
filename=".wav"
myaudio = AudioSegment.from_file(folder+filename , "wav") 
chunk_length_ms = 15000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files

for i, chunk in enumerate(chunks):
    chunk_name = filename.split('.')[0]+"{0}.wav".format(i)
    print ("exporting", chunk_name)
    chunk.export(folder+chunk_name, format="wav")
