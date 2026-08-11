'''
Question:
Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.
'''

# range(0,n+1)
#iterate wo numbers karny hain jo n%7==0 den
n=int(input("enter the value of n"))
class my_class:
 def my_gen(self):
    for i in range(0,n+1):
      if(i%7==0):
          yield i
obj=my_class()

for num in obj.my_gen():
   print(num)
