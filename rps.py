# here i  am implementing the rock, scissor and paper game 
import random

def get_user_choice():
    print("welcome to the rock, scissors and paper game")
    print("1.Rock")
    print("2.Scissors")
    print("3.Paper")
    choice = input("enter the number(1/2/3)")
    choices = {"1" : "Rock",
               "2" : "Scissor",
               "3": "Paper"
               }
    return choices.get(choice,None)


def get_computer_choice():
    return random.choice(["Rock","Scissor","Paper"])

user_choice = get_user_choice().strip().lower()
computer_choice = get_computer_choice().strip().lower()

while True:
    user_choice = get_user_choice().strip().lower()
    computer_choice = get_computer_choice().strip().lower()

    if user_choice==computer_choice:
        print("draw")
        play_request= input("do you want to play again(y/n)")
        if play_request =='y':
            continue
        break

    else:
        if (user_choice=="rock" and computer_choice=="paper") or (user_choice=="scissor" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="rock"):

            print("You win")
        else:
            print("you lose")  

        play_request= input("do you want to play again(y/n)")
        if play_request =='y':
            continue
        break



     

 



        