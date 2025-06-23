# check if an array is palindrome

def is_palindrome(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left +=1
        right -=1

    return True

arr =  [1, 2, 3, 2, 1]
print(is_palindrome(arr))