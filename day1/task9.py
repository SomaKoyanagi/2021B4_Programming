# -*- coding: utf-8 -*-

import sys
import random

args = sys.argv
args.pop(0)

lst = []
for w in args:
    if len(w) <= 3:
        lst.append(w)
    else:
        wlist = list(w[1:-1])
        random.shuffle(wlist)
        lst.append(w[0]+''.join(wlist) + w[-1])
typ = ' '.join(lst)
print(typ)