import cPickle as pickle  # data preprocessing
from collections import Counter  # tokenization
import keras  # ML
import postprocessing as pr  # helper


# Step 1 - Load data
with open('data/%s.pkl', 'rb') as fp:
    headings, articles, keywords = pickle.load(fp)


# Tokenize text
def get_vocab(lst):
    vocabcount, vocab = Counter(w for txt in lst for w in txt.split())
    return vocab, vocabcount

vocab, vocabcount = get_vocab(head+desc)

print vocab[:50]
print '...', len(vocab)

