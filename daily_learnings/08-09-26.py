#creat a class
"""class Student:
    pass

student1=Student()

#add attributes
student1.name="lana"
student1.age=12

#show screen
print("my pet name is",student1.name)
print("age is", student1.age )

#use __init__
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
student1=Student("lana",12)
student2=Student("jee",0.8)
#show value
print(student1.name,student1.age)
print(student2.name)"""

#dog class + methods
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(self.name,"is barking")

dog1=Dog("lana",8)
print("name",dog1.name)
print("age",dog1.age)

dog1.bark()          
  


    