import string
import re
import codecs
from os import path
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import wordpunct_tokenize

class Tokenizer:

  def __init__(self):
    self.stemmer = PorterStemmer()
    self.stopwords = (nltk.corpus.stopwords.words('english') +
      list(string.punctuation) +
      ['lt', 'gt', 'vs'])
    self.numbers = re.compile('^\d+(st|nd|rd|th|p|pct)?$', re.IGNORECASE)

  #Tokenize
  #Unicode
  #Remove stopwords, numbers and common abbreviations
  # More things to try:
  # > better tokenising for in-word punctation like u.s. and 
  #    energy/usa
  def tokenize(self, doc):
    tokens = wordpunct_tokenize(doc.strip())
    return [unicode(self.stemmer.stem(t.lower())) for t in tokens
            if not t.lower() in self.stopwords and not self.numbers.match(t)]


class SingleFileCorpus(object):

  def __init__(self, in_file, dictionary):
    self.in_file = in_file
    self.dictionary = dictionary

  def __iter__(self):
    with codecs.open(self.in_file, 'r', 'utf-8') as f:
      for doc in f:
        yield self.dictionary.doc2bow(doc.strip().split())

class Paths(object):
  base = 'data'
  texts_clean = path.join(base, 'reuters_preprocessed.txt')
  text_index = path.join(base, 'reuters_fileids.txt')
  dictionary = path.join(base, 'dictionary.txt')
  corpus = path.join(base, 'corpus.mm')
  tfidf_model = path.join(base, 'tfidf.model')
  lsi_model = path.join(base, 'lsi.model')
  similarity_index = path.join(base, 'tfidf-lsi.index')