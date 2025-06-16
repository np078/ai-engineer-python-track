# Q21: Write a Python program to count the number 4 in a given list.

lst = [4,5,6,8,4,2,6,7,4,4,4]

count= 0
for i in lst:
    if i ==4:
        count+=1

print("Number of 4s in the list: ", count)

# USing .count() method

print("Numbr of 4s in the given list: ", lst.count(4))