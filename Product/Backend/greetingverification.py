from difflib import get_close_matches

def greeting_verification(transcript,greetings,perc=0.25):
    wordlist = transcript.strip().split()
    if(len(wordlist)!=0):
        nw = int(perc*len(wordlist)) + 1
        verificationList = wordlist[0:nw]
        
        verificationdict = dict()
        for i in greetings:
          verificationdict[i]=0

        c=0
        detectedwords = []
        for i in greetings:
            closest = get_close_matches(i, verificationList,cutoff=0.7)  #closeMatches(startlist,i)
            #print(i,closest)
            if(len(closest)>0):
                c+=1
                detectedwords.append(i)
                verificationdict[i]+=1

        '''
        for i in names:
          if(verificationdict[i]==0):
            if(len(get_close_matches(i,verificationlist,cutoff=0.5))>0):
                print(get_close_matches(i,verificationlist,cutoff=0.5))
                c+=1
                verificationdict[i]+=1
        '''
        return(c/len(greetings)*100 , detectedwords)