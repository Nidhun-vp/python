a='''mistakes
makes
a man
perfect.'''
print(a)
b="nidhun"
print(b[0],b[1],b[2])
print(b[-1],b[-2],b[-3])
#slicing string
print(b[0:4])
print(b[3:-1])
#upper
print(b.upper())
#lower
print(b.lower())
#isupper
print(b.isupper())
#islower
print(b.islower())
#alphanumeric
print(b.isalpha())
#returns True if string starts with an uppercase letter and then rest of the characters are lowercase
c="Camel"
print(c.istitle())
c="Camel \nhell"
print(c.isspace())
#split and join
list=["one","two","three"]
s='-'.join(list)
print(s)
newlist=s.split(':')
print(newlist)
#string formatting
first1='first'
second1='second'
s="sunday is the {} day of the week,whereas monday is the {} day of the week".format(first1,second1)
print(s)
