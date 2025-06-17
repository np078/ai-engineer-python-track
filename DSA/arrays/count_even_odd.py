# Q3: Count Even and Odd Numbers

def count_even_odd(arr):
   even_count = 0
   odd_count = 0

   for i in arr:
    if i%2 == 0:
      even_count +=1
    if i %2 != 0:
      odd_count +=1

   return even_count, odd_count
   
arr = [1, 4, 5, 6, 7, 10]
e_count , o_count = count_even_odd(arr)
print("Even:", e_count)
print("Odd:", o_count)
