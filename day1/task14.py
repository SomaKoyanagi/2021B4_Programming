import numpy as np

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]] 
terms = ["リンゴ", "レモン", "ミカン"]

def idf(term,docs):
    N = len(docs)
    df = 0
    for d in docs:
        if term in d:
            df+=1
    return np.log10(N/df)+1

for t in terms:
    print("idf(",t,") = ",idf(t,docs))