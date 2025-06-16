# Q24: Write a Python program to test whether a passed letter is a vowel or not.

text = input("Enter a letter: ")
vowel = ['a', 'e', 'i', 'o', 'u']

if text in vowel: 
       print(f"The letter {text} is a vowel.")
else:
    print(f"The letter {text} is not a vowel")