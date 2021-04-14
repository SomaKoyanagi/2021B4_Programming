# -*- coding: utf-8 -*-
import sys

def bigram(seq,n):
    lst1 = []
    for i in range(len(seq)-1):
        lst2 = []
        for s in range(n):
            lst2.append(args[i+s])
        lst1.append(lst2) 
    print("単語bi-gram:",lst1)

    lst2=[]
    word = ''.join(seq)
    for i in range(len(word)-1):
        lst2.append(word[i:i+n])
    print("文字bi-gram:",lst2)
    
    
args = sys.argv
args.pop(0)
bigram(args,2)