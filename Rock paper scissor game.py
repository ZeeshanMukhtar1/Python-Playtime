import random
item_list=["Rock", "Paper", "Scissor"]

user_choice = input("Your choice = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(user_choice, comp_choice)

if user_choice == comp_choice:
    print("Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock, Computer wins")
    else:
        print("Rock smashes Scissor, You won")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper, Computer wins")
    else:
        print("Paper covers Rock, You won")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes Scissor, Computer won")
    else:
        print("Scissor cuts Paper, You won")