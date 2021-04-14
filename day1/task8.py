words = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
dict = {}
lst = words.split(' ')
cnt=1
for s in lst:
    if cnt == (1 or 5 or 6 or 7 or 8 or 9 or 15 or 16 or 19):
        dict[s[:1]] = cnt
    else:
        dict[s[:2]] = cnt
    cnt+=1
print(dict)    
