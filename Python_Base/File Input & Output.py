

# FILE I/O
# types of file :- 
# 1. TEXT files (.txt, .c, .py etc)
# 2. BINARY files (.jpg, .dat, etc)


# OPENING A FILE

f= open("file.txt","r")  #open the file in read mode 
data = f.read()
print(data)
f.close()   #whenever we are used any file at last you have to close it 




#  open() func gets two parameters 1. file name , 2. mode 

# MODES OF OPENING FILES:-
# r- reading 
# w - for writing 
# a - for appending 
# +  for updating 
# 'rb' open for read in binary mode 
# 'rt' open for read in text mode 

# WRITING DATA IN FILE FROM PYTHON 
st = "Hey muskan you are amazing "

f= open("myfile.txt", "w")  
# after execution of this you will see the text file named myfile.txt has been made

f.write(st)
f.close()


# /APPEND
st = "Hey muskan you are amazing "

f= open("myfile.txt", "w")  

f.append(st)


# WITH STATEMENTS 

f=open("file.txt")
print(f.read())

f.close()
# this same can be written using WITH STATEMENTS like this:-
with open("file.txt") as f:
    print(f.read())
# you dont have to explicitly close the file



