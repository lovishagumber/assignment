#Q1
f=open("file.txt",encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("enter number of lines you want to print"))
for i in range(0,n):
    print(a[i])
f.close()

#Q2
a="best"
f=open("file1.txt",'r')
b=f.read()
c=b.split()
print(b.count(a))

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
list=[]
sortedlist=[]
for i in range(0,10):
    list.append(random.randint(1,10))
f=open("random.txt","w")
for s in list:
    r="".join(str(s))
    f.write(r)
f.close()
f1=open("random.txt","r")
t=f1.read()
for u in t:
    if(u.isdigit()):
        v="".join(u)
        sortedlist.append(v)
sortedlist.sort()
w=open("sorted.txt","w")
w.write(str(sortedlist))
f.close()









