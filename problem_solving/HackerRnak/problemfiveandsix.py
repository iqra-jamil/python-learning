n= int(input())
my_list=[]
i=1
while i<=n:
  print(i)
  my_list.append(i)
  i+=1
 

result="".join(map(str,my_list))
print(result)

# the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

user_string=input("Enter a string")
user_substring=input("Enter a substring")

print(len(user_string))

my_count=user_string.count(user_substring,0,len(user_string))
print(my_count)