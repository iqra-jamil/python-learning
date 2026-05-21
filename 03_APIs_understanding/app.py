import requests
#GET request
response=requests.get('https://api.github.com')

# print(response.status_code)
# print("json",response.json()) #does the conevrsion behind the secene automatiaclly we dont need to sue json.load()
# print("text",response.text)#string
# print("content",response.content)#bytes
# print("header",response.headers)#extra details
# print("URl",response.url)#URl

# #POST request
# userdata={"name":"iqra", "student":True} #payload data
# #will craete a new post from our payload
# response=requests.post('https://jsonplaceholder.typicode.com/posts',json=userdata)
# print(response.json())
# #print("header",response.headers)
# print(response.text)
##PUT method
# userdata={"name":"iqra", "student":True} #payload data
# response=requests.put('https://jsonplaceholder.typicode.com/posts/5',json=userdata)
# print(response.json())


##PATCH method
# userdata={"name":"iqra jamil"} #payload data
# response=requests.patch('https://jsonplaceholder.typicode.com/posts/5',json=userdata)
# print(response.json())

##DELETE method
response=requests.patch('https://jsonplaceholder.typicode.com/posts/5?userId=5')
print(response.json())
print(response.headers)