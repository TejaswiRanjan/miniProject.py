#Guess the number 

import random
target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit : ")

    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess !!")
        break

    elif(userChoice < target):
        print("Your number is too small. Take a bigger guess..")

    else:
        print("Your Number is too bigger. Take a smaller guess..")

print("____GAME OVER ____")