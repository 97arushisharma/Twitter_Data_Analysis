import json, os, random
import nltk
import matplotlib.pyplot as plt 

from nltk.corpus import stopwords
from nltk.corpus import twitter_samples
from nltk.tokenize import word_tokenize, sent_tokenize
from pprint import pprint
#from docx import Document





result=[]
output_file=open('neg-pos.txt', 'w')

for filename in os.listdir('/home/arushi/Desktop/files/python nltk/tweets/india/'):
    if filename.endswith(".json"): 
        input_file=open('/home/arushi/Desktop/files/python nltk/tweets/india/'+filename, 'r')
        json_decode=json.load(input_file)
        for item in json_decode:
        	my_dict={}
        	my_dict['']=item.get('text')
        	result.append(my_dict)

        
        '''
        for item in result:
        	output_file.write("%s\n" % item)'''
        continue
    else:
        continue


#random.shuffle(result)

#output_file.write("%s\n" % result)	#form of list

stop_word_hin = set(stopwords.words("hindi"))
stop_word_eng = set(stopwords.words("english"))

x = stop_word_eng.union(stop_word_hin)
x.add('}')
x.add('{')
x.add('?')
x.add('”')
x.add('“')
x.add(':')
x.add('RT')
x.add('\'RT')
x.add('@')
x.add('!')
x.add('#')
x.add('$')
x.add('%')
x.add('^')
x.add('&')
x.add('*')
x.add('(')
x.add(')')
x.add('/')
x.add(']')
x.add('[')
x.add(',')
x.add('.')
x.add(';')
x.add('-')
x.add('+')
x.add('=')
x.add('\'')
x.add('\'' +'\'')
x.add('`'+'`')
x.add('~')
x.add('https')
x.add('’')
x.add('I')
x.add('\'s')
x.add('...')
x.add('n\'t')
x.add('…')
string = "\\n\\n"
string2 = "\\n"
x.add(string)
x.add(string2)


#print(stop_word)



#most common

words = word_tokenize(str(result))

#output_file.write("%s\n" % words)

filtered = []
all_words = []
common = []

for w in words:
  if w not in x:
     filtered.append(w)

#print(filtered)

for wrds in filtered:
       all_words.append(wrds.lower())


#output_file.write("%s\n" % all_words)      

all_words = nltk.FreqDist(all_words)

common = all_words.most_common(10)

cmn_wrds = []
wrds_count = []

for i in range(0,10):
      cmn_wrds.append(common[i][0])
      wrds_count.append(common[i][1])


#print(cmn_wrds)
#print(wrds_count)	
#common_words= list(all_words.keys())[:10] 
#count = list(all_words.values())[:10]

#print(common[1].key())
#print(common.values())


left = [1,2,3,4,5,6,7,8,9,10]


#plt.bar(left, wrds_count, tick_label = cmn_wrds, width = 0.5, color = ['red', 'blue'])
#plt.show()






#sentimental analysis
k = len(result)
print("Total tweets : ")
print(k)

hin_pos = []
hin_neg = []
eng_pos = []
eng_neg = []

pos_hin = open('/home/arushi/Desktop/files/python nltk/pos')
neg_hin = open('/home/arushi/Desktop/files/python nltk/neg')
pos_eng = open('/home/arushi/Desktop/files/python nltk/pos1')
neg_eng = open('/home/arushi/Desktop/files/python nltk/neg1')

hin_pos = pos_hin.read().split()
hin_neg = neg_hin.read().split()
eng_pos = pos_eng.read().split()
eng_neg = neg_eng.read().split()


xpos = hin_pos + eng_pos
random.shuffle(xpos)
xneg = hin_neg + eng_neg
random.shuffle(xneg)


poscount = 0
negcount = 0
neutral = 0

for j in range (0, k):

	count = 0
	

	strng = str(result[j])

	wordx = word_tokenize(strng)
	
	for words in wordx:
		if words in xpos:
			count = count + 1

		if words in xneg:
			count = count - 1

	
	if(count > 0):
		poscount = poscount + 1
	
	if(count < 0):
		negcount = negcount + 1

	if(count == 0):
		neutral = neutral + 1
    		



print("Positive tweets : ")
print(poscount)
print("Negative tweets : ")
print(negcount)
print("Neutral tweets : ")
print(neutral)    
	
	




'''
count = 0

for words in filtered:
	if words in xpos:
		count = count + 1

	if words in xneg:
		count = count - 1

		
#print(count)
'''    




