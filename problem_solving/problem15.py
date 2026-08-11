#Question 15
#Level 2

#Question:
#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program: 9
#Then, the output should be:
#11106

user_input=int(input("enter a digit"))
# a,a*2,a*3,a*4
#a*a=aa
one_digit=user_input
two_digits=str(user_input)*2
three_digits=str(user_input)*3
four_digits=str(user_input)*4

result=int(one_digit)+int(two_digits)+int(three_digits)+int(four_digits)
print(result)

