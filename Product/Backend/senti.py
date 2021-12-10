# %reload_ext watermark
# %watermark -v -p numpy,pandas,torch,transformers
from transformers import BertTokenizer,BertModel
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
PRE_TRAINED_MODEL_NAME = 'C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/sentimodel/'
tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)
# tokenizer.save_pretrained('C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/sentimodel')
def bert(transcript,filename):
    tokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)
    class_names = ['negative', 'neutral','positive']

    class SentiTeam44(nn.Module):

        def __init__(self, n_classes):
            super(SentiTeam44, self).__init__()
            self.bert = BertModel.from_pretrained('bert-base-cased')
            self.drop = nn.Dropout(p=0.3)
            self.out = nn.Linear(self.bert.config.hidden_size, n_classes)
        def forward(self, input_ids, attention_mask):
            pooled_output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
            )[1]
            output = self.drop(pooled_output)
            return self.out(output)

    dp_model = SentiTeam44(len(class_names))
    dp_model.load_state_dict(torch.load("C:/Users/Dell/Desktop/notes/sem6/Capstone/UI/sentimodel/best_model_state_10k.bin",map_location=torch.device('cpu')))
    dp_model = dp_model

    encoded_review = tokenizer.encode_plus(
    transcript,
    max_length=512,
    add_special_tokens=True,
    return_token_type_ids=False,
    pad_to_max_length=True,
    return_attention_mask=True,
    return_tensors='pt',
    )

    input_ids = encoded_review['input_ids']
    attention_mask = encoded_review['attention_mask']
    output = dp_model(input_ids, attention_mask)
    pr = torch.sigmoid(output)
    pred=str(pr)[9:31]
    predout=list(map(float,pred.split(",")))
    print(predout)
    print("Negative : "+str((predout[0]/sum(predout))*100))
    print("Neutral : "+str((predout[1]/sum(predout))*100))
    print("Positive : "+str((predout[2]/sum(predout))*100))
    _, prediction = torch.max(output, dim=1)
    print(output)
    print(f'Review text: {transcript}')
    print(f'Sentiment  : {class_names[prediction]}')
    sentivalues = [str((predout[0]/sum(predout))*100),str((predout[1]/sum(predout))*100),str((predout[2]/sum(predout))*100)]
    plt.figure(figsize=(5,5))
    plt.pie(sentivalues, labels=class_names,autopct="%1.1f%%",colors = ["#ff9999", "#66b3ff", "#99ff99"],shadow=True) 
    url = 'static\\piecharts\\'+filename+'.png'
    #plt.show()
    plt.savefig(url)
    plt.close()
    return class_names[prediction]