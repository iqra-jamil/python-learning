# try:
#  age=int(input("enter your age "))
#  print(f"hellow {age}")
# except ValueError:
#  print("eror")


#searching users (find user by id)
my_dict={"user1":{'name':'iqra' ,'id':0},"user2":{'name':'jay' ,'id':1}}
my_id=int(input("enter id:"))

user_found=None
for user in my_dict.values():
  if user["id"]==my_id:
   user_found=user
print(user_found)
print(my_dict)
def remove_user(user):
  my_dict.pop(user)
remove_user("user1")
print("after",my_dict)