# Q16: Write a Python program to get the volume of a sphere with radius six.

# Solution

from math import pi
r = 6
vol = (4/3) * pi * (r ** 3)
print("The volume of the sphere: ",round(vol, 2), "cm³")
