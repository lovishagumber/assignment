#Q1
try:
    a=3
    if a<4:
     a=a/(a-3)
     print(a)
except (ValueError,ZeroDivisionError):
    print("enter only integer and should not be zero")


#Q2
# It is Index error
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("enter correct index value")


#Q3
#An exception


#Q4
#-5.0
#a/b result in 0


#Q5
try:
    import lovisha
except ImportError:
    print("enter a valid import file")

try:
    import threading
except ImportError:
    print("enter a valid import file")

try:
    a=int(input("enter a number"))
except ValueError:
    print("enter a integer number")

try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("enter correct index value")

try:
    l=[1,2,3]
    print(l[2])
except IndexError:
    print("enter correct index value")

#Q6
class AgeTooSmall(Exception):
    pass
a=True
while(a):
    try:
        age=int(input("enter age"))
        if(age>=18):
            a=False
            raise AgeTooSmall
        else:
            print(age)
    except AgeTooSmall:
        print("age is greater than 18")
    except ValueError:
        print("enter an integer value")


