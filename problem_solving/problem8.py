#----------------------------------------#
#Question 8
#Level 2

#Question:
#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

sequence=input("Enter a comma separated sequence of words : ").split(",")
sequence.sort()
print(sequence)

# sort dont return anything it modify orginal sequence,so we cant store its reults in a variable