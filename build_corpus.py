import codecs
from gensim import corpora, models, similarities
from reuters_nlp import SingleFileCorpus, Paths

# Build corpus script - build gensim dictionary and corpus 
dictionary = corpora.Dictionary()

#First pass: create dictionary and write out a processed file with
# one document per line
with codecs.open(Paths.texts_clean, 'r', 'utf-8') as f:
  for doc in f:
    tokens = doc.strip().split()
    dictionary.doc2bow(tokens, allow_update=True)

# Remove very rare and very common words
dictionary.filter_extremes()
dictionary.save(Paths.dictionary)

#Second pass over files to serialize corpus to file
corpus = SingleFileCorpus(Paths.texts_clean, dictionary)
corpora.MmCorpus.serialize(Paths.corpus, corpus)