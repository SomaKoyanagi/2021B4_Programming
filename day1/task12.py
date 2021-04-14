f = open('dataset/data.txt','r')
line = f.readline()
docs = []
d =[]
terms = []

while line:
    d = line.strip().split('と')
    docs.append(d)
    terms += d
    line = f.readline()

terms = list(set(terms))
f.close()
print("docs : ", docs)
print("terms : ", terms)

