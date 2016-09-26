import re
from nltk import word_tokenize
from nltk import FreqDist
from nltk import bigrams
from nltk import trigrams
import re
from nltk.corpus import stopwords
import string
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem.lancaster import *
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

sentence = 'Five score years ago , a great American , in whose symbolic shadow we stand signed the Emancipation Proclamation .'
sentence = re.sub('\W', ' ', sentence.lower())

# get unigrams
words = word_tokenize(sentence)
words_frequency = FreqDist(words)
# print(words_frequency.most_common(20))

# get bigrams
# print(list(bigrams(words))[10:40])

# get trigrams
# print(list(trigrams(words))[1:5])

# delete stopwords
stopwords = stopwords.words('english')
clean_speech = filter(lambda x: x not in stopwords, words)
clean_speech = list(clean_speech)
# clean_speech2 = [word for word in words if word not in stopwords]

#stemmer
stemmer = PorterStemmer()
porter_text = [stemmer.stem(word) for word in clean_speech]
print(porter_text)

#lancaster
stemmer = LancasterStemmer()
lancaster_text = [stemmer.stem(word) for word in clean_speech]
print(lancaster_text)

#snowball
# print(SnowballStemmer.languages)
stemmer = SnowballStemmer('english')
snowball_text = [stemmer.stem(word) for word in clean_speech]
print(snowball_text)
