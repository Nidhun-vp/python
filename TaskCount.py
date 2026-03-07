import re
s=input()
groups=re.findall(r'\[(.*?)\]',s)

count=0
for g in groups:
    tasks=g.split(',')
    for t in tasks:
        t=t.strip()
        if any(c.isalpha() for c in t):
            count+=1
print("no of task is:",count)            