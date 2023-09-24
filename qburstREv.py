def modify_string(input_str):
    # Step 1: Reverse each individual word in the string
    words = input_str.split()
    reversed_words = [word[::-1] for word in words]

    # Step 2: Replace even index characters with uppercase and odd index characters with lowercase
    modified_words = []
    for word in reversed_words:
        modified_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                modified_word += word[i].upper()
            else:
                modified_word += word[i].lower()
        modified_words.append(modified_word)

    # Step 3: Replace even index space with '#' and odd index space with '*'
    modified_str = ''
    for i, word in enumerate(modified_words):
        if i % 2 == 0:
            modified_str += word.replace(' ', '#')
        else:
            modified_str += word.replace(' ', '*')

    # Step 4: Replace any other characters in even index with '@' and odd index with '$'
    final_output = ''
    for i in range(len(modified_str)):
        if i % 2 == 0:
            final_output += modified_str[i].replace(' ', '@')
        else:
            final_output += modified_str[i].replace(' ', '$')

    return final_output

# Test the function
input_string = "Hello , World. "
result = modify_string(input_string)
print(result)
