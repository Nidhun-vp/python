def factorial(n):
    if(n==0):
        return 1
    else:
        return (n*factorial(n-1))
n=int(input())
result=factorial(n)
print("factorial of given number ",n,"is:",result)    