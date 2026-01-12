


# PROJECT-1 : SNAKE, WATER & GUN GAME
import random 
'''
1 for snake 
-1 for water 
0 for gun
'''
computer = random.choice([-1,0,1])
yourstr=input("Enter your choice: ")
youDict={"s": 1, "w": -1, "g": 0}
revdict= {1:"Snake", -1: "Water", 0: "Gun"}

you= youDict[yourstr]

# by now we have 2 numbers (variables), you and computer
print(f"You Selected {revdict[you]}\n Computer selected {revdict[computer]}")

if(computer==you):
    print("Its a Draw")

else:
    if(computer== -1 and you==1):
        print("You Win!\nYAYYYYYYYYYY!!!")
    
    elif(computer== -1 and you==0):
        print("You Lose!")
    elif(computer== 1 and you==-1):
        print("You Lose!")
    elif(computer== 1 and you==0):
        print("You Win!\nYAYYYYYYYYYY!!!")
    elif(computer== 0 and you==-1):
        print("You Win!\nYAYYYYYYYYYY!!!")
    elif(computer== 0 and you==1):
        print("You Lose!")
    else :
        print("Something Went Wrong!")

