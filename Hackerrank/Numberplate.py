def Format_Numberplate(p):
    if not p.isalnum() or not plate.isupper():
        return "invalid1"
    n=len(p)   
    # Handle invalid case where last group cannot be 3 or 2 characters
    # last group would have only 1 character, which is not allowed
    if(n<2 or (n%3==1)):
        return "invalid2"
    result=[]
    i=0
#last group need to be 2 charactors
# We run the loop until there are exactly 2 characters left at the end (i.e., n - i == 2).
# Example: For n = 8, we do:
# Group 3: i=0 → ABC
# Group 3: i=3 → 123
# Final 2: i=6 → XY
    if n%3==2:
        while i<=n-5:
            result.append(p[i:i+3])
            i=i+3
        result.append(p[-2:])  
    else:
        while i<n:   
              result.append(p[i:i+3])  
              i=i+3
    return "-".join(result)
#input
plate=input().strip()
print(plate)
print(Format_Numberplate(plate))

    