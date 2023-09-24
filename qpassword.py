# string="Qburst@123"
# length=len(string)
# print(length)
# if(length>8 and string[0].isupper()):
#     print("super")
#     for item in string:
#         print(item.isdigit)
#     if(item=="@" | item=="#"|item=="%"|item=="&"):
#         print("true") 
    
    
# else:
#     print("bad")
            
import re

def check_string_conditions(input_string):
    # Check if the length is at least 8 characters
    if len(input_string) < 8:
        return False

    # Check if it starts with a capital letter
    if not input_string[0].isupper():
        return False

    # Check if it contains at least one numeric value
    if not re.search(r'\d', input_string):
        return False

    # Check if it contains at least one special character from the list [@$%&]
    if not re.search(r'[@$%&]', input_string):
        return False

    # If all conditions are met, return True
    return True

# Example usage:
input_string = input()
result = check_string_conditions(input_string)
print(result)  # This will print True for the example input
