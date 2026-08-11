#----------------------------------------#
'''
Question 18
Level 3

Question:
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
# Abc123$,abc123$,ABC123$,Abc123,Ab1$
import re
# ()-->generator
# []--> list comprehension
# (expression for item in iterable if condition)
#re.search(pattren we want to search, string we want to search in)



user_password=input("enter different passwords").split(",")
for password in user_password:
 if(len(password)>=6 and len(password)<=12):
     if(re.search("[a-z]",password) and re.search("[0-9]",password) and re.search("[A-Z]",password) and re.search("[$#@]",password)):
         print(password)
    





















































###### just to revise functions syntax


# def chk_password_len(password):
#     if(len(password)<6):
#         return 'Invalid: Password must be at least 6 characters long'
#     elif(len(password)>12):
#          return "Invalid: Password cannot be longer than 12 characters."
#     else:
#         return "valid length"
# print(chk_password_len("2We3345"))