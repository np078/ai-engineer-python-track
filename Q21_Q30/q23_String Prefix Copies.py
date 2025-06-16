'''
Q23: Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n 
copies of the whole string if the length is less than 2.

'''
str = input("Enter a string: ")
n = int(input("Enter the number of copies: "))
n2 = str[:2] * n  # slicing
if len(str) <2:
    print("The number of copies: ", n*str)
else:
    print("The number of copies: ",n2)