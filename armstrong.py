n=int(input("enter number:"))
result=0
copy=n
# length=len(str(abs(n)))
length=len(str(n))
print(length)
while(n>0):
    digit=n%10
    result=result+digit**length
    n=n//10
print("result is:",result)    
if(result==copy):
    print("given number is armstrong")
else:
    print("given number is Not a armstrong")
            
    