
# OOPs:- OBJECT ORIENTED PROGRAMMING 
# this concept of OOPS focusses on using REUSEABLE CODE (DRY Principle)
# A CLASS is a blue print of OBJECT
# from one class we can make many objects 

# syntax of creating class:
class Employee: #when a class is defined an empty stucture of object has been created
    
    language = "Py" #this is a class attribute
    salary = 2000000

Muskan = Employee()  #here an object has been created 
print(Muskan.name,Muskan.language)

sukoon = Employee()
print(sukoon.salary,sukoon.language)

rohan = Employee()
rohan.name= "Rohan roro rombson" #this is an object/INSTANCE attributes 
rohan.language= "Javascript"  
print(rohan.name,rohan.language)
# Here name is object attribute and salary and language are class



# SELF PARAMETER

class Emp:
    language= "python"
    salary= 300000
    def getinfo(self):  #here we can create a function in a class
        print(f"the language is {self.language}. the salary is {self.salary} ") #here we have taken self as a parameter
    @staticmethod  # we have setted this funnction into static coz we don't want any instance attribute or data from the object
    def greet():
        print("Good morning")


harry = Emp()
harry.language = "Javascript"  
harry.getinfo() #below is the another way of writing this 
#Emp.getinfo(harry)
harry.greet()



# __INIT__() CONSTRUCTOR
class emp:
    def __init__(self):   #dunder method which is automatically called when you make any object
        print("I am creating an object")

harry= emp()   #here when we created an object the __init__() func automatiically has been called
print(rohan.salary)