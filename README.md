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

    Enter a query document:
    > africa coffee
    The closes matching document:
    training/3034 - 0.804
    UGANDA DISAPPOINTED BY COFFEE TALKS FAILURE
      Uganda, Africa's second largest coffee producer [...]

    The most significant topic included these stems:
    gencorp, april, group, cent, price, offer, china, crown, american, industri, 
    week, six, gener, save, januari, taiwan, day, baker, deficit, copper
    -------------------------------------------------------------------------------
    > american coffee
    The closes matching document:
    training/6595 - 0.675
    N.Y. TRADERS SAY LATIN COFFEE PRODUCERS TO MEET
      Several traders and analysts here told Reuters Latin American coffee 
      producers will meet [...]  

    The most significant topic included these stems:
    co, quarterli, corp, sugar, april, set, corn, gencorp, japan, bill, cyclop, 
    qtli, march, system, merger, februari, reserv, o, taiwan, offer
    -------------------------------------------------------------------------------


## TODO:

* HTTP API for results visualisation and analysis
* Improved tokenisation of in-word punctuation
* More similarity metrics

## Resources
 * [Gensim tutorials](http://radimrehurek.com/gensim/tutorial.html)
    - [Gist](https://gist.github.com/jwhitfieldseed/8943758)
 * [Natural Language Processing with Python](http://www.nltk.org/book/)