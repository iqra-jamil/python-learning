#----------------------------------------#
#Question 10
#Level 2

#Question:
#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world

sequence=input("Enter a sequence of whitespace separated words ").split()
print(type(sequence))
remove_duplicates=set(sequence)
print(remove_duplicates)
sorted_sequence=sorted(remove_duplicates)
print(sorted_sequence)
#now join the comma separated words using empty space with join()
results= " ".join(sorted_sequence)
print(results)
#to sort any iterble like set use sorted( ) not sort


# or
X = [i for i in input("Enter sentence:").split(" ")]
print(" ".join(sorted(list(set(X)))))