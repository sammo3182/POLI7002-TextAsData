import json
import csv
from nltk import FreqDist
from nltk import word_tokenize

# set working directory
wd = "./"

# load JSON file
file_name = wd + "trump.json"
with open(file_name) as json_data:
    d = json.load(json_data)

# create word list
word_list = [] # default, empty list
for key, value in d.items():
    if value.get('clean_text') is not None: 
    # to get rid of empty article (the one becoming empty after tokenization)
        article_words = word_tokenize(value.get('clean_text'))
        article_words_frequency = FreqDist(article_words)
        article_word_list = list(article_words_frequency)
        word_list = word_list + article_word_list
#word_list = [x.encode("utf-8", "ignore") for x in word_list]
word_list = set(word_list) # get the unique elemement of the list

# create csv
with open(wd + 'trump_dtm.csv', 'a', encoding='utf-8') as my_csv:
    # the encoding part is very important for Chinese systems.
    data_writer = csv.writer(my_csv)
    data_writer.writerow(word_list)

# create freq list
for key, value in d.items():
    if value.get('clean_text') is not None:
        article_words = word_tokenize(value.get('clean_text'))
        article_words_frequency = FreqDist(article_words)
        article_freq_list = []
        for word in word_list:
            article_freq_list.append(article_words_frequency[word])

        with open(wd + 'trump_dtm.csv', 'a') as my_csv:
            data_writer = csv.writer(my_csv)
            data_writer.writerow(article_freq_list)
