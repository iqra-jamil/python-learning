#----------------------------------------#
#Question 2
#Level 1

#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

#8*7*6*5*4*3*2*1
#n=8
#n*(n-1)(n-2)(n-3)(n-4)(n-5)(n-6)(n-7)
#n=4
#4.3.2.1
# or 1*2*3*4
# num k andr 1*2*3*4 aarhy hain jab loop chly ge to i =1/2/3/4 and 
# res=1 final res he hmy find krna h res=res*i i jo har baar incremnt ho ga 

# res=i*res
# res=1*1=1
# res=2*1=2
# res=3*2=6
# res=4*6=24
#stop i on n

# import math
# n=8
# print(math.factorial(n))
#using for loop
num=input("Enter a number : ")
find_fact=range(1,int(num)+1)
res=1
for i in find_fact:
     res=i*res
print(res)


#recursion

def fac(x):
    if (x>1):
        x = x * fac(x-1)       
    return x
        
number = int(input("Enter Number:"))
print(fac(number))