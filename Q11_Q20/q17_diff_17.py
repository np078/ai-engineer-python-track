# Q17: Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

# Solution

num = int(input("Enter a number: "))
if num > 17:
    print(2*(num - 17))
else:
    result = num - 17
    print(abs(result))
