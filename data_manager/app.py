import json
default_data={
      "user3":{
        "id": 2,
         "name": "sara",
        "age": 26,
        "student": True,
        "hobbies": [
            "cooking",
            "climbing",
            "collecting coins"]
      }
      # or data={}
   }
#.................loading data...................................
File_loaded=False
data={}
def load_data():
 global File_loaded
 global data
 try:
    with open("users.json","r") as f:
     data=json.load(f)
     print(data)
     File_loaded = True
     print("loading from file")
 except FileNotFoundError: #to be specific
   print("file not found")
   data=default_data.copy()
   print("loading default")
 except Exception as e:
   print("broken",e)
   data=default_data.copy()
   print("loading default")
load_data()
#.................adding new users..................................
##############harcodede################################################
# data['user4']={'id':2,'name':'ali','age':32,'student':False, 'hobbies': [
#             "traveling",
#             "music",
#             "coding"
#         ]}
# # data.update(user4)

# user5={'id': 3,'name':'ja','age':38,'student':False, 'hobbies': [
#             "traveling",
#             "dancing",
#             "coding"
#         ]}
# user6={ 'id': 4,'name':'ij','age':23,'student':True, 'hobbies': [
#             "traveling",
#             "dancing",
#             "coding"
#         ]}

# #data.update(user5) only keys not as a whole entry
# data['user5']=user5
# data["user6"]=user6
#adding user by function
def add_user(key,dict_value):
  #key name ko dictionary as a value assign ho jay
  data[key]=dict_value
#function call
add_user('user7',{'id': 7,'name':'iquu','age':23,'student':True, 'hobbies': [
             "traveling",
             "dancing",
             "coding"
        ]})
  
#.................remove the user.................................
###hard coded
# def remove_user():
#   #remove user2 we can use .pop to reomev a user
#  data.pop("users2")
# #we can also remove wrong keys we added using .update 
#  data.pop("name")
#  data.pop("age")
#  data.pop('student')
#  data.pop("hobbies")
# #remove_user()
##function to remove user
def remove_user(user):
    data.pop(user)
#remove_user('user4')
#.................chk type of age ..................................
age=None
def age_format():
 try:
   global age
   age=int(input("enter your age :"))
   print("entered age is",age)
 except Exception as e :
   print(e)
 else:
   data["user3"]["age"]=age
 finally:
   print("passed try/except")
age_format() 
##.................update a user's data..................................
data["user3"]["student"]=True
data["user3"]["hobbies"][2]="coins"

print(data)


##.................find user by Id..................................
def find_user():
 my_id=int(input("enter id : "))
 Found_User=None
 for user in data.values():
   if user["id"]==my_id:
      Found_User=user
 print(Found_User)
find_user()
##.................writing backj to file ..................................
def write_data():
 if File_loaded:
  with open("users.json","w" ) as f:
    json.dump(data,f,indent=4)
 else:
   print("file was broken, skipped saving to protect data")
write_data()
print("alll done.............!!!!!!!!!")

##.................NOTES.................................
#error handling like file dosnt exist , if  file doent exist data will never load/assign 
# if it will not be assigned then it will be undefibned and throw NameError
# data never assigned means the object we are modifying like user3 will also throw keyerror
# handle them in except block by assigning data base data in case of file dont exist
#broken json file is already handled in frst try except but its overriting the existing data with default_data in case of broken file exception to handle that write data only in case file is loaded

# # user say input int main len gay or agr wo input int main na hoe to valueError exception aay ge

#we can use .update() but it will add only keys in the file 
# or we can diretly assign new value to data object to add a new user in dict(it will add user as a whole entry)
#we can use .append() in case of list

##.................the improvements we can do..................................
#take a number from user and run functions on the base of that
#instead of hardcoding we can remove a user dynamically by looping over users and taking input form user by finding id


