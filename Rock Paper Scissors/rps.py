import random

#List of Options
options = ["rock", "paper", "scissors"]

#User Choice
choice = input("Rock, Papers or Scissors: ").lower()

comp_choice = random.choice(options)

print(f"You chose {choice}")
print(f"Computer chose {comp_choice}")

if choice == comp_choice:
    print("Its a Tie!")
elif (choice == "rock" and comp_choice == "scissors") or (choice == "scissors" and comp_choice == "paper") or (choice == "paper" and comp_choice == "rock"):
    print("Congratulations! You Win!")
else:
    print("Computer Wins!")
