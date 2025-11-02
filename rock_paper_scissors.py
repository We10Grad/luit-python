import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Enter rock, paper, or scissors:\n")

print("Computer choice:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors"):
    print("You win!")
elif (user_choice == "paper" and computer_choice == "rock"):
    print("You win!")
elif (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")

