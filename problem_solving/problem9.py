#----------------------------------------#
#Question 9
#Level 2

#Question£º
#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT
lines=int(input("how many sequence of lines you want to enter"))
my_list=[]
for i in range(1,lines+1):
 sequence=input("Enter sequence of lines : ")
 #print(sequence)
 results=sequence.upper()
 print(results)
 my_list.append(results)
print(my_list)
