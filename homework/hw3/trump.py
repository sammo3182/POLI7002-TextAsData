# Title: Homework3_Trump
# Author: Yue Hu
# Environment: Win 10, Python 3.5
# Purpose: The assignment is a project downloading lexisnexis articles about Donald Trump


# import modules
import codecs
import re
import json
import string
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# set working directory
wd = "./hw3/"
#wd = "./"

html_path = wd + 'trump.html'
html_file = codecs.open(html_path, encoding='utf-8') # opent the file
soup = BeautifulSoup(html_file, 'html.parser') # parse with beautiful soup

d = {}  # default dict
key_count = 0 # starting number

# get index: to check the article match later.
key_count = 0
index_data = soup.find_all('div', class_ = 'c0')
for index in index_data:
    if "of 1000 DOCUMENTS" in indiex.find_all('span', class_='c2')[0].get_text():
        key_count += 1
        d[str(key_count)]['index'] = index.find_all('span')[0].get_text()



# get date
date_data = soup.find_all('div', class_='c3') 
# get the data of div on all things class is c3
# be sure typing class_ rather than class
# print(len(date_data))  # check if get all articles' date_data

# print(date_data[0].find_all("span", class_ = "c2")[0].get_text()) 
## try to get the date from the data. 
## be sure using [0] after the find_all

for date in date_data:
    key_count += 1 # starting count from 1, and adding 1 each time
    d[str(key_count)] = {} # embed a dict for each article
    d[str(key_count)]['date'] = date.find_all('span')[0].get_text() 
    # save the text data as a value in a dic


# get title
title_data = soup.find_all('span', class_='c6')
key_count = 0
for title in title_data:
    if len(title.find_all('span', class_= 'c6'))>0:
        temp_title = title.find_all('span', class_='c6')[0].get_text()
    if len(title.find_all('span', class_= 'c7')) != 0:
        if "LENGTH:" in title.find_all('span', class_='c7')[0].get_text():
            key_count += 1
            d[str(key_count)]['title'] = temp_title


# get byline(Problematic)
byline_data = soup.find_all('p', class_='c5') # data including byline, section, etc.
# print(len(byline_data))
key_count = 0
for byline in byline_data:
    if len(byline.find_all('span', class_='c7')) > 0:
        if "LENGTH:" in byline.find_all('span', class_='c7')[0].get_text():
            key_count += 1
            d[str(key_count)]['byline'] = ''
        if "BYLINE:" in byline.find_all('span', class_='c7')[0].get_text():
            print(key_count)
            #d[str(key_count)]['byline'] = byline.find_all('span', class_='c2')[0].get_text()
            


# get text
text_data = soup.find_all('div', class_='c4')
key_count = 0
for text in text_data:
    if len(text.find_all('p', class_='c8')) > 0: # the first element does not have text.
        key_count += 1
        article = '' # empty string
        for line in text.find_all('p', class_='c8'):
            article += line.get_text() # combined lines into a paragraph
        d[str(key_count)]['text'] = article

# preprocessing
original_stopwords = stopwords.words('english')
custom_stopwords = stopwords.words('english')
custom_stopwords.append('&quot;')
custom_stopwords.append('&nbsp;')
custom_stopwords.append('&amp;')

for key in range(1, 100):
    # remove punctuation and capitalization
    article = re.sub('\W', ' ', d[str(key)]['text'].lower())

    # get unigrams
    article_words = word_tokenize(article)

    # remove stop words
    clean_article = filter(lambda x: x not in original_stopwords, article_words)
    clean_article = list(clean_article)

    # apply stemmer
    stemmer = SnowballStemmer('english')
    snowball_words = [stemmer.stem(word) for word in clean_article]

    # print words
    d[str(key)]['clean_text'] = ' '.join(snowball_words)

    # remove custom stop words
    clean_article = filter(lambda x: x not in custom_stopwords, article_words)
    clean_article = list(clean_article)

    # apply stemmer
    stemmer = SnowballStemmer('english')
    snowball_words = [stemmer.stem(word) for word in clean_article]

    # print words
    d[str(key)]['clean_text2'] = ' '.join(snowball_words)


# save the file as a JSON file
file_name = wd + "lexis.json"
with open(file_name, "w") as writeJSON:
    json.dump(d, writeJSON)
