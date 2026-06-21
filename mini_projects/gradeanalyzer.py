print("grde analyzer")

number=int(input("how many students you want to add : "))
# calculate average marks
def average_marks(marks):
  return sum(marks)/len(marks)
name_list=[]
avrgmarks_list=[]
result_list=[]
#for loop on names,marks average marks
for i in range(number):
 #get names & marks
 student_name=input("enter the name of student : ")
 student_marks=input("enter the marks of student : ").split(",") #by default space 
 int_marks=list(map(int,student_marks))
 #average marks
 avg_marks=average_marks(int_marks)
 #make list of names and average marks
 name_list.append(student_name)
 avrgmarks_list.append(avg_marks)

#chek pass/fail
 if(avg_marks>33):
    print(f"congratulations {student_name} you got {avg_marks}")
    result_list.append("Pass")
 else:
    print(f"hard luck {student_name} you got {avg_marks}")
    result_list.append("Fail")

#summary
print("student name list",name_list)
print("student avg marks list",avrgmarks_list)
summary=list(zip(name_list,avrgmarks_list,result_list))
print(summary)


