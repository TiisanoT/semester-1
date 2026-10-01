# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")  #
print(f"Modified String 1: {user_string.lower()}")  # converts to lowercase 
print(f"Modified String 2: {user_string.upper()}")   # converst to uppercase
print(f"Modified String 3: {user_string.strip()}")    # removes spaces from start and end 
print(f"Modified String 4: {user_string.replace('a', '@')}")  # it wouldreplace every a with an @
print(f"Modified String 5: {user_string.capitalize()}")  # it would capaatalize the first lette  
print(f"Modified String 6: {user_string[::-1]}")   # it will reverse teh string 
print(f"Modified String 7: {user_string.title()}")  # it willl capoatalise the first letter of each word
print(f"Modified String 8: {len(user_string)}")   # it will couunt the number of characters
print(f"Modified String 9: {user_string.find('a')}")   # it woudld find the index of the first a 
print(f"Modified String 10: {user_string.count('a')}")  # it will count how many times a would appear
print(f"Modified String 11: {user_string.startswith('Hello')}")  # It will check if the string starts with hello
print(f"Modified String 12: {user_string.endswith('!')}")  # It will check if the string ends with an exclamation mark 
print(f"Modified String 13: {user_string.isalnum()}")  # checks if letters contains only letters and numbers 
print(f"Modified String 14: {user_string.isalpha()}")  # checks if the string only contains letters 
print(f"Modified String 15: {user_string.isdigit()}")  # checks if the string only contains digits 



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!