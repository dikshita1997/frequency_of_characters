str1="Mississippi"
dict={}

def char_frequency(str1):
    for i in str1:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    print(str(dict))
char_frequency(str1)
