# Q Check if array is sorted
'''
Input: [1, 2, 3, 4]
Output: True
'''
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
    
arr = [1, 2, 4, 5]
print(is_sorted(arr))