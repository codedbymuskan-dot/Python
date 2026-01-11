

# FUNCTIONS:- the part containing the exact set of instructions which are executed during the function call.

# FUNCTION DEFINATION :-
def avg():  #here, a function named "avg()" has been created using  'def'
    a=12    #everithing under this indentation is in the function "avg()"
    b=45
    c=56
    avg= (a+b+c)/3
    print(avg)

# FUNCTION CALL:-
avg()  



# TYPES OF FUNCTIONS IN PYTHON :-

# 1. Built in function (ALREADY PRESENT IN PYTHON ) ex.. len(), print(), range()
# 2. User Define functions (Defined by the user ) ex... greet(), avg()  we can create


# FUNCTIONS WITH ARGUMENTS:-

def greet(name, ending):  #here, as 'Muskan' variable name goes in function 
    print("Have a Good Day Dear" + name ) #string CONCATINATION
    print(ending)

greet(" Muskan", "Thank You")
greet(" Varun", "See uh")
greet(" Zee", "Thanks")
greet(" Ganeshu", "Thank You")
greet(" Komal", "Thank You")

# FUNCTION RETURN A VALUE AS SHOWN BELOW :-

def gr(name):  #here, as 'Muskan' variable name goes in function 
    print("Hhheeeelllooooowwwwww" + name ) #string CONCATINATION
    return "done"


a= gr(" Muskan")
print(a)  #this will show none untill we use return in the end of def func. 
# whatever  we return will be the output of 'a' when we print it "


gr(" Varun" )
gr(" Zee" )
gr(" Ganeshu")
gr(" Komal")


# DEFAULT PARAMETER VALUE:-

def g(name=  " stranger" , ending="See uhhh"):  
    print("Have a Good Day " + name ) #string CONCATINATION
    # print(f"Good day, {name}")   #ANOTHE WAY OF STRING CONCATINATION
    print(ending)
g()
g(" Varun", " okiieee")
g(" Zee")
g( )
g()  #this will give by default name "stranger"

# RECURSION:-   it is directly use a mathametical formula as function  
# function which CALLS ITSELF 
# For example :- factorial 
# factorial(n) = n * factorial (n-1)
# this factorial function can be defined as follows :-
def factorial(n):
    if (n == 0 or n == 1) :  #base condition which doesn't call the function 
        return 1
    else:
        return n* factorial(n-1)   #factorial calling itself 

i= int(input("enter a number"))
print(f"factorial of this number is :  {factorial(i)}")