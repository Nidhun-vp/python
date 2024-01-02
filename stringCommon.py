def freq_words():
    str=input("enter a string:") #sheena loves eating apple and mango. Her sisters also loves eating apple and mango
    split_string=str.split()
    d={}
    for i in split_string:
        if i not in d.keys():#d[i]=d.get(i,0)+1
            d[i]=0           #or you can above code for line 6,7,8
        d[i]=d[i]+1          #
    print(d)        
freq_words()    