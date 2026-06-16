# Python Datetime

- what is date object in python??
  a date object in python represent calender date(year,month,day) without any time information
- it comes from datetime module in py

# Python Dates

- date is not a datatype in python
- so we import it from a module name datetime to work with dates as date objects
- datetime module is a standart built-in library in python.
- import the module datetime
- and use datetime.datetime.now() or datetime.datetime.today() to dispaly current date and time
- .now us more flexible cz it accept timezone (tz) as a parameter

# about datetime class inside module:

- we have datetime class inside datetime module
- that is why we were using datetime.datetime.method() (to avoid this import the class from module)
- .now,.today are the methods provided by datetime class we have inside module

## classes we have inside datetime module

to use these classes import them from the module frst

- datetime.date (have year,month,day) represent calender date
- datetime.time (have hour, minute, second, microsecond, tzinfo) represnt time
- datetime.datetime(have all the attributes of date & time) represnt combo of date & time
- datetime.timedelta: we use it to represent duaration between two dates/times,so we can add/subtract days,time(hours,second etc) from a date
- datetime.tzinfo Used to implement custom time zone adjustments.
- datetime.timezone (have offset, name) subcalss of tzinfo for fixed UTC offsets

### timedelta supports days, seconds, microseconds, milliseconds, minutes, hours, and weeks

# Creating Date Objects

- to craete date we can use datetime() class(constructor) of the datetimemodule
- The datetime() class requires three parameters to create a date: year, month, day.
- The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

# The strftime() Method

- instance method of datetime/date/time classes
- we can format the date and time using strftime() method it take only one paramter,format,to specify the format of the returned string
- its a method of datetime class to format date objects into raedable strings
- works on datetime class and date class bcz they give us actual date/time values
- this method wrks on any calss that give the actual time /date values
- for details we can see https://www.w3schools.com/python/python_datetime.asp
