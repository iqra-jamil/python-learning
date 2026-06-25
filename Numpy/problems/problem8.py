# # 8. Create a 5×5 array, extract the inner 3×3 submatrix (not the border).
import numpy as np
rng=np.random.default_rng()
my_arr=rng.integers(low=0,high=100,size=25).reshape(5,5)
print(my_arr[1:4,1:4])