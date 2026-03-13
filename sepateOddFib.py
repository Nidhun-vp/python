def find_nth_term(n):
    if n%2 !=0:
        idx=(n//2)+1
        a,b=1,1
        for _ in range(idx-1):
            a,b=b,a+b
        return a
    else:
        idx=n//2
        primes,num=[],2
        while len(primes)<idx:
            if all(num%i !=0 for i in range(2,int(num**0.5)+1)):
                primes.append(num)
            num+=1
        return primes[-1]        

n=int(input("enter N:"))
print(f"result:{find_nth_term(n)}")