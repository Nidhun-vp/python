s={1,2,3}
print(s)
s=set({1,2,3})
print(s)
s={1,2,3,3,3,3,4,4,5,4}#automatically remove duplicate
print(s)
s.add(8)
print(s)
s.update([10,11,12,10])#multiple values entering
print(s)
#delete
s.discard(3)
print(s)
s.remove(5)
print(s)