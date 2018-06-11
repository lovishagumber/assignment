#Q1
a=int(input("enter year"))
if(a%4==0):
    print("it is a leap year")
else:
    print("it is not a leap year")


#Q2
l=int(input("length"))
b=int(input("breadth"))
if(l==b):
    print("it is a square")
else:
    print("it is a rectangle")


#Q3
x=int(input("age of first person"))
y=int(input("age of second person"))
z=int(input("age of third person"))
if(x>y and x>z):
    print("x is oldest")
elif(y>x and y>z):
    print("y is oldest")
elif(z>x and z>y):
    print("z is oldest")
else:
    print("others have same age")
if(x<y and x<z):
    print("x is youngest")
elif(y<x and y<z):
    print("y is youngest")
elif(z<x and z<y):
    print("z is youngest")
else:
    print("others have same age")


#Q4
p=int(input("enter the points"))
if(p>1 and p<50):
    print(" sorry no prize")
elif(p>51 and p<150):
    print("get wooden dog")
elif(p>151 and p<180):
    print("book")
elif(p>181 and p<200):
    print("chocolates")
else:
    print("congratulations you won")


#Q5
q=int(input("enter the quantity"))
if(q*100>1000):
    print("discount is there"+str(q*100-0.10*q*100))
else:
    print(q*100)


