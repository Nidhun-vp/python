a={1,2,3,4,5,6,7}
b={8,9,10,11,2,5}
#intersection
print(a&b)
#union
print(a|b)
#difference
print(a-b)
#symmetric difference
print(a^b)
#comprehensions create new list using existing  list
c=[i+1 for i in a]
print(c)
#create a new set using values of an existing set.
d={i**2 for i in a}
print(d)
f={'hello':'world','first':'1'}
print(f)
e={val:k for k,val in f.items()}
print(e)