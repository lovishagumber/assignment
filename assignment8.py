#Q1
print("There is a popular time module available in python which provides function for working with time, and for converting between representations, "
      "the function (time.time()) returns the current system time in ticks since 12 am, january 1,1970(epoch)")
print("index  attribute  values"
      "0      tm_year    2018"
      "1      tm_mon     1 to 12"
      "2      tm_mday    1 to 31"
      "3      tm_hour    0 to 23"
      "4      tm_min     0 to 59"
      "5      tm_sec     0 to 61"
      "6      tm_wday    0 to 6"
      "7      tm_yday    1 to 366"
      "8      tm_isdst   -1,0,1")

#Q2
import time
print(time.asctime())

#Q3
import datetime
d=(datetime.date.today())
print(d.month)

#Q4
import datetime
d=(datetime.date.today())
print(d.day)

#Q5
import datetime
a='2021/01/11'
d=(datetime.datetime.strptime(a,"%Y/%m/%d"))
print(d.day)

#Q6
import time
print(time.asctime(time.localtime()))

#Q7
import math
f=int(input("enter a number"))
print(math.factorial(f))

#Q8
import math
a=int(input("enter a number"))
b=int(input("enter a number"))
print(math.gcd(a,b))

#Q9
import os
print(os.getcwd)
print(os.environ)



