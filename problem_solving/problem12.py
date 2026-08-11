#Question 12
#Level 2

#Question:
#Write a program, which will find all such numbers between 1000 and 3000
#(both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.

val=[]

for i in range(1000,3001):
   my_num= str(i)
   if(int(my_num[0])%2==0 and int(my_num[1])%2==0 and int(my_num[2])%2==0 and int(my_num[3])%2==0):
     val.append(i)

print(val)
print(','.join(str(x) for x in val))