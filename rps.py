import random

#Note that this is the simplest possible version of a **working** python code for a rock paper scissors game that is written in 10 minutes. 
# I very well know that a ton of improvements and betterments can be made in this code.

while True:
    print("Hi! This is a very simple CLI based version of the rock paper scissors game written in python in 10 minutes! Enjoy!")
    print("Enter [1] to choose rock, Enter [2] to choose paper or Enter [3] to choose scissors.\nEnter [4] to quit.")
    usr_choice = int(input("Enter your choice: "))
    if(usr_choice != 4):
        comp_choice = random.randint(1,3)

        if(usr_choice == 1):
            print("You chose Rock")
        elif(usr_choice == 2):
            print("You chose Paper")
        elif(usr_choice == 3):
            print("You chose Scissors")

        if(comp_choice == 1):
            print("The computer chose Rock")
        elif(comp_choice == 2):
            print("The computer chose Paper")
        elif(comp_choice == 3):
            print("The computer chose Scissors")

        if(usr_choice == comp_choice):
            print("Game Draw.")

        if(usr_choice == 1 and comp_choice == 2):
            print("The computer wins!")
        elif(usr_choice == 1 and comp_choice == 3):
            print("You win!")
        elif(usr_choice == 2 and comp_choice == 1):
            print("You win!")
        elif(usr_choice == 2 and comp_choice == 3):
            print("The computer wins!")
        elif(usr_choice == 3 and comp_choice == 1):
            print("The computer wins!")
        elif(usr_choice == 3 and comp_choice == 2):
            print("You win!")
        print("\n ----------------")
    if(usr_choice == 4):
        print("You have quitted!")
        break

