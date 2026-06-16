# print("Python Datetime")

from datetime import datetime,timezone,timedelta,date
# #curent date & time
# # x=datetime.datetime.today()
# x=datetime.today()
# print(x)#same for time
# print(x.year)
# print(x.day)
# print(x.month)

# #only date
# # x=datetime.date.today() #its comming from module
# x=datetime.today().date() #from class frst call today() and then extarct date
# print(x)
# #curent date & time(accept tz as a paarmeter)
# # x=datetime.datetime.now(tz=datetime.timezone.utc)
# x=datetime.now(timezone.utc)
# print(x)
# #timedelta
# today=datetime.today()
# print("today is",today)
# Future=today+timedelta(days=3)
# print("future strftime",Future.strftime("%B"))
# print("3 weeks later",Future)
# past=today-timedelta(weeks=3)
# print("3 days ago",past)

# create_date=datetime(2026,7,26) #year,month,date
# print(create_date)
# print(create_date.strftime("%B"))
# print(create_date.strftime("%m"))


# a simple age calculator
# today_date=datetime.now()
# current_year=today_date.year
# print(current_year)
# birth_year=int(input("enter your birth year :"))
# print(birth_year)
# current_age =current_year - birth_year
# print(current_age)

#Build a days left until New Year calculator 
# current_time=datetime.today()
# future_time=datetime(2027,1,1)

# until_now=future_time-current_time
# print(until_now)

# Build a birthday countdown 
birth_month=int(input("enter your birth month : "))
birth_day=int(input("enter you day : "))
today=datetime.today()
current_year=today.year
#use datetime() to combine them
user_birth=datetime(current_year,birth_month,birth_day)
final_result=user_birth-today
print("Your bithday will be after :" ,final_result)