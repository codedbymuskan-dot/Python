

# LOOPS
# TWO TYPES IN PYTHON
# WHILE LOOP:-

i=1
while(i<6):
    print(i)
    i+=1

l=["harry", "Muskan", "Zee", "Varun", "Ganesh"]
i=0         #initialisation
while(i<len(l)):  #condition portion
    print(l[i])   #statement to be executed 
    i +=1          #increment[+=]/ decrement[-=]


# FOR LOOP:-

# range function  generates no. from 0 to n-1
for i in range(4):
    print(i)

# ITERATION USING 'FOR LOOP' AS IT IS USED TO ITERATE
ls=[1,45,78,98,54,65]
for i in ls:
    print(i)
    print(i+10)

tupp=(6,789,87,76)
for i in tupp:
    print(i)

str="Muskan"
for i in str:
    print(i)

# FOR LOOP WITH ELSE  #IMP....
# we can use an optional else with for loop in python 
# this concept is usually asked in interviews but in work it  doesn't get that much used 
lst=[12,54,78]
for i in lst:
    print(i)
else:
    print("DONE")  #this is printed when the loop exhausts!

# THE BREAK STATEMENT:-
for i in range(0,70):
    print(i)
    if(i==5):
        break   # means :- exit the loop right now

# CONTIBUE STATEMENT:-
# skip this iteration (i value)
# it stops next lines to get execute and continues lines before the continue command
for i in range(4):
    print("printing")
    if(i==2):
        continue
    print(i)



# PASS STATEMENT:-
# null statement in python
# it instructs "DO NOTHING"
for i in range(645):
    pass   #it will skip whole statement 

while(i<45):
    print(i)
    i += 1

