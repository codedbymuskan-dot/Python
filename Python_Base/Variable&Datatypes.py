# VARIABLES DATATYPE 

a=5  #ASSIGNMENT OPERATOR 
b=4
c=a+b  #ARITHMETIC OPERATOR
d=a*b
print(c)
print(d)
e=True  #BOOLEAN VARIABLE
f= False #BOOLEAN VARIABLE
g = None #NONE TYPE VARIABLE 
# @sameer= 56 {INVALID  due to @ symbol }
# s@meer=67 {INVALID  due to @ symbol }
# A VARIABLE SHOULD ALWAYS START FROM A CHARACTER OR UNDERSCORE NOT ANY DIGIT OR SPECIAL CHARACTER 
print(e)
print(f)
print(g)
B= 10
B += 3 #INCREMENT the value of b by 3 and then assign it to b 
B *= 2
B -= 4
B /= 1
print(B)
# COMPARISON OPERATORS
h= 5<4
i= 5>=5
j= 8!=4
k= 5==5
print(h)
print(i)
print(j)
print(k)
# LOGICAL OPERATORS
e= True or False
# TRUTH TABLE OF "or" :-
print("True or False is" , True or False)  #TRUE
print("True or True is" , True or True)    #TRUE
print("False or True is" , False or True)  #TRUE
print("False or False is" , False or False) #FALSE
# TRUTH TABLE FOR "and" :-
print("True  and False is" , True and  False)  #False
print("True  and True is" , True  and True)    #TRUE
print("False and  True is" , False  and True)  #FALSE
print("False and  False is" , False  and False) #FALSE

#Not
print(not(False))  #it will show TRUE
print(not(True))   # it will show FALSE 

#type() FUNCTION AND TYPECASTING :-
# it will show the type of variable
y=34
t= type(y)
print(t)    #class "int" 
s= "31.2"  #in double cots everything is string
T= type(s)
print(T)    #class 'str'
# float() , str(), and int() also are functions which transforms a variable into their type but if its possible 
#  that means these func. uses REPL if evaluation is right then they print 
# ex: float("harry") it will show error as its not possible to turn strv into float
w= "31.2"
an= float(w)
tn= type(an)
print(tn)

# INPUT() FUNCTION:-
on = input("Enter number 1 : ")
off = input("enter number 2: ")
print("Number a is:  ",on)  #here  befor closing cot i pressed shift+alt+down arrow key [REPLICET]
print("Number b is:   ",off) # HERE, 1 and 2 sum= 12  because it supposes the values as strings not int 
# thats why it oprates those input int digits as str
print("sum is ", on + off) 
# if i want it aise 1+2 = 12 nah ho concanitate nah ho toh i will tell it to change my input into input
# on = int(input("Enter number 1 : "))
# off =int( input("enter number 2: "))
# COMPLETE 





 





