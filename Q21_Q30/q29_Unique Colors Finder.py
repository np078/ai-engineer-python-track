# Q29:
'''
Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}

'''
# My approach (but it does not matches the output sequence)
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

for i in color_list_1:
    if i not in color_list_2:
        print(i) 

# Exact solution

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

output = (color_list_1 - color_list_2)
print(output)
