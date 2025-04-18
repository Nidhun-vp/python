def char_sequence_count(stringinput):
    if not stringinput:
        return "Input string is empty"
    result=""
    count=1
    
    
    for i in range(1,len(stringinput)):
        if stringinput[i]==stringinput[i-1]:
            count+=1
        else:
            result+=str(count)+stringinput[i-1]
            count=1
            
    #add last sequence
    result+=str(count)+stringinput[-1]
    return result        

input_string=input("Enter a string: ")
output=char_sequence_count(input_string)
print(output)