#for one student only
student_names=input("enter the names of student")
student_marks=input("enter the marks of student").split(",") #by default space 
marks_int=list(map(int,student_marks))
print(student_names)
#print(len(marks_int))
def average_marks(marks):
   return sum(marks)/len(marks)
avg_marks=average_marks(marks_int)
print("the average marks of this student are",avg_marks)

if(avg_marks>33):
   print(f"congratulations {student_names} you got {avg_marks}")
else:
   print(f"hard luck {student_names} you got {avg_marks}")