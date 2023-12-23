import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose."

def play_again():
    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again not in ['yes', 'no']:
        play_again = input("Invalid choice. Do you want to play again? (yes/no): ").lower()
    return play_again == 'yes'

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}, the computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

    if not play_again():
        break