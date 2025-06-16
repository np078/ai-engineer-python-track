
# Q21: Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

# My logic
n=int(input("Enter a number: "))

if n%2 == 0:
    print(f"The number {n} is even")

else:
    print(f"The number {n} is odd")

# USing function
def even_odd(n):
    if n%2 == 0:
        return f"The number {n} is even"
    else:
        return f"The number {n} is odd"
    
num = int(input("Enter a number: "))
print(even_odd(num))


'''
This program takes an integer input from user and prints a message accordingly, whetehr the input is even or odd.
'''