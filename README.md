# reuters-nlp

Learning basic natural language processing and topic modelling techniques with [NLTK](http://www.nltk.org/) and [Gensim](http://radimrehurek.com/gensim/index.html).

 * Document tokenising and normalising
 * Stemming
 * Removing stopwords and words that are very rare and very common in a corpus
 * Bag-of-words vectors
 * [TF-IDF](http://en.wikipedia.org/wiki/TFIDF)
 * [Latent Semantic Indexing](http://en.wikipedia.org/wiki/Latent_semantic_indexing)
 * Similar document retrieval

## Install

    $ pip install nltk
    $ pip install gensim 

## Prepare data

    $ python preprocess.py
    $ python build_corpus.py
    $ python train.py

## Find documents similar to search terms

    $ python query.py

## TODO:

* HTTP API for results visualisation and analysis
* Improved tokenisation of in-word punctuation
* More similarity metrics