# 9. Given a 1D array of integers, replace all even numbers with 0 using boolean masking.
import numpy as np
my_arr=np.arange(1,10)

print(my_arr)

mask=my_arr%2==0

my_arr[mask]=0
print(my_arr)