N=int(input("maximun capacity of Jar:"))

K=int(input("enter Refill limit of Jar:"))

M=int(input("Current no candies in jar:"))

C=int(input("enter candies requested by customer:"))
if C>M:
    print("invalid inpout")
else:
    #substract candiest given  to customer
    M=M-C
    
    #if candies become less than or equal to K
    #refill the jar to full capacity
    
    if M<=K:
        M=N
        
    print(" number of candies sold:",C)     
    print(" number of candies Available after update:",M)  
    