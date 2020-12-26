import operator
str1="Mississippi"
d={}

def char_frequency(str1):
    for i in str1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    print(sorted_d)
char_frequency(str1)
