nums = [2, 11, 7, 15]
target = 9

index_map = {}  # DOne by using hashing

for i in range(len(nums)):
    num = nums[i]
    complement = target - num

    if complement in index_map:
        print("Two indices:", [index_map[complement], i])
        break

    index_map[num] = i
