# Q20: Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

# Solution

# My Logic
text = input("Enter a string: ")

if text.startswith("Is"):
    print(text)

else:
    print("Is" + text)

# Using Function
def Is_prefix(s):
    if s.startswith("Is"):
        return s
    else:
        return "Is" + s
    
text = input("Enter a string: ")
print(Is_prefix(text))
