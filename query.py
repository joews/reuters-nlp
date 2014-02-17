from gensim import corpora, models, similarities
from nltk.tokenize import word_tokenize, wordpunct_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import reuters
import numpy as np
from reuters_nlp import Tokenizer, Paths

# Query script - find the documents that most closely match an input document
#  and examine the top topics to see which were the most important

# Similarity index
index = similarities.MatrixSimilarity.load(Paths.similarity_index)

# LSI model
model = models.LsiModel.load(Paths.lsi_model)

# Gensim dictionary (word <-> feature ID mapping)
dictionary = corpora.Dictionary.load(Paths.dictionary)

# Custom tokeniser/normaliser
tokenizer = Tokenizer()

# Recall NLTK corpus fileids to retrieve matching document
fileids = []
with open(Paths.text_index) as f:
	fileids = [line.rstrip() for line in f]


print "Enter a query document:"
s = raw_input('> ')

while s and s != 'exit':

	# Convert input document into LSI vector space
	tokens = tokenizer.tokenize(s)
	bow_vector = dictionary.doc2bow(tokens)
	lsi_vector = model[bow_vector]

	# Compute similarity of input vector to all document vectors
	similarities = index[lsi_vector]
	similarities = sorted(enumerate(similarities), key=lambda item: -item[1])

	# Get contents of most similar documents
	(file_no, score) = similarities[0]
	fileid = fileids[file_no]
	contents = reuters.open(fileid).read()

	# Re-convert most similar document to LSI space
	#  to examine similarity
	match_tokens = tokenizer.tokenize(contents.strip())
	match_bow_vector = dictionary.doc2bow(match_tokens)
	match_lsi_vector = model[match_bow_vector]

	# Find the topic (LSI vector element) with the smallest difference
	#  between the corpus document and the query document - this should
	#  be the topic that contributed the most to the similarity
	lsi_values = np.array([e[1] for e in lsi_vector])
	match_lsi_values = np.array([e[1] for e in match_lsi_vector])
	deltas = np.absolute(lsi_values - match_lsi_values)
	
	# Sort to bring the most important topics to the start of the list
	sorted_topics = sorted(enumerate(deltas), key=lambda e: e[1])
	top_topic = model.show_topic(sorted_topics[0][0], 20)
	top_topic_words = [e[1] for e in top_topic]
	
	print "The closes matching document:"
	print "%s - %.3f" % (fileid, score)
	print contents, "\n"

	print "The most significant topic included these stems:"
	print ', '.join(top_topic_words), "\n"

	print "-" * 80
	s = raw_input('>')