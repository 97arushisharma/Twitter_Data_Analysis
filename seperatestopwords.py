import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from matplotlib import pyplot as plt
#from mpl_toolkits.basemap import Basemap

#example_sent="Hey there! I am new to NLTK and python programming. Hope you can help me."

file_content = open("/home/arushi/Desktop/files/python nltk/dataindia.txt").read()
tokens = nltk.word_tokenize(file_content)

#print(sent_tokenize(example_sent))

#print(word_tokenize(example_sent))

#for i in word_tokenize(example_sent):
#	print(i)

stop_words1=set(stopwords.words("english"))
stop_words2=set(stopwords.words("hindi"))
x=stop_words1.union(stop_words2)

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

#print(stop_words)
#words= word_tokenize(example_sent);

filtered=[]
for w in tokens:
	if w not in x:
		with open("testindia.txt", "a") as myfile:
			myfile.write("%s , " %w)
			filtered.append(w)
			
myfile=open("testindia.txt","r")


'''def word_count():
    counts = dict()
    
    for line in myfile:
        for word in line.split():
        	if word in counts:
        		counts[word] += 1
        	else:
        		counts[word] = 1

    return counts'''
left=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
common={}
f = nltk.FreqDist(filtered)
common = f.most_common(15)
print(common)
key=[]
value=[]
for l in range(0,15):
	key.append(common[l][0])
	value.append(common[l][1])


#print( word_count())
plt.bar(left, value,tick_label=key, width=0.3, color=['red','black'])

# naming the x-axis
plt.xlabel('most frequent words from tweets')
# naming the y-axis
plt.ylabel('no. of times they appeared')
# plot title
plt.title('twitter data analysis')
 
# function to show the plot
plt.show()

#filtered_sent.append(w)
#print (w)
