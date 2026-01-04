
# STRINGS:-

s="Muskan" #strings are IMMUTABLE {we can't change any existing string if its created once}
# STRING SLICING:-
# here indexing starts from 0 and in reverse fromm -1 backwardly 
print(s[0:4])  #start from index 0 all the way till (3 excluding 3)
print(s[1])
print(s[-4:-1])  
print(s[:]) # it will print whole string 
print(s[1:]) 
print(s[:4]) 
# SKIP VALUE :-
word="amazing"
print(word[1:6:2]) 
# STRING FUNCTIONS:
# 1. len()
print(len(s)) #prints the length of that string stored i the variable "s"
# 2. .endswith()
str="hello world"
print(str.endswith("rld")) #it will answer in True or False 
print(str.startswith("woi")) #casesensitive func.
# 3. .count()
print(str.count("o")) #counts the total occurance of a letter in your string)
# 4. .capitalize()
print(str.capitalize()) #this will capitalizeof the initial letter of string
# 5. .find()
print(str.find("wor")) #find the word and returns the index of first occurance
# 6. .replace()
print(str.replace("world", "python") )  #it will replace the "world " from second word "python"
#ESCAPE SEQUENCE CHARACTERS :-
a="muskan is a good girl \n but not a bad girl" # takes after \n strs to the new line 
print(a)
b="harry is a good boy \n but not a bad \" boy\"" #here \"abc..\" the '\"'specifes double cotys in printing
print(b)
# \t is used for tab
# \\ is used to use literal backslash
# \; is used in case of single cots


