import os, json
import pandas as pd
from pprint import pprint

'''with open('/home/arushi/Desktop/files/python nltk/tweets/bts/1517481527.json') as data_file:
	data= json.load(data_file)
pprint(data)'''

result=[]



path_to_json = '/home/arushi/Desktop/files/python nltk/tweets/india/'
json_file = [pos_json for pos_json in os.listdir('/home/arushi/Desktop/files/python nltk/tweets/india/') if pos_json.endswith('.json')]
#print(json_files)  # for me this prints ['foo.json']
output_file=open('dataindia.txt', 'w')
#input_file=open('/home/arushi/Desktop/files/python nltk/tweets/bts/1517481527.json', 'r')
for inputf in json_file:
	input_file=open('/home/arushi/Desktop/files/python nltk/tweets/india/'+inputf, 'r')
	json_decode=json.load(input_file)
	for item in json_decode:
    		my_dict={}
    		my_dict['']=item.get('text')
    	
    		result.append(my_dict)

	for item in result:
  			output_file.write("%s\n" % item)



	print(result) 