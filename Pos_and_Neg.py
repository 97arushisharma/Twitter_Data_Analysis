from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import matplotlib.pyplot as plt
import nltk
import random
import os,json
from textblob import TextBlob



text=[]
output_file=open('test1.txt', 'w')

for filename in os.listdir('/home/charul/code_switching/new/'):
    if filename.endswith(".json"): 
        input_file=open('/home/charul/code_switching/new/'+filename, 'r')
        json_decode=json.load(input_file)
        for item in json_decode:
            my_dict={}
            my_dict['']=item.get('text')
            print(my_dict)
            print(TextBlob(str(my_dict)).sentiment)

        
        '''
        for item in result:
            output_file.write("%s\n" % item)'''
        continue
    else:
        continue
