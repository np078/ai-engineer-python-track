# Q2: Find Max and Min in an Array

def get_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for i in arr:
      if i > max_val:
        max_val  = i

      if i < min_val:
        min_val = i

    return max_val, min_val

arr = [12, 4, 99, 23, 7]

max_value, min_value = get_max_min(arr)
print("Max:", max_value)
print("Min:", min_value)