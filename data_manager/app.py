import json


with open("users.json","r") as f:
    data=json.load(f)
    print(data)
data['user4']={'name':'ali','age':32,'student':False, 'hobbies': [
            "traveling",
            "music",
            "coding"
        ]}
# data.update(user4)

user5={'name':'ja','age':38,'student':False, 'hobbies': [
            "traveling",
            "dancing",
            "coding"
        ]}
user6={'name':'ij','age':23,'student':True, 'hobbies': [
            "traveling",
            "dancing",
            "coding"
        ]}
#data.update(user5) only keys not as a whole entry
data['user5']=user5
data["user6"]=user6
 #remove user2 we can use .pop to reomev a user
#data.pop("users2")
#we can also remove wrong keys we added using .update 
#data.pop("name")
# data.pop("age")
# data.pop('student')
# data.pop("hobbies")
#update a user
data["user3"]["student"]=True
data["user3"]["hobbies"][2]="collecting coins"
print(data)
#we can use .update() but it will add only keys in the file 
# or we can diretly assign new value to data object to add a new user in dict(it will add user as a whole entry)
#we can use .append() in case of list
with open("users.json","w" ) as f:
    json.dump(data,f,indent=4)