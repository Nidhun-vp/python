def printnumbers(n):
    if n==0:
        return 0
    else:
        return n+printnumbers(n-1)
    
  
  
  
limit=int(input("enter limit:"))  
print(printnumbers(limit))  