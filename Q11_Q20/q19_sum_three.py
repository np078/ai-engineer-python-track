# Q19: Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

# Solution 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

total = num1+num2+num3
print("Sum: " ,total)

if num1 == num2 == num3:
    print("All the numbers are equal.")
    print("Tripled sum", 3*total)