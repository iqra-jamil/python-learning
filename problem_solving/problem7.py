#----------------------------------------#
#Question 7
#Level 2

#Question:
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


X=int(input("Enter X"))
Y=int(input("Enter Y"))

outer_list=[]
for i in range(X): #0,1,2
    temp_row=[]
    for j in range(Y): #0,1,2,3,4
        results= i*j #0*0,0*1,0*2,0*3,0*4=0,0,0,0,0
        temp_row.append(results)
    outer_list.append(temp_row)
print(outer_list)











#0*0,0*1,0*2,0*3,0*4=0,0,0,0,0
#1*0,1*1,1*2,1*3,1*4=0,1,2,3,4
#2*0,2*1,2*2,2*3,2*4=0,2,4,6,8
#result is storing"
# 0 j's frst iteration i=0
# 0 j's second iteration i=0
# 0 j's third iteration i=0
# 0 j's fourth iteration i=0
# 0 j's fifth iteration i=0
# 0 j's frst iteration i=1
# 1 j's second iteration i=1
# 2 j's third iteration i=1
# 3 j's fourth iteration i=1
# 4 j's fifth iteration i=1
# 0  i=2
# 2  i=2
# 4  i=2
# 6   i=2
# 8   i=2