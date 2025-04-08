

#read list of numbers
numlist=list(map(int,input("enter list of numbers" ).split()))
print(numlist)
n=len(numlist)
sum=0
for i in range(len(numlist)):
    sum=sum+numlist[i]
sumfirst=sum-numlist[0]
sumsecond=sum-numlist[n-1]   
print("first sum is",sumfirst)
print("second sum is",sumsecond)