import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
def determine_winner(user_choice, computer_choice):
    if user_choice == 0 and computer_choice == 2:
        return ("You win!")
    elif computer_choice == 0 and user_choice == 2:
        return ("You lose!")
    elif computer_choice > user_choice:
        return ("You lose!")
    elif user_choice > computer_choice:
        return ("You win!")
    else:
        return ("It's a draw")

def play_game():
    user_score = 0
    computer_score = 0
    play_again = True

    while play_again:

        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))





        while user_choice >= 3 or user_choice < 0:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

        computer_choice = random.randint(0, 2)
        print("you chose:")
        print(game_images[user_choice])

        print("Computer chose:")
        print(game_images[computer_choice])

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1


        print(f"\nScore - You: {user_score}  Computer: {computer_score}")

        print("\nDo you want to play again? (yes/no)")
        play_again_input = input("> ").lower()

        while play_again_input not in ['yes', 'no']:
            print("Invalid input. Please enter yes or no.")
            play_again_input = input("> ").lower()

        if play_again_input == 'no':
            play_again = False

    print("\nThanks for playing!")

play_game()
