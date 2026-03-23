l,r=map(int,input("enter your range:").split())
found=False
for n in range(l,r+1):
    if n%7==0 and n%5!=0:
        s=str(n)
        if s!=s[::-1]:
            if len(s)==len(set(s)):
                print(n)
                found=True
if not found:
    print(-1)                