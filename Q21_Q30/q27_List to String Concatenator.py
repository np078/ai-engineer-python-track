# Q27: Write a Python program that concatenates all elements in a list into a string and returns it.

# My logic
def concatenate_el(items):
    output = ''
    for i in items:
        output += i

    return output
            
input = ['p', 'y', 't', 'h', 'o', 'n']
print(concatenate_el(input))

# Python built in method

input = ['p', 'y', 't', 'h', 'o', 'n']
print(''.join(input))