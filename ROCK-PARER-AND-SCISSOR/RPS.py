import random


computer_choice = random.choice(["scissors", "rock", "paper"])

user_choice = input("Do you want - rock, paper, scissors ? \n")
if computer_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "scissors":
    print(" YOU WIN THE GAME :), THe computer chose " + computer_choice)
elif user_choice == "paper" and computer_choice == "rock":
     print(" YOU WIN THE GAME :), THe computer chose " + computer_choice)
elif user_choice == "scissors" and computer_choice == "paper":
     print(" YOU WIN THE GAME :), THe computer chose " + computer_choice)
elif user_choice == "rock" and computer_choice == "paper":
    print(" YOU LOSE :( , THe computer chose " + computer_choice)
elif user_choice == "paper" and computer_choice == "scissors":
      print(" YOU LOSE :( , THe computer chose " + computer_choice)
elif user_choice == "scissors" and computer_choice == "rock":
      print(" YOU LOSE :( , THe computer chose " + computer_choice)