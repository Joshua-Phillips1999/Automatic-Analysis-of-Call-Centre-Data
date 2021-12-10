from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from wordcloud import WordCloud

def frequent_words(transcript,filename):
    #f = dict()
    w = transcript.split()
    #w = ['evil', 'hello', 'hi', 'look', 'shell', 'non', 'fit', 'mishel', 'name', 'cat', 'call', 'behalf', 'squar', 'bit', 'dot', 'com', 'got', 'thank', 'much', 'ok', 'call', 'first', 'name', 'Ye', 'may', 'thank', 'michel', 'go', 'ask', 'complet', 'address', 'object', 'put', 'account', 'want', 'right', 'ask', 'jip', 'cot', 'nine', 'eight', 'six', 'six', 'three', 'nine', 'eight', 'six', 'six', 'three', 'saran', 'safe', 'pay', 'vancouv', 'washington', 'right', 'far', 'go', 'custom', 'mishelton', 'twenti', 'thirti', 'fort', 'fifti', 'mile', 'thrifti', 'mile', 'fifti', 'mile', 'toon', 'tan', 'Lo', 'problem', 'e-mail', 'address', 'go', 'send', 'inform', 'wide', 'e', 'nail', 'address', 'So', 'host', 'oath', 'sorri', 'repeat', 'name', 'k', 'old', 'name', 'tot', 'last', 'name', 'includ', 'right', 'Ye', 'yahoo', 'dot', 'com', 'k', 'procedur', 'tori', 'realign', 'yo', 'verifi', 'wright', 'plea', 'bear', 'would', 'letter', 'mari', 'e', 'india', 'c', 'charli', 'h', 'harri', 'e', 'Co', 'elfelima', 'El', 'lima', 'e', 'echo', 'h', 'harri', 'oscar', 'x', 'x', 'ray', 'x', 'sam', 'india', 'e', 'echo', 'yahoo', 'dot', 'com', 'get', 'correctli', 'Ye', 'wonder', 'thank', 'promo', 'go', 'ahead', 'provid', 'temporari', 'user', 'name', 'password', 'plea', 'bare', 'uncl', 'ant', 'michel', 'aha', 'secur', 'question', 'choo', 'time', 'okay', 'secur', 'question', 'grandmoth', 'maiden', 'name', 'foot', 'sen', 'answer', 'k', 'oka', 'right', 'custom', 'option', 'servic', 'provid', 'would', 'want', 'wait', 'one', 'two', 'two', 'highest', 'one', 'five', 'five', 'highest', 'one', 'five', 'one', 'two', 'five', 'right', 'anda', 'servic', 'categori', 'option', 'put', 'To', 'three', 'categori', 'depend', 'mania', 'servic', 'It', 'put', 'categori', 'pet', 'care', 'servic', 'provid', 'mean', 'anim', 'ah', 'dog', 'sit', 'hou', 'sit', 'saw', 'odin', 'craig', 'list', 'mention', 'provid', 'servic', 'pet', 'sit', 'correct', 'hosieri', 'Ye', 'well', 'reason', 'call', 'network', 'custom', 'vancouv', 'interest', 'servic', 'done', 'saw', 'ad', 'survey', 'would', 'want', 'provid', 'hou', 'clean', 'hou', 'sit', 'elderli', 'york', 'york', 'sicko', 'goti', 'ate', 'ass', 'oh', 'ka', 'wonder', 'thesof', 'clean', 'servic', 'interior', 'interior', 'exterior', 'exterior', 'exterior', 'lawn', 'Al', 'wart', 'two', 'categori', 'pastor', 'lawn', 'glean', 'servic', 'busi', 'name', 'oh', 'kick', 'Iv', 'put', 'name', 'like', 'michel', 'dog', 'hou', 'sitter', 'k', 'IL', 'kit', 'ear', 'alreadi', 'bet', 'night', 'ka', 'perfectli', 'fine', 'busi', 'summari', 'go', 'ahead', 'copi', 'past', 'current', 'crake', 'list', 'k', 'one', 'num', 'edit', 'han', 'full', 'access', 'account', 'busi', 'lichen', 'insur', 'bund', 'yet', 'natur', 'problem', 'give', 'second', 'michal', 'deer', 'go', 'congratul', 'michal', 'exist', 'account', 'squar', 'biddand', 'tea', 'maxim', 'free', 'busi', 'profil', 'given', 'option', 'put', 'pictur', 'ibu', 'logo', 'crete', 'uniqu', 'busi', 'summari', 'need', 'help', 'assist', 'quick', 'contact', 'option', 'home', 'page', 'wadsik', 'send', 'us', 'e-mail', 'support', 'squar', 'bit', 'dot', 'com', 'one', 'way', 'gent', 'lot', 'work', 'busi', 'go', 'ill', 'send', 'everyth', 'male', 'includ', 'temporari', 'use', 'name', 'password', 'direct', 'wobbl', 'web', 'side', 'refer', 'would', 'like', 'get', 'york', 'name', 'password', 'would', 'rather', 'wait', 'e-mail', 'year', 'would', 'like', 'hear', 'k', 'pen', 'paper', 'radio', 'Ye', 'k', 'Ru', 'user', 'name', 'user', 'name', 'go', 'first', 'name', 'shall', 'small', 'mete', 'kan', 'small', 'mal', 'ah', 'ok', 'best', 'word', 'go', 'michel', 'zero', 'one', 'first', 'letter', 'carpet', 'first', 'letter', 'galway', 'carpet', 'ok', 'michel', 'zero', 'one', 'first', 'letter', 'carpet', 'ok', 'know', 'busi', 'help', 'opt', 'custom', 'look', 'dog', 'hou', 'fitter', 'would', 'like', 'connect', 'custom', 'area', 'go', 'cost', 'michel', 'sure', 'ok', 'agr', 'simpl', 'ok', 'right', 'use', 'name', 'password', 'cure', 'bug', 'site', 'would', 'squar', 'bit', 'squar', 'bit', 'dot', 'com', 'ill', 'send', 'e-mail', 'fora', 'bear', 'squar', 'bid', 'last', 'letter', 'tea', 'dog', 'right', 'ill', 'go', 'ahead', 'send', 'mal', 'plea', 'check', 'box', 'see', 'check', 'span', 'mal', 'right', 'k', 'k', 'thank', 'michel', 'posit', 'adscribei', 'tot', 'come', 'help', 'grow', 'busi', 'tori', 'rest', 'day', 'thank', 'euro', 'man', 'whew', 'sign', 'perform', 'web', 'side', 'tripoli', 'w', 'dot', 'squar', 'bit', 'dot', 'com', 'allow', 'sign', 'start', 'receiv', 'regular', 'e-mail', 'us', 'let', 'know', 'servic', 'request', 'k', 'choo', 'decid', 'interest', 'go', 'ahead', 'grow', 'ill', 'grab', 'servic', 'request', 'go', 'ahead', 'ignor', 'e-mail', 'ok', 'happen', 'front', 'comput', 'also', 'check', 'bat', 'side', 'eomer', 'sorri', 'happen', 'front', 'comper', 'Ye', 'ill', 'park', 'grate', 'yo', 'go', 'ahead', 'check', 'west', 'side', 'see', 'look', 'like', 'go', 'squar', 'bit', 'squar', 'bit', 'dot', 'com', 'world', 'spell', 'andsesac', 'infinli', 'consid', 'k', 'perfectli', 'fine', 'go', 'ahead', 'crete', 'free', 'account', 'michel', 'provid', 'temporari', 'use', 'name', 'temporari', 'password', 'send', 'e-mail', 'go', 'ahead', 'costum', 'convent', 'time', 'arriv', 'ok', 'k', 'michel', 'tire', 'five', 'gent', 'question', 'ask', 'busi', 'relat', 'ask', 'person', 'inform', 'would', 'mind', 'provid', 'last', 'name', 'k', 'Ye', 'last', 'name', 'would', 'coxi', 'h', 'f', 'e', 'h', 'Xe', 'Li', 'f', 'e', 'one']
    count = Counter(w)
    l = []
    for j in count:
        if(count[j]<2):
            l.append(j)
    [count.pop(k) for k in l]
    #print(count,w,l)
    
    if(len(l)>0):
        #plt.rcParams["figure.figsize"] = (12, 8)
        plt.figure(figsize=(12,5))
        x = count.keys()
        y = count.values()
        plt.bar(x,y,color='darkgray')
        ax = plt.gca()
        plt.draw()
        ax.tick_params(axis='x', labelrotation = 45)
        url = 'static\\freq\\'+filename+'.png'
        plt.savefig(url)
        plt.close()
        


#convert list to string and generate
        #unique_string=(" ").join(my_list)
        wordcloud = WordCloud().generate(transcript)
        plt.figure(figsize=(15,5))
        plt.imshow(wordcloud)
        plt.axis("off")
        url = 'static\\cloud\\'+filename+'.png'
        plt.savefig(url, bbox_inches='tight')
        #plt.show()
        plt.close()
    return count.keys()