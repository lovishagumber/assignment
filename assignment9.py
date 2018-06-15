#Q1
class Circle:
    def __init__(self,radius):
        self.r=radius
    def area(self):
        area=3.14*r*r
        return area
    def circumference(self):
        circumference=2*3.14*r
        return circumference
r=int(input("enter a radius"))
x=Circle(r)
print("area of circle is",x.area())
print("circumference of circle is",x.circumference())

#Q2
class Student:
    def __init__(self,a,b):
        self.name=a
        self.roll_number=b
name=input("enter your name")
roll_number=int(input("enter your roll number"))
x=Student(name,roll_number)
print(x.name)
print(x.roll_number)

#Q3
class Temperature:
    def __init__(self,celsius):
        self.C=celsius
    def fahrenheit(self):
        fahrenheit= C*9/5+32
        return fahrenheit
    def __init__(self,fahrenheit):
        self.F=fahrenheit
    def celsius(self):
        celsius=(F-32)*5/9
        return celsius
C=int(input("enter degree celsius"))
x=Temperature(C)
print("temperature in fahrenheit",x.fahrenheit())
F=int(input("enter degree fahrenheit"))
y=Temperature(F)
print("temperature in celsius",y.celsius())

#Q4
class MovieDetails:
    def __init__(self,a,b,c,d):
        self.movie_name=a
        self.artist_name=b
        self.year_of_releasing=c
        self.ratings=d
    def __update__(self,a,b,c,d):
        print("updated details")
        self.movie_name=a
        print(a)
        self.artist_name=b
        print(b)
        self.year_of_releasing=c
        print(c)
        self.ratings=d
        print(d)
x=MovieDetails("Race 3", "Salman Khan", "15/06/2018","**")
print(x.movie_name)
print(x.artist_name)
print(x.year_of_releasing)
print(x.ratings)
movie_name=input("enter movie name")
artist_name=input("enter aritist name")
year_of_releasing=int(input("enter the year"))
ratings=input("rate the movie")
y=MovieDetails(movie_name,artist_name,year_of_releasing,ratings)
y. __update__(movie_name,artist_name,year_of_releasing,ratings)


#Q5
class Expenditure:
    def __init__(self,expenditure,savings,total=0):
        self.e=expenditure
        self.s=savings
        self.t=0
    def display(self):
        print("total expenditure=",end="")
        print(self.e)
        print("total savings=",end="")
        print(self.s)
    def total_salary(self):
        self.t=self.e+self.s
    def display_salary(self):
        return self.t
n=int(input("enter the expenditure"))
m=int(input("enter savings"))
y=Expenditure(n,m)
y.display()
y.total_salary()
print("total salary=",end="")
print(y.display_salary())
