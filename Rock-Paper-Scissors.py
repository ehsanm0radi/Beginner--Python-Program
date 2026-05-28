import random

#==================================

User_choices = ("rock", "paper", "scissor")

def get_user_input():
    choice = input("pick your choice [\"rock\",\"paper\",\"scissor\"]: ")
    while choice not in User_choices:
        choice = input("pick your choice [\"rock\",\"paper\",\"scissor\"]: ")
    return choice

def get_pc_input():
    pc_choice = random.choice(User_choices)
    print(f"Computer choice was: {pc_choice}")
    return pc_choice

#===========================================

def determine_winner(user_input, pc_input):
    if user_input == pc_input:
        print("Your choice is the same as the computer's choice. ")
        return "DRAW!"
    elif (user_input == "rock" and pc_input == "scissor") \
            or (user_input == "scissor" and pc_input == "paper") \
            or (user_input == "paper" and pc_input == "rock"):
        print("You won")
    else:
        print("Computer won")

def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input, pc_input)
    print("End of Game")

keys = ("y" , "n")
answer = 'y'
while answer == "y":
    main()
    answer = input("Do you want to continue? (y/n):")
    while answer not in keys:
        answer = input("Do you want to continue? (y/n):")
    if answer == "n":
        print("Thanks for playing.")