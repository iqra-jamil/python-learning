# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# 1.	Take number of students and then take naes and gardes till there
# 1 .names ->as input in string
# 2.	grades -> as input in int (total grades not seprate)
# 3.	store them as nested lists using zip
# 4.	find min(marks) and eliminate that and get the other min(marks) print taht
# 5.	if there are dublicates of 2md min(marks ) then sort them alphabetically 

number_of_student=int(input("enter number of students : "))
names_list=[]
students_list=[]
for i in range(0,number_of_student):
    names_of_students=input("Enter names of students")
    names_list.append(names_of_students)
    grades_of_students=int(input("Enter grades of students"))
    students_list.append(grades_of_students)
zipped_list=list(zip(names_list,students_list))
joined_list=[]
for item in zipped_list:
         list_item=list(item)
         joined_list.append(list_item)
print(joined_list)
new_list=[]
#syntax:lambda arguments:expressions
lowest_grade = min(joined_list, key=lambda item: item[1])
print(lowest_grade) 
sort_list=[]
for item in joined_list:
    if lowest_grade[1]<item[1]:
       new_list.append(item[1])
for item in joined_list:
    if min(new_list)==item[1]:
       print(sort_list.append(item[0]))
  
sort_list.sort()
print(sort_list)

for name in sort_list:
    print(name)
         
   
#--------------optimized solution------------------------------------------
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
number_of_student=int(input("enter number of students : "))
names_list=[]
students_list=[]
for i in range(0,number_of_student):
    names_of_students=input("Enter names of students")
    names_list.append(names_of_students)
    grades_of_students=int(input("Enter grades of students"))
    students_list.append(grades_of_students)
zipped_list=list(zip(names_list,students_list))
joined_list=[list(item) for item in zipped_list]
print(joined_list)
lowest_grade = min(joined_list, key=lambda item: item[1])
filtered_list= [item for item in joined_list if item[1]!=lowest_grade[1]]

print(filtered_list)
second_lowest=min(filtered_list,key=lambda item:item[1])
print(second_lowest)
result=[item for item in filtered_list if second_lowest[1]==item[1]]
result.sort()
for name in result:
  print(name[0])



 



