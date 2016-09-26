import json
import csv
from nltk import FreqDist
from nltk import word_tokenize

# set working directory
wd = "/Users/brycedietrich/Desktop/"

# load JSON file
file_name = wd + "lexis.json"
with open(file_name) as json_data:
    d = json.load(json_data)

# create word list
word_list = []
for key, value in d.items():
    if value.get('clean_text2') is not None:
        article_words = word_tokenize(value.get('clean_text2'))
        article_words_frequency = FreqDist(article_words)
        article_word_list = list(article_words_frequency)
        word_list = word_list + article_word_list
word_list = set(word_list)

# create csv
with open(wd + 'lexis_dtm.csv', 'a') as my_csv:
    data_writer = csv.writer(my_csv)
    data_writer.writerow(word_list)

# create freq list
for key, value in d.items():
    if value.get('clean_text2') is not None:
        article_words = word_tokenize(value.get('clean_text2'))
        article_words_frequency = FreqDist(article_words)
        article_freq_list = []
        for word in word_list:
            article_freq_list.append(article_words_frequency[word])

        with open(wd + 'lexis_dtm.csv', 'a') as my_csv:
            data_writer = csv.writer(my_csv)
            data_writer.writerow(article_freq_list)
