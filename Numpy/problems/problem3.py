# 3. Create two 1D arrays of 5 random integers each, then find their dot product.
import numpy as np
# arr_1=np.array([2,5,7,8,9])
# arr_2=np.array([89,7,24,56,8])
rng=np.random.default_rng()
arr_1=rng.integers(low=1,high=100,size=5)
arr_2=rng.integers(low=1,high=100,size=5)
product=np.dot(arr_1,arr_2)
print(product)