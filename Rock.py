import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a draw!"
    elif (
        (player_choice == "1" and computer_choice == "3") or
        (player_choice == "2" and computer_choice == "1") or
        (player_choice == "3" and computer_choice == "2")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = {"1": "rock", "2": "paper", "3": "scissors"}

    while True:
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        player_choice = input("Enter your choice (1-4): ")

        if player_choice == "4":
            print("Thanks for playing!")
            break

        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = str(random.randint(1, 3))
        print(f"You chose {choices[player_choice]}.")
        print(f"The computer chose {choices[computer_choice]}.")
        print(determine_winner(player_choice, computer_choice))
        print()

play_game()


 