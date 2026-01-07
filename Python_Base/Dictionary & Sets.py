# DICTIONARY:- collection of Key value pairs
marks={
     "Harry" : 56,
     "Muskan" : 98,
     "Varun" : 78
}

print(marks, type(marks))
# in dict. INDEXING BY 0 ... DOESN'T WORK 
# Here, indexing happens using the key for ex:-
print(marks["Muskan"])
# dictionaries are MUTABLE 
# cannot contain duplicate keys(columns)
# it is 2-D
# here all the operation taken will not affect the actual data of the dictionary just like a list and 
# if uh have to change the actual data the performa task permanently which will we study soon


# DICT. FUNCTIONS:-
print(marks.items())  #return list of the data stored
print(marks.keys())   #returns keys of dict. :- Harry , Muskan, Varun
marks.update({"Sheela":45})  #here, sheela is new so we can update dict. and it will add this new data in it and if there any update in existing data then that update will also got taken
print(marks)
print(marks.get("Harry"))  #returns the values of specified key here, it will return harry's marks

'''
difference between  
print(marks.get("Harry")) 
       AND
print(marks["Muskan"])
both will give the values of those specified keys but 
.get will give you none if you enter wrong key
other side will give uh error in same case
'''

# SETS IN PYTHON :- collection of NON-REPETITIVE elements  (Mathematics based)
# dictionary and set both made with curly braces
# so to make empty dictionary we use :- D={} but 
# to make empty set we use:-
se = set()  #This is the only way to make an empty set
s={1,45,87,"Harry",45,5,8,9}   #set created with data 
# in set we can store multiple data type data
print(s,type(s))
# FUNCTIONS OF SET
s.add(345)
print(s)   
s.remove(4)
print(s)
s.pop()   #removes a random element and returns that whicch element got removed 
print(s)
s.clear()  #empties the set (clear all the data stored in set)

s1={145,78,6}
s2={7,8,1,78}
print(s1.union(s2))   #this union will  combine both set's data and show it but will not show repeated elements like 1 will come once at a time 

print(s1.intersection(s2))  #this will return the data which is in both sets like 1 and 78





