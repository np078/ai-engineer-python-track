# Q4: Count frequency of each element
'''
Input: [1, 2, 2, 3, 1, 4]
Output: {1: 2, 2: 2, 3: 1, 4: 1}
'''
def count_frequency(arr):
    freq = {}

    for item in arr:
        if item in freq:
            freq[item]+=1
        else:
            freq[item] = 1

    return freq

arr = [1, 2, 2, 3, 1, 4]
print("Frequencies:", count_frequency(arr))