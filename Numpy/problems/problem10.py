# 10. Create two 3×3 matrices and perform element-wise multiplication, then matrix multiplication  store both results.
import numpy as np

arr_1=np.arange(1,10).reshape(3,3)
arr_2=np.arange(11,20).reshape(3,3)

matrix_multiplication=arr_1 @ arr_2
element_wise=arr_1*arr_2

print(matrix_multiplication)
print(element_wise)