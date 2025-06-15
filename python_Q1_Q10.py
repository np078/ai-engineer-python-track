'''
Q1: Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

# Solution
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
'''

'''
Q2: Write a Python program to find out what version of Python you are using.

# Solution
import sys
print(sys.version)
'''

'''
Q3: Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

# Solution
import datetime
now = datetime.datetime.now()
print("Current date and time:\n", now)
'''

'''
Q4: Write a Python program that calculates the area of a circle based on the radius entered by the user.

# Solution
import math
r = float(input("Enter the radius(in cm): "))
area = math.pi * r * r
print(f"Area of the circle with radius {r} cm is: ", area, "cm²")
'''

'''
Q5: Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

# Solution
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
print(f"{l_name} {f_name} ")
'''

'''
Q6: Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

# Solution
num = input("Enter comma separated numbers: ")

num_list = num.split(",")
num_tuple = tuple(num_list)

print("List: ", num_list)
print("Tuple: ", num_tuple)
'''

'''
(FILE EXTENSION EXTRACTOR)
Q7: Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java

# Solution
f_name = input("Enter Your file name: ")
extension  = f_name.split(".")[-1]  # Here the .split, split the entered string wherever it finds a "." (eg; hello.py --> f_name.split(".")  →  ['hello', 'py']

print("The extesion of the file is: ", extension)
'''

'''
Q8: Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]

# Solution
color_list = ["Red","Green","White" ,"Black"]
f_color = color_list[0]
l_color = color_list[3]

print("The first color of the list is: ", f_color)
print("The last color of the list is: ", l_color)
'''

'''
Q9: Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014

#Solution
exam_st_date = (11, 12, 2014)
print("The examination will start from: %i / %i /%i " % exam_st_date ) # String Fomatting (newly learned)

'''

'''
Q10: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615

# Solution
n = input("Enter a number: ")
value = int(n) + int(n*2) + int(n*3) # Key concept of string multipliccation , not math multiplication
print(value)
'''

'''
Q11:
Build a class Book with:

Attributes: title, author, pages

Method: show_details() that prints all info

# Solution
class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def show_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages:{self.pages}")

b1= Book("Harry Potter", "Unknown", 300)
b2= Book("Ramayana", "valmiki", 1000)
b3= Book("Mahabharata", "Lord Krishna", 5000)

b1.show_details()
b2.show_details()
b3.show_details()
'''