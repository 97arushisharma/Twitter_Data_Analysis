#!/usr/bin/python
from operator import itemgetter
import sys



current_word = None
#current_count = 0
word = None
text = '"screen_name":'

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word = line.split('\t')

    for sent in word:
        if text in sent:
            print(sent)

    



