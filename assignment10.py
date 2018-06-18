#Q1
class Animal:
    def animal_attribute(self):
        print("this animal has a tail")
class Tiger(Animal):
    def animal_type(self):
        print("it is our national animal")
x=Tiger()
x.animal_attribute()

#Q2
#result:
#AB
#AB


#Q4
class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        area=(self.length*self.breadth)
        print(area)
class Rectangle(Shape):
    def area(self):
        area=(self.length*self.breadth)
        print("area of rectangle is")
        print(area)
class Square(Shape):
    def area(self):
        area=(self.length*self.breadth)
        print("area of square is")
        print(area)
r=Rectangle(3,6)
s=Square(6,6)
r.area()
s.area()





