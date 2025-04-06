# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import degrees,atan2

# Enter your code here. Read input from STDIN. Print output to STDOUT
def angle(ab,bc):
    MBC=round(degrees(atan2(ab,bc)))
    
    return (str(MBC))
    
ab=int(input())
bc=int(input())
result=angle(ab,bc)  
print(result,chr(176),sep='')  
#chr(176) is degree sign
