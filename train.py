from gensim import corpora, models, similarities
from reuters_nlp import Paths

# Train script - train models and build similarity index
n_topics = 300

print "Loading corpus and dictionary"
corpus = corpora.MmCorpus(Paths.corpus)
dictionary = corpora.Dictionary.load(Paths.dictionary)

print "Training TFIDF model"
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

print "Training LSI model"
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=n_topics)
corpus_lsi = lsi[corpus_tfidf]

print "Building index"
# Memory-bounded similarity method - use similarities.Similarity for larger data
index = similarities.MatrixSimilarity(corpus_lsi)

print "Serialising models and index"
tfidf.save(Paths.tfidf_model)
lsi.save(Paths.lsi_model)
index.save(Paths.similarity_index)