n,m=map(int,input().split())
count=0
for _ in range(n):
    marks=list(map(int,input().split()))
    if sum(marks)>50:
        count+=1
print(count)        