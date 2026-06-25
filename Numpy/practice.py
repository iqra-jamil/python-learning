print("Numpy")

import numpy as np
1d array
list1=[1,2,3,4,5]
#print(type(list1))
my_array=np.array(list1)
#print(type(my_array)) #multi dimenstional array nd array
print(my_array)

#store different datatypes in a list
list2=[1,2,"H",4.0,5]
my_array=np.array(list2 ,dtype=str)
print(my_array)

list3=[[1,2,3,4],[5,6,7,8],[9,1,2,0]]

my_array=np.array(list3)
print(my_array)
# so we can create an arary using arange() too,instead of craeting list frst
my_array=np.arange(1,7.0)
print(my_array)

#we can also create the shape of matrix using .reshape(rows,col)
my_array=np.arange(1,7).reshape(2,3)
print(my_array)

# generate 0's matrix #bydefalut float values deta h 0.0

my_array=np.zeros(10 ,dtype=int)
print(my_array)
#ones
my_array=np.ones(10 ,dtype=int)
print(my_array)
my_array=np.zeros((4,2),dtype=int)
print(my_array)
print(my_array.dtype) #int64 bits
print(my_array.itemsize)  # 8 aik elmnt 8 bytes ka hai
print(my_array[1][-2])
my_array=np.ones((4,2,3),dtype=int)
print(my_array)
print(my_array.ndim) # dimesnsion
print(my_array.shape) # order
print(my_array.size) # number of elemnts
print(my_array.dtype) #datatype #int64 64 bits space 1byte=8 bits
print(my_array.itemsize) # elemnt's memory size in bytes 
# #output of last one is 8 means aik elemnt 8 bytes ly rha h
my_List=[[1,3,4,6],[7,8,9,3],[6,8,6,9]]
my_arr=np.array(my_List)
print(my_arr[1,2])
print(my_arr[:,2])
## for better undersatnding on 12 we have 9
#c=    0 1 2 3 
## r=0 1 3 4 6 
## r=1 7 8 9 3 
## r=2 6 8 6 9 

# slicing in 1d array

my_list=[10,20,30,40,50,60,70,80,90]
oned_arr=np.array(my_list)
print(oned_arr[1:3])
print(oned_arr[1:6:2])
print(oned_arr[-1:-6:-2])
print(oned_arr[::2]) #pura array but with a step
print(oned_arr[::-1]) #in case of reverse indexing the 3rd parameter is compulsry

#slicing in 2d arrays
my_list=[[15,16,17],[25,26,27],[35,36,37],[45,46,47]]
twod_arr=np.array(my_list)
print(twod_arr[1, ]) #frst row
print(twod_arr[:,1]) #1st col
print(twod_arr[1:3,1:3])
print(twod_arr[1:3, ])
print(twod_arr[:,1:3])
##print(twod_arr[row_s:row_e,col_st:col_end])
print(twod_arr[1:3,1])
print(twod_arr[1:3,:1])
##Addition
list_1=[[1,2],
       [3,4]]
list_2=[[11,12]
       ,[13,14]]
arr_1=np.array(list_1)
arr_2=np.array(list_2)
res=arr_1+arr_2
print(res)

# ## subtarction
list_1=[[1,2],
       [3,4]]
list_2=[[11,12]
       ,[13,14]]
arr_1=np.array(list_1)
arr_2=np.array(list_2)
res=arr_2 - arr_1
print(res)

# ## multiplication

list_1=[[1,2],
       [3,4]]
list_2=[[11,12]
       ,[13,14]]
arr_1=np.array(list_1)
arr_2=np.array(list_2)
res=arr_1 * arr_2
print(res)

# #  matrix multiplication(@)
list_1=[[1,2],
       [3,4]]
list_2=[[11,12]
       ,[13,14]]
arr_1=np.array(list_1)
arr_2=np.array(list_2)
res=arr_1 @ arr_2
print(res)

# #  divison # will work same as *,+,- but ansers will be in float
list_1=[[1,2],
       [3,4]]
list_2=[[11,12]
       ,[13,14]]
arr_1=np.array(list_1)
arr_2=np.array(list_2)
res=arr_2 / arr_1
print(res)

# #Floor Divison(//) # will return only interger part(before point)
list_1=[[1,2],
       [3,4]]
list_2=[[11,12]
       ,[13,14]]
arr_1=np.array(list_1)
arr_2=np.array(list_2)
res=arr_2 // arr_1
print(res)
# # exponentation(**)
list_1=[[1,2],
       [3,4]]
list_2=[[11,12]
       ,[13,14]]
arr_1=np.array(list_1)
arr_2=np.array(list_2)
res=arr_2 ** arr_1
print(res)
# # Modulo(%)
list_1=[[1,2],
       [3,4]]
list_2=[[11,12]
       ,[13,14]]
arr_1=np.array(list_1)
arr_2=np.array(list_2)
res=arr_2 % arr_1
print(res)

# # transpose
list_1=[[1,2],
       [3,4]]
list_2=[[11,12]
       ,[13,14]]
arr_1=np.array(list_1)
arr_2=np.array(list_2)
res=arr_1.transpose()
print(res)

## sorting on 1d array
# #sort()
my_list=[2,7,4,9,3,5]
my_arr=np.array(my_list)
X=np.sort(my_arr)
print(X)
X=np.sort(my_arr) [::-1]
print(X)

# # #argsort()
my_list=[2,7,4,9,3,5]
my_arr=np.array(my_list)
X=np.argsort(my_arr)
print(X)

# # #arr_name.sort() (inplace sorting)
my_list=[2,7,4,9,3,5]
my_arr=np.array(my_list)
my_arr.sort()
print(my_arr)

# # # sorting in 2D arrays
my_arr=np.array([[12,15,11],
                 [25,24,26],
                 [34,33,35]])
X=np.sort(my_arr)#[::-1]
print(X)
# #column wise sorting
my_arr=np.array([[12,15,11],
                 [25,24,26],
                 [3,5,33]])
X=np.sort(my_arr,axis=0)
print(X)
# #getting indexres argsort() #column=0 #row=1

my_arr=np.array([[12,15,11],
                 [25,24,26],
                 [3,5,33]])
X=np.argsort(my_arr,axis=0) 
print(X)

# #arr_name.sort() #inplace sorting

my_arr=np.array([[12,15,11],
                 [25,24,26],
                 [3,5,33]])
my_arr.sort()
print(my_arr)

# Statistical operations on 1D Array
my_list=[2,7,4,9,3,5]
my_arr=np.array(my_list)
X=my_arr.sum() 
print(X)

my_list=[2,7,4,9,3,5]
my_arr=np.array(my_list)
X=np.max(my_arr) # same sum b
print(X)

my_list=[2,7,4,9,3,5]
my_arr=np.array(my_list)
X=np.var(my_arr) # saary same he way main execute hoty hain
print(X)