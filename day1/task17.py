import numpy as np
from nlp import task15
from nlp import task16
import task12

docs = task12.docs
terms = task12.terms
tfidf = task15.tfidf(terms,docs)
ld = len(docs)
array = np.zeros((ld,ld))


for s in range(len(tfidf)):
    for t in range(len(tfidf)):
        array[s][t] = task16.cosine_sim(tfidf[s],tfidf[t])

print(array)