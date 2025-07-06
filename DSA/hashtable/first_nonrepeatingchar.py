string = "szsubauna"
freq = {}

for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

for ch in string:
    if freq[ch] == 1:
        print("Fisrt non-repeating character is:", ch)
        break