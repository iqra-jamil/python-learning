# problem 3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#problem 4
year=input()
def is_leap(year) :
 if year%400==0  :
   return True
 elif year%100==0 :
   return False
 elif year % 400==0:
    return True
 else:
   return False
is_leap(2000)




