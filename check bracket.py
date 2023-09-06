open_list=["[","{","("]  
close_list=["]","}",")"]
def check(mystr):
    stack=[]
    for i in mystr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos=close_list.index(i)
            if((len(stack)>0)and (open_list[pos]==stack[len(stack)-1])):     
                stack.pop()
            else:
                return "unbalaced1"
    if len(stack)==0:
        return "balanced"
    else:
         return "Unbalanced"
string="{[]{()}}"
print(string,"-",check(string))      
string="{[]}"
print(string,"-",check(string))       
string=input("enter braces:\n")
print("\n\n")
print(string,"-",check(string))                         