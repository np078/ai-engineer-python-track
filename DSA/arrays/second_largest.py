# Q3: Find the second largest element

'''
# METHOD 1 (By SOrting)
arr = [12, 35, 1, 10, 34, 1]
arr = sorted(set(arr)) # it will remove duplicates and then sort

if len(arr) < 2:
    print(None)
else:
    print(arr[-2])
    '''

def secondlargest(arr):
    flargest = arr[0]
    slargest = float('-inf')

    for i in arr:
        if i > flargest:
            slargest = flargest
            flargest = i

        elif i < flargest and i > slargest:
            slargest = i

    return slargest

arr = [12, 35, 1, 10, 34, 1]
slarge = secondlargest(arr)
print(slarge)