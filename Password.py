import re
password="Secure@123"
pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
if re.match(pattern,password):
    print("StrongPassword")
else:
    print("Not Strong")    