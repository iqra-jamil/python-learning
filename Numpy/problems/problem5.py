# 5. Create a 4×4 array of random integers (1–100), then find the max value in each row.
import numpy as np
#my_arr=np.random.default_rng().integers(low=1 ,high=101 ,size=100)
rng=np.random.default_rng()
my_arr=rng.integers(low=1,high=101 ,size=16).reshape(4,4)
print(my_arr)
# for i in range(len(my_arr)):
#  print(my_arr[i].max())
print(my_arr.max(axis=1))
