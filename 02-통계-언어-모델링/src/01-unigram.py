import nltk
from nltk.util import ngrams
from nltk.corpus import alpino

unigrams = ngrams(alpino.words(), 4)

for i in unigrams:
    print(i)
    exit()
