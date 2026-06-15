print("iterators")
num=[1,2,3]
it= iter(num)
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) will raise StopIteration error

mytuple = ("apple", "banana", "cherry")
it= iter(mytuple)
print(next(it))
print(next(it))
print(next(it))
#print(next(it))


# create a class define iter and next methods inside the class give inital value to a varaible in iter method and define some opeeartion in next method the create an object for the class and then call iter and next function on object

class myNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if(self.a<=3):
          x=self.a
          self.a+=1
          return x
        else:
           raise StopIteration
class MyEvenNumbers:
   def __iter__(self) :
      self.even=2
      return self
   def __next__(self) :
     if(self.even<=20):
        y=self.even
        self.even+=2
        return y
     else:
        raise StopIteration

myclass=myNumbers()
myObj=MyEvenNumbers()
myEvenItr=iter(myObj)
myIter=iter(myclass)
print("even",next(myEvenItr))
print("even",next(myEvenItr))
print("even",next(myEvenItr))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

#generator
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))  # 1
print(next(g))  # 2


## List comprehension
[x * 2 for x in range(10)]

## Generator expression it's just a shorthand way to create a generator without writing a full function.
(x * 2 for x in range(10))

## Dict comprehension
{x: x * 2 for x in range(10)}

## Set comprehension
{x * 2 for x in range(10)}
## To make a tuple, we wrap a generator with tuple()
tuple(x * 2 for x in range(10))  # (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)

g = (x * 2 for x in range(5))

print(next(g) ) # 0
print(next(g))  # 2