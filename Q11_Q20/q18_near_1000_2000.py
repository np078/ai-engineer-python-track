# Q18: Write a Python program to test whether a number is within 100 of 1000 or 2000.

# Solution

def near_1000_or_2000(n):
    return (abs(1000-n) <=100) or (abs(2000-n) <=100)

while True:
   num = int(input("Enter a number: "))
   print(near_1000_or_2000(num))

   cont = input("Do you want to check again? (y/n): ")
   if cont.lower() != 'y':
       break