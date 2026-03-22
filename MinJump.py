import math
H=int(input("enter height of pole"))
X=int(input("enter climb distance"))
Y=int(input("enter slip distance"))

if H<=X:
    print(1)
else:
    jump=math.ceil((H-X)/(X-Y))+1
    print(jump)

