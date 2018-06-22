#Q1
f=open("file.txt",encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("enter number of lines you want to print"))
for i in range(0,n):
    print(a[i])
f.close()

#Q2
a="i"
f=open("file4.txt","r")
k=f.read()
m=k.split()
print(k.count(a))

#Q3
f=open("file.txt",encoding="utf8")
f1=open("file2.txt","w")
for story in f:
    f1.write(story)
f.close()

#Q4
i=0
f=open("file2.txt",encoding="utf8")
a=(f.readlines())
b=open("file4.txt",encoding="utf8")
c=(b.readlines())
d=open("file3.txt","w")
for i,j in zip(a,c):
    d.write(i+j)
f.close()
b.close()
d.close()

#Q5
import random
l=[]
a=int(input("enter a number"))
l.append(a)
print(l)









