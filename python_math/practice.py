# print("Python math")
#.................built-in functions................
# x=min(30,10,83)
# y=max(30,10,83)
# print(x)
# print(y)

# z=abs(-0.78)
# print(z)

# p=pow(2,4)
# print(p)


# #exercise :find the result before running the code:
# numbers = [-10, 3, -7, 15, -2]

# a = min(numbers) #-10
# b = max(numbers)  #15
# c = abs(a) #10
# d = pow(b, 2) #225

# print(a + b + c + d)
# #-10+15+10+225=240

#.................math module................

import math

x=math.sqrt(64)
y=math.ceil(5.4) #round updward
z=math.floor(5.4) #round downward
c=math.pi

print(x)
print(y)
print(z)
print(c)

#exercise

a = math.sqrt(144) #12
b = math.ceil(7.3) #8
c = math.floor(7.9)#7
d = math.pi #3.14

print(round(d, 2) + a + b + c) #30.14
