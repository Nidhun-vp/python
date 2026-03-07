a=[1,2,0,4,8,0,3,0,7]
non_zero=[x for x in a if x!=0]
zero=[0]*a.count(0)
result=non_zero+zero
print(result)