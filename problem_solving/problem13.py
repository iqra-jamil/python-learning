#Question:
#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3
user_sentence=input("enter a sentence")
alpha_count=0
digit_count=0
for i in user_sentence:
    if (i.isalpha()):
       alpha_count+=1
    if(i.isdigit()):
       digit_count+=1
print("Letters : ",alpha_count)
print("digit : ",digit_count)
