import requests
from dotenv import load_dotenv
import os
load_dotenv()
city_name=input("enter city name :")
API_KEY = os.getenv("API_KEY")
#/weather endpoint accept only GET request
API_URL=f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city_name}&units=metric" #python f strings
response =requests.get(API_URL)
print("status code", response.status_code)
data=response.json()
if(data['cod']=='404'and data['message']=='city not found'):
    print("city not found")
elif(data['cod']==200):
 print("City",city_name)
 #print("MY_DATA",data)
 #print('msg',data['message'])
 #print("MY_DATA_keys",data.keys())
 temp=data['main']['temp']
 humadity=data['main']['humidity']
 print(f"Temprature:{temp}\u00b0C")
 print(f"Humadity:{humadity}\u0025",)
 print("Wind degree",data['wind']['deg'])
else:
   print("something went wrong")








##POST request
# payload={'name':'iqra','student':True}
# API_URL=f"https://httpbin.org/post"
# response=requests.post(API_URL,json=payload)

# print("status code", response.status_code)
# my_data=response.json()
# print("iqra data",my_data)
# print("name",my_data['json']['name'])
# print("is_student",my_data['json']['student'])
# print(my_data['headers']['Content-Length'])