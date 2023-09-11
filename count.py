import math
count=6
while count>0:
    print(count)
    count-=1
def func():
     global Value
     Value="local"
Value="global"
print(Value) 
func()
print(Value)    
print(math.pi)