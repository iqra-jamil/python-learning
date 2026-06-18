# # # Decorators + Context managers +Map + Filter + Zip + Dunder methods 

print( "Decorators")
def my_decorator(func):
    def wrapper():
       print("before function runs")
       func()
       print("after function runs")
    return wrapper

@my_decorator
def say_hello():
    print("hello world")

say_hello()


print( "Context managers")
with open("demo.txt","r") as f:
    data=f.read()

# # # print( "map(),filter(),zip()")
string_list=["1","2","3"]
results=list(map(int,string_list))
print(results)
#using for loop
my_list=[]
for i in string_list:
   results= int(i)
   my_list.append(results)
print(my_list)

# Exercise: Filter a list of numbers and keep only those greater than 10, then using map() square each of those numbers.
#### wrong
# import math
# nums = [3, 7, 12, 15, 6, 20]
# empty_list=[]
# def func():
#     for i in nums:
#         if(i>10):
#         # print(i)
#          res=i
#          empty_list.append(res)


# my_list=list(filter(func(),empty_list))
# map_it=list(map(math.sqrt,my_list))
# print(map_it)

nums = [3, 7, 12, 15, 6, 20]

def is_greater(num):
   return num>10 
# will return True or False filter will keep True and drop False  looping over nums will be handled by filter
filter_result=list(filter(is_greater,nums))
print(filter_result)

def sq(num):
    return num**2 #will return sq of each number

map_result=list(map(sq,filter_result))
print(map_result)

# # #filter decide which item to keep and map decide what to do for each item

# Exercise:Use zip() to combine these two lists, then use map() to add each pair of numbers together.

a = [1, 2, 3]
b = [10, 20, 30]

zip_res=list(zip(a,b))
# print(type(zip_res)) #zip
print(zip_res)

# def add_pair(i):
#     return sum(i)
def add_pair(pair):
    return pair[0]+pair[1]
# #print(add_pair(3,7))
final_res=list(map(add_pair,zip_res))
print(final_res)

#  exercise: Use zip() to combine these two lists, then use filter() to keep only the pairs where both numbers are greater than 5.
a = [6, 7, 2, 8]
b = [6, 4, 9, 10]

zip_res=list(zip(a,b))
print(zip_res)
# [(6, 6), (2, 9), (8, 10)]
def chk_pairs(pair):
    return pair[0] > 5 and pair[1] > 5
final_res=list(filter(chk_pairs,zip_res))
print(final_res)



# 2:57 AM
# Exercise:Use zip() to combine these two lists, then use filter() to keep only pairs where both numbers are even, then use map() to add each pair together.

a = [2, 3, 4, 7, 8]
b = [6, 5, 2, 4, 10]
#zip
zip_res=list(zip(a,b))
print(zip_res)
#filter
def even_pair(pair):
    return pair[0]%2==0 and pair[1]%2==0
filter_res=list(filter(even_pair,zip_res))
print(filter_res)
#map
def add_pairs(pair):
    return pair[0] +pair[1]
map_res=list(map(add_pairs,filter_res))
print(map_res)

#exercise: Use zip() to combine these two lists, then use filter() to keep only pairs where the sum of both numbers is greater than 15, then use map() to return the difference (larger minus smaller) of each kept pair.

a = [3, 10, 8, 14, 6]
b = [12, 7, 9, 5, 11]
#zip
zip_res=list(zip(a,b))
print(zip_res)

def filter_zip(pair):
   return pair[0]+pair[1] > 15
filter_res=list(filter(filter_zip,zip_res))
print(filter_res)
# [(10, 7), (8, 9), (14, 5), (6, 11)]
def map_filteredlist(pair):
    return max(pair)-min(pair)
#   if(pair[1] > pair[0]):
#      return pair[1]- pair[0]
#   elif(pair[0]>pair[1]):
#      return pair[0]-pair[1]
    
map_res=list(map(map_filteredlist,filter_res))
print(map_res)