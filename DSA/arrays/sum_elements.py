# Q1: Sum of all elements

def sum_elements(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
    
arr = [5, 8, 2, 10]
sum = sum_elements(arr)
print(sum)
