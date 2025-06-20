#rock, paper, scissors

import random #me import vazoume vivliothikes
print("We are playing the game of Rock, Paper and Scissors. Select")
choice = input("What you're selecting: ")

ai_choices = ["Rock", "Paper", "Scissors"] #lista pou mporei na periexei polles metavlites
ai= random.choice(ai_choices)
print("My decision is",ai,)

if choice=="Scissors" and ai =="Scissors" :
    print("This is a tie.")
elif choice=="Rock" and ai=="Rock":
    print("Try again, tie.")
elif choice=="Paper" and ai=="Paper":
    print("This is a tie.")
elif choice=="Rock" and ai=="Paper":
    print("Ez W (bot wins)")
elif choice=="Rock" and ai=="Scissors":
    print("You win!1!!")
elif choice=="Paper" and ai=="Rock":
    print("You win!1!!")
elif choice=="Paper" and ai=="Scissors":
    print("Try again, you lost.")
elif choice=="Scissors" and ai=="Rock":
    print("You are bad in this game. LOL")
elif choice=="Scissors" and ai=="Paper":
    print("Good job!")
else:
    print("Please choose a valid option (Rock-Paper-Scissors).")
