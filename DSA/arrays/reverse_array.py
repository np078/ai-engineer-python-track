# Q2: Reverse the array (without using reverse())

def reverse_arr(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1
    return arr

arr = [1, 2, 3, 4]
rev_arr = reverse_arr(arr)
print(rev_arr)