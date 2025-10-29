import random

# List of possible choices
choices = ["rock", "raper", "scissor"]

# Take user Input
user_choices = input("Enter your choice (rock, paper, scissors): ").lower()

# Computer choices
computer_choices = random.choice(choices)

print(f"\n You choose {user_choices}")
print(f"computer choose {user_choices}\n")

# Incase of match tie
if user_choices == computer_choices:
    print("match tie")

# Checking all probabilities of win and lose
elif user_choices == "rock":
    if computer_choices == "scissor":
        print("You win! Rock crushes scissors.")
    else:
        print("Computer win! Paper covers rock.")

elif user_choices == "paper":
    if computer_choices == "rock":
        print("You win! Paper covers rock.")
    else:
        print("Computer win! Scissors cut paper.")

elif user_choices == "scissor":
    if computer_choices == "paper":
        print("You win! Scissors cuts paper")
    else:
        print("Computer win! Rock crushes Scissors")

else: 
    print("Invalid input! Please choose rock, paper, or scissors.")