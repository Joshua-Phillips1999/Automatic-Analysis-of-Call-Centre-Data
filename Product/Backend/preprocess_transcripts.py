import re 
import nltk 
from gingerit.gingerit import GingerIt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def stopwordremoval(transcript):
    #nltk.download('stopwords')
    #nltk.download('punkt')
    #set of stopwords
    stop_words=set(stopwords.words('english'))
    stop_words.add("im")
    stop_words.add("'s")
    stop_words.add("'ll")
    return(' '.join([j for j in transcript.split() if j not in stop_words]))
    
def spelling_correction(transcript):
    return(' '.join([GingerIt().parse(j)['result'] for j in transcript.split()]))
    
def stemming(transcript):
    nltk.download('wordnet')
    from nltk.stem.porter import PorterStemmer 
    from nltk.stem.wordnet import WordNetLemmatizer

    ps = PorterStemmer()
    lem = WordNetLemmatizer()
    
    return(' '.join([ps.stem(j) for j in transcript.split()]))