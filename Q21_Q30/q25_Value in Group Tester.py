'''
Q25: Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

'''
def value__in_group(n,group):
    if n in group:
        return True
    else:
        return False


lst = [1, 5, 8, 3]
num = int(input("Enter a number: "))
print(value__in_group(num,lst))