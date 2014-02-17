import codecs
from nltk.corpus import reuters
from reuters_nlp import Tokenizer, Paths

# Preprocess script - build a single text file with cleaned, normalised documents
#  - tokenised, stemmed, one document per line.
# Track fileids to retrieve document text later

docs = 0
bad = 0

tokenizer = Tokenizer()

with open(Paths.text_index, 'w') as fileid_out:
  with codecs.open(Paths.texts_clean, 'w', 'utf-8-sig') as out:

    for f in reuters.fileids():
      contents = reuters.open(f).read()

      try:
        tokens = tokenizer.tokenize(contents)
        docs += 1
        if docs % 1000 == 0:
          print "Normalised %d documents" % (docs)
        
        out.write(' '.join(tokens) + "\n")
        fileid_out.write(f + "\n")

      except UnicodeDecodeError:
        bad += 1

print "Normalised %d documents" % (docs)
print "Skipped %d bad documents" % (bad)
print 'Finished building ' + Paths.texts_clean
