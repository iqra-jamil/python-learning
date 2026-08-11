#Question 16
#Level 2

#Question:
#Use a list comprehension to square each odd number in a list.
#The list is input by a sequence of comma-separated numbers.
#Suppose the following input is supplied to the program:
#1,2,3,4,5,6,7,8,9
#Then, the output should be:
#1,9,25,49,81


### with comprehension
user_list=input("enter comma seprated integers").split(",")
newlist=[int(i)**2 for i in user_list if(int(i)%2!=0)]
#[print ,for loop ,if statemnt]
print(",".join(str(x) for x in newlist))




### without comprehension
#user_list=input("enter comma seprated integers").split(",")
# for i in user_list:
#     int(i)
#     if(int(i)%2!=0):
#         #print(pow(int(i),2))
#         print((int(i)**2))