#Q1
i=0
while(i<10):
    num=input("enter a no.")
    i=i+1
    print("entered no. is" +num)

#Q2
while True:
    print("infinite")

#Q3
num=[]
sq=[]
for i in range(0,5):
    x=int(input("enter a no."))
    num.append(x)
    sq.append(x*x)
print(num,sq)

#Q4
i=0
l=[1,2,"lovisha",0,8,4,2]
a=[]
b=[]
c=[]
for i in l:
    if(type(i)==int):
        a.append(i)
    elif(type(i)==str):
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)

#Q5
for i in range(1,101):
    x=int(input("enter a no."))
    if(x%2==0):
        print("the no. is even")
    else:
        print("the no. odd")

#Q6
k=4
for i in range(0,k):
    for j in range(0,i+1):
        print("*",end='')
    print("\r")

#Q7
d={'name':'lovisha',
   'age':20}
for i in d:
    print(d[i])

#Q8
i=0
l=[]
while(i<5):
    n=int(input("enter a no."))
    l.append(n)
    i=i+1
n=int(input("enter a no. to be searched"))
for i in l:
    if(n==i):
        l.remove(i)
print(l)









