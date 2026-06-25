# 6. Stack two 2×3 arrays vertically and two 2×3 arrays horizontally.
import numpy as np
arr_1=np.arange(0,6).reshape(2,3)
arr_2=np.arange(10,16).reshape(2,3)
#use vstack to stack them vertically
print(np.vstack((arr_1,arr_2))) 

#vstack takes only one argumnt not 2 so use dbl round brackets

#use vstack to stack them vertically horizontally
print(np.hstack((arr_1,arr_2))) 
