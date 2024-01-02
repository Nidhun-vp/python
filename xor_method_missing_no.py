def get_missing_xor(a):
    n=len(a)
    xor_a=a[0]
    for index in range(1,n):
        xor_a=xor_a^a[index]# ^ is xor,xor of 1to n
    x2=0
    for index in range(1,n+2):    
        x2=x2^index # ^ of nos present in the array
    print(xor_a^x2)    
    
    
a=[1,2,4,5,6,7]   
get_missing_xor(a) 