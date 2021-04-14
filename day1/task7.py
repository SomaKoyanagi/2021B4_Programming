words = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = words.replace(',','')
words = words.replace('.','')
lst = words.split(' ')
lst  = [len(s) for s in lst]
print(lst)