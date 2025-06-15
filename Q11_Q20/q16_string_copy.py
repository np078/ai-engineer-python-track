# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

# Solution

def copies_str(s, n):
    return n * s

text = input("Enter the string: ")
num = int(input("Enter the number of copies: "))

if num < 0:
    print("Please enter a non-negative number")
else:
    print("Numer of copies: ", copies_str(text,num))