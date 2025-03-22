import re
text="Hello python are you good"
modified_text=re.sub(r"\s","_",text)
print(modified_text)

#extracting text from string
text2="i have 2 apple,3 banana,4 mango"
numbers=re.findall(r"\d+",text2)
print('Numbers found are:',numbers)

text3="alice and Alexander are close friends"
words=re.findall(r"\b[Aa]\w+",text3)
print('words found are:',words)