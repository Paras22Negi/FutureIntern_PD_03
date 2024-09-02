import random

def run_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def run_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose again.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"
def game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = run_user_choice()
    computer_choice = run_computer_choice()
    print("You chose: "+ user_choice)
    print("The computer chose: "+ computer_choice)
    result = get_winner(user_choice, computer_choice)
    print(result)
game()
x=input("do you want to play again?[Y/N]:").lower()
while x == "y":
    game()
    x = input("do you want to play again?[Y/N]:").lower()
print("Thankyou! for playing")