def regenerate_number(original_number,digit_to_replace,new_digit):
    num_str=str(original_number)
    if str(digit_to_replace) in num_str:
        modified_str=num_str.replace(str(digit_to_replace),str(new_digit))
        regenerated_number=int(modified_str)
        return regenerated_number
    else:
        return None

original_number=input("enter no:")
digit_to_replace=1#replace all 1 with 2
new_digit=2
new_number=regenerate_number(original_number,digit_to_replace,new_digit)
print(new_number)
original_number=int(original_number)
diff=new_number-original_number
print("difference b/w new number and original is: ",diff)
