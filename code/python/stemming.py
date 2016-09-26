# import modules
import requests
from bs4 import BeautifulSoup
import re
# from nltk import FreqDist
# from nltk import word_tokenize
# from nltk import bigrams
# from nltk import trigrams
# from nltk.corpus import stopwords
# from nltk.stem.porter import *
# from nltk.stem.lancaster import *
# from nltk.stem.snowball import SnowballStemmer
 #from nltk.stem import WordNetLemmatizer

# url
url = 'http://avalon.law.yale.edu/20th_century/mlk01.asp'

# create soup
response = requests.get(url)
contents = response.content
soup = BeautifulSoup(contents, 'html.parser')

# print soup
# get text
speech = " "
lines = soup.find_all('p')
for line in lines:
    speech += line.get_text()

# remove punctuation
speech = re.sub('\W', ' ', speech.lower())
print(speech)

# get text
speech = " "
lines = soup.find_all('p')
# print(type(lines))
print(lines[0].get_text())

for line in lines:
    speech += line.get_text()

# remove punctuation
speech = re.sub('\W', ' ', speech.lower())

# get unigrams
words = word_tokenize(speech.lower())
words_frequency = FreqDist(words)
# print(words_frequency.most_common(20))

# get bigrams
# print(list(bigrams(words))[10:40])

# remove stopwords
stopwords = stopwords.words('english')
clean_speech = filter(lambda x: x not in stopwords, words)
clean_speech2 = [word for word in words if word not in stopwords]
# print(list(clean_speech))
# print(clean_speech2)

# stemming
# paragraph
sample_text = 'Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity.'
sample_text = re.sub('\W', ' ', sample_text.lower())
sample_words = word_tokenize(sample_text)

# porter
stemmer = PorterStemmer()
porter_text = [stemmer.stem(word) for word in sample_words]
# print(' '.join(porter_text))

# lancaster
stemmer = LancasterStemmer()
lancaster_text = [stemmer.stem(word) for word in sample_words]
# print(' '.join(lancaster_text))

# print(stem_speech[0:10])

# snowball
# print(SnowballStemmer.languages)
stemmer = SnowballStemmer('english')
snowball_text = [stemmer.stem(word) for word in sample_words]
# print(' '.join(snowball_text))

# snowball 2
stemmer = SnowballStemmer('english', ignore_stopwords=True)
snowball_text2 = [stemmer.stem(word) for word in sample_words]
# print(' '.join(snowball_text2))

# lemmatizing
# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('cats'))
# print(lemmatizer.lemmatize('cacti'))
# print(lemmatizer.lemmatize('geese'))
# print(lemmatizer.lemmatize('rocks'))
# print(lemmatizer.lemmatize('python'))
# print(lemmatizer.lemmatize('better', pos='a'))
# print(lemmatizer.lemmatize('best', pos='a'))
# print(lemmatizer.lemmatize('run'))
# print(lemmatizer.lemmatize('run', pos='v'))

# stemming
stemmer = PorterStemmer()
print(stemmer.stem('cats'))
print(stemmer.stem('cacti'))
print(stemmer.stem('geese'))
print(stemmer.stem('rocks'))
print(stemmer.stem('python'))
print(stemmer.stem('better'))
print(stemmer.stem('best'))
print(stemmer.stem('run'))
print(stemmer.stem('run'))

# final example
sample_text = 'Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation.'
sample_text = re.sub('\W', ' ', sample_text.lower())
sample_words = word_tokenize(sample_text)
clean_words = filter(lambda x: x not in stopwords, sample_words)
clean_words = list(clean_words)
stemmer = SnowballStemmer('english')
snowball_words = [stemmer.stem(word) for word in clean_words]
words_frequency = FreqDist(snowball_words)
print(words_frequency.most_common(10))
