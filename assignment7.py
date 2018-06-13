#Q1
r=int(input("enter the radius"))
def area(a):
    a=22/7*r*r
    print(a)
area(22/7*r*r)

#Q2
def perfect(p):
    sum=0
    for i in range (1,p):
        if(p%i==0):
          sum=sum+i
    if(sum==p):
        return True
    else:
        return False
for i in range(1,1001):
    if perfect(i):
        print(i)

#Q3
def mult12(n):
    if(n==1):
        return 12
    else:
        return mult12(n-1)+12
for i in range(1,11):
    print(mult12(i))

#Q4
a=int(input("enter the number"))
b=int(input("enter its exponant value"))
def raise_to_power(a,b):
    if b==1:
        return a
    else:
        return(a*raise_to_power(a,b-1))
print('%d^%d=%d' %(a,b,raise_to_power(a,b)))

#Q5
def fact(f):
    if f==1:
        return 1
    g=(f*fact(f-1))
    return g
num=int(input("enter the number"))
h=fact(num)
d={num:h}
print(d)









