# Q26:  Write a Python program to create a histogram from a given list of integers.
'''
What is a Histogram (in Coding Terms)?

A histogram is a visual representation of frequency — it shows how many times something appears.
In Python, you can simulate a text-based histogram using * symbols.

'''
def print_histogram(items):
    for i in items:
        print('*' * i)

values = [2,5,7]
print_histogram(values)


