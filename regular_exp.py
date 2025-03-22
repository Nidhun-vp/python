import re
text1="l love you python 7025"
match=re.search(r"python",text1) #text search
if match:
    print("python text found")
else:
    print("python text not found") 
    
number=re.search(r"\d+",text1)    #numbers search
if number:
    print("number text found")
else:
    print("number text not found")    

email="nidhun@gmail.com"
pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(pattern,email): #mail search
    print("validMail")
else:
    print("invalid Mail")    
        
