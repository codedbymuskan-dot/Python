# LISTS AND TUPLES:-
L=["apple", "Muskan", "rohan",345.06,  False,7]  #container to store a set of values of any data type
L[4]='True'   #Lists are MUTABLE  means we can change data of list through indexing
print(L[4])

# A list can store any datatype 
# LIST IDEXING
L1=[7,9,"harry"]
print(L1[0]) #7
print(L1[1]) #9
# L1[] #error
print(L1[0:3]) #list slicing
# LIST FUNCTIONS 
# LIST METHODS OR FUNCTIONS AFFECTS THE ACTUAL DATA OF LIST 
L2=[1,8,7,2,21,15]
L2.sort()   #this will sort the actuall data of llist
print(L2)
L2.reverse()
print(L2)
L2.append(4) #this will ADD THE DATA the you write with append
print(L2)

L2.insert(3, 3333)   #inssert adds the data on a particular index
print(L2)

L2.pop(2)  #deletes the element of the written index '(2)'  and returns the whole list excluding deleted value
print(L2)   
L2.remove(21)    #will remove the written data '21' from the list
print(L2)

# TUPLES 
# IMMUTABLE DATA TYPE OPTION
# like a list but immutable  
a=() #empty tuple
# a=(1)  this will give error if you try to add only one element in tuple like that
a=(1,)    #this is the format of tuple if you want to add one element
b=(5,7,8,9,6,2,3)
print(type(b))
# TUPLE FUNCTIONS :-
print(b.count(2))   #counts the occurance of 2 in the tuple b
print(b.index(3))    #return the index of first occurance of 3







