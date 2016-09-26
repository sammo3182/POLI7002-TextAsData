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
wd = "/Users/brycedietrich/Desktop/"

html_path = wd + 'lexis.html'
html_file = codecs.open(html_path, encoding='utf-8')
soup = BeautifulSoup(html_file, 'html.parser')

d = {}
key_count = 0

# get date
date_data = soup.find_all('div', class_='c3')
for date in date_data:
    key_count += 1
    d[str(key_count)] = {}
    d[str(key_count)]['date'] = date.find_all('span')[0].get_text()

# get title
title_data = soup.find_all('span', class_='c6')
key_count = 0
for title in title_data:
    key_count += 1
    d[str(key_count)]['title'] = title.get_text()

# get byline
byline_data = soup.find_all('p', class_='c5')
key_count = 0
for byline in byline_data:
    if len(byline.find_all('span', class_='c7')) > 0:
        if "LENGTH:" in byline.find_all('span', class_='c7')[0].get_text():
            key_count += 1
            d[str(key_count)]['byline'] = ''
        if "BYLINE:" in byline.find_all('span', class_='c7')[0].get_text():
            d[str(key_count)]['byline'] = byline.find_all('span', class_='c2')[0].get_text()

# get text
text_data = soup.find_all('div', class_='c4')
key_count = 0
for text in text_data:
    if len(text.find_all('p', class_='c8')) > 0:
        key_count += 1
        article = ''
        for line in text.find_all('p', class_='c8'):
            article += line.get_text()
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
