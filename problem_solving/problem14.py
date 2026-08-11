#Question 14
#Level 2

#Question:
#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9
user_sentence=input("ENter a sentence")
upper_count=0
lower_count=0
for i in user_sentence:
    if(i.isupper()):
        upper_count+=1
    if(i.islower()):
        lower_count+=1
print("UPPER",upper_count)
print("lower",lower_count)