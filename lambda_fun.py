numbers=[2,4,5,6,12]
num=[1,2,3,4,5]
result=list(map(lambda x:x**2,numbers))
print(result)
even=list(filter(lambda x:x%2==0,numbers) )
print(even)
product=list(map(lambda x,y:x*y,numbers,num))
print(product)