def palindrome(s):
    return s==s[::-1]
message=input("enter message:")
result=palindrome(message)
if(result==True):
    print(message,"is palindrome")
else:
    print(message,"is not a  palindrome")

print(result)