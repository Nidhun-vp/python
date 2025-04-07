def binary_str(binary_string):
    parts=binary_string.split()
    hours=int(parts[0],2)*10+int(parts[1],2)
    minutes=int(parts[2],2)*10+int(parts[3],2)
    return (f"{hours:02}:{minutes:02}")

binary_string=input("Enter binary string (four binary numbers separated by spaces):")    
result=binary_str(binary_string)
print(result)