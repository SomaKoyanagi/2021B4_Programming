f = open('dataset/data.txt','r')
line = f.readline()

while line:
    print(line.strip())
    line = f.readline()
f.close()