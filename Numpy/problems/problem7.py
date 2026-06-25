# 7. Given a 1D array, normalize it so all values fall between 0 and 1.
import numpy as np
my_list=[[2, 5, 10]]
my_arr=np.array(my_list)
#formula (value - min) / (max - min)

normalization=((my_arr-np.min(my_arr))/(np.max(my_arr)-np.min(my_arr)))
print(normalization)


# NumPy applies the operation to every element automatically — that's broadcasting. my_arr - min subtracts min from each element at once.