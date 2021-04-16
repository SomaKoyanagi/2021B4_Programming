import numpy as np

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]] 
terms = ["リンゴ", "レモン", "ミカン"]

def tf(term,doc):
    return doc.count(term)/len(doc)

def idf(term,docs):
    N = len(docs)
    df = 0
    for d in docs:
        if term in d:
            df+=1
    return np.log10(N/df)+1


def tfidf(term,doc):
    array = []
    t_num =-1
    d_num =-1
    array = np.zeros((len(term),len(doc)))
    for t in term:
        t_num += 1
        d_num = -1
        for d in doc:
            d_num += 1
            array[d_num][t_num] = idf(t,doc)*tf(t,d)
    return array

print(tfidf(terms,docs))





