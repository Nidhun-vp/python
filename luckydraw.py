n=int(input())
sum=0
r=0
for i in range(2):
    r=n%10
    sum=sum+r
    n=n//10
if sum==3 or sum==8:
        print("lucky draw winner")
else:
    print("not a lucky draw winner")        