# 2. Create a 3×3 matrix of zeros, then replace the diagonal with 1s (without using `eye()`).

import numpy as np
my_arr=np.zeros((3,3),dtype=int)
print(my_arr)
np.fill_diagonal(my_arr,np.ones(3))
print(my_arr)
