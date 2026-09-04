# Task
# Given an integer,n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird
# Input Format
# A single line containing a positive integer, .
# Constraints
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

num=int(input("Enter a num"))
if(num%2!=0) :
    print("Weird")
if(num%2==0) and 2<= num <=5 :
    print("Not Weird")
if(num%2==0) and 6<= num <=20 :
    print("Weird")
if(num%2==0) and num>20 :
    print("Not Weird")


