# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.


# The first line contains n. The second line contains an array  A[] of  integers each separated by a space.

#using numpy
import numpy as np
n=int(input("Enter number of players"))
rng=np.random.default_rng()
int_arr=rng.integers(low=1,high=10 ,size=n)
new_list=[]
for index,value in enumerate(int_arr):
  if(value<max(int_arr)):
     new_list.append(value)
print(max(new_list))
# without numpy 
import random
int_arr=[]
new_list=[]
n=int(input("Enter number of players"))
for i in range(0,n):
   rand_arr=random.randint(1,10)
   int_arr.append(rand_arr)
print(int_arr)

for index,value in enumerate(int_arr):
  if(value<max(int_arr)):
     new_list.append(value)
print(max(new_list))

#---------------------------------
int_arr=[]
new_list=[]
n=int(input())
int_arr = list(map(int, input().split()))

for index,value in enumerate(int_arr):
    if(value<max(int_arr)):
        new_list.append(value)
print(max(new_list))




