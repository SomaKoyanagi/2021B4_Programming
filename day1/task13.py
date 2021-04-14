
docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]] 
terms = ["リンゴ", "レモン", "ミカン"]


def tf(term,doc):
    return doc.count(term)/len(doc)

for t in terms:
    for d in docs:
         print("tf(",t,",",d,") =",tf(t,d))

