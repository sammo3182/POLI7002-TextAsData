#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import csv
import re
import string
from os import listdir
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# working directory
wd = "/Users/brycedietrich/Desktop/"

# list files
speeches = listdir(wd + "capitol_words/house/speeches/104/")

# preprocessing
stopwords = stopwords.words('english')
stemmer = SnowballStemmer('english')

# positive words
with open(wd + 'pos_words.txt') as f:
    positive_words = f.read().splitlines()  # not stemmed

# negative words
with open(wd + 'neg_words.txt') as f:
    negative_words = f.read().splitlines()

# stem dictionaries
positive_words = [stemmer.stem(word) for word in positive_words]
negative_words = [stemmer.stem(word) for word in negative_words]

count = 0
for speech in speeches:
    count += 1
    print(count)

    # get id
    speaker_id = speech.split('_')[0]  # record the congress's ide

    # read speech
    f = open(wd + 'capitol_words/house/speeches/104/' + speech, 'r')
    text = f.read()

    # remove punctuation and capitalization
    text = re.sub('\W', ' ', text.lower())

    # get unigrams
    words = word_tokenize(text)

    # remove stop words
    clean_text = filter(lambda x: x not in stopwords, words)
    clean_text = list(clean_text)

    # apply stemmer
    stemmer = SnowballStemmer('english')
    snowball_words = [stemmer.stem(word) for word in clean_text]

    # word count
    word_count = len(snowball_words)

    # count positive
    pos_count = 0  # default value setting 
    for word in positive_words:
        if word in snowball_words: 
            pos_count += 1

    # count negative
    neg_count = 0
    for word in negative_words:
        if word in snowball_words:
            neg_count += 1

    # append the csv
    with open(wd + 'results.csv', 'a') as my_csv:
        # create row
        row = [speaker_id, speech, pos_count, neg_count, word_count]

        # write the row
        data_writer = csv.writer(my_csv)
        data_writer.writerow(row)
