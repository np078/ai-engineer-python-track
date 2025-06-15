'''
Q15: Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
# Solution

# My Raw Logic Solution but it was not accurate for the months that have 31 or 28 days as well as for the leap year
date1 = (2014,7,2)
date2 = (2014,7,11)

y=date1[0] - date2[0]
m=date1[1] - date2[1]
d=date1[2] - date2[2]

result = (y*365) + (m*30) + d
print("The number of days between two given dates are: ", abs(result)) 

# Using datetime module
from datetime import date

date1 = date(2014,7,2)
date2 = date(2014,7,11)

result = date2 - date1

print("NUmber of days between: ", result.days)