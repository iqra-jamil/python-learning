# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# The first line contains the integer n , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.


number_of_students=int(input("add Number of students"))
print(number_of_students)
names_list=[]
marks_list=[]
for i in range(number_of_students):
   # names of students
   names_of_students=input("add Name of students")
   names_list.append(names_of_students)
   # marks of a student
   marks_of_student=list(map(int,input("enter marks").split()))
   print(marks_of_student)
   marks_list.append(marks_of_student)
print(marks_list)
print(names_list) 
joined_lists=list(zip(names_list,marks_list))
print(joined_lists)

query_name=input("Enter query name :")
for item in joined_lists:
    if query_name==item[0]:
       avg_marks=(sum(item[1])/len(item[1]))
       print(avg_marks)



   
