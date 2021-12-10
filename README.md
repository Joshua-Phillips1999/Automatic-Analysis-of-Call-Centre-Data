# Automatic-Analysis-of-Call-Centre-Data

Call centers have been the first point of contact between an organization and it’s valuable clients. The centers consists of a large number of ”customer service executives”, whose role is to attend to customers and provide support. Customer satisfaction is a very important metric within the call center. Due to the large volume of calls, it is impossible for a Quality control manager to listen to each call to check if the required quality benchmarks are maintained within the call center. The proposed system would help automate this process by flagging calls that do not meet the pre-defined benchmarks. In this paper, we identify the different kinds of analysis that can be done on such audio data, mainly silence detection, keyword analysis, sentiment analysis and emotion analysis and explore the various mechanisms to implement these modules. By using a variety of data, both generic and call center specific, we inspected different modules best suited for the different modules of our system. We scouted for an offline Speech-to-Text engine to transcribe the audio data, where out of the models VOSK, DeepSpeech, CMU Sphinx and Wav2Vec, we found that Wav2Vec gave better WER and worked best with different dialects as well. We also proceeded to explore TextBlob, VADER, BERTweet and a BERT trained model to detect sentiment, where the BERT trained model performed best. An emotion model was trained by using features of the audio like frequency, pitch and timbre, which gave an overall accuracy of 70.83%. These modules were integrated to form a system, which could automatically analyse various calls in a call center. So, rather than a manager going through every call, an automated model would perform similar functions. This would prove to be a more diligent and efficient option.

## Links to Datasets used 

Indic TTS: https://www.iitm.ac.in/donlab/tts/database.php

Call Center Sample files from Magellan Solutions: https://www.magellan-solutions.com/resources/sample-recordings/

Restaurant Reviews from YELP: https://www.kaggle.com/omkarsabnis/yelp-reviews-dataset

RAVDESS: https://zenodo.org/record/1188976#.YbNlpr1BzIU

CREMA-D: https://www.tensorflow.org/datasets/catalog/crema_d

## Steps to Use

1. Install all the libraries and run the files from Sentiment folder in order to create your Sentiment Model (GPU is required for computation).
2. Install all the libraries and run the files in Emotional folder in order to create your Emotional Model.
3. Go to Product folder and connect to the database and run trial.py
4. On home page upload your audio file and wait a while, once the different models have finished running the Dashboard page will open showing the results.
5. You can view a summarized view of your past audio files as well on the VoiceLogger page
6. Voila! You're done :)


