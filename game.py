"""A number-guessing game."""

import random


def play_game():

    name = input("Hello, what is your name?: ")
    
    start_num = int(input("Please pick a starting number between 1 and 100."))
    end_num = int(input("Please pick an end number between your starting number and 100."))

    print(f"Hi {name}, I'm thinking of a number between {start_num} and {end_num}.")

    random_number = random.randint(start_num, end_num)
    guesses = 0
    best_score = 0
    max_guess = 7

    while max_guess >= guesses:
        
        guess = input(f"Please guess a number between {start_num} and {end_num}: ")


        # A bunch of ways to FAIL
        # then, execute the code that you want
        
        if not guess.isnumeric() or int(guess) not in range(start_num, end_num): # Short-circuit evaluation
            print(f"That is not a valid number, please guess a number between {start_num} and {end_num}.")
            continue # move to next time through the loop 
        
        guess = int(guess)

        if guess < random_number:
            print(f"Number guessed {guess} is too low.")
            guesses += 1
        elif guess > random_number:
            print(f"Number guessed {guess} is too high.")
            guesses += 1
        else:
            print(f"Congrats {name}!  You guessed {guess} which is correct and took you {guesses} number of guesses!")
            check_score(guesses, best_score)
            play_again()

    print("You have guessed too many times!")
    play_again()
        
        
        


def check_score(guesses, best_score):

    if guesses > best_score:
        print(f"The new best score is {guesses}!")
        best_score = guesses
    elif guesses < best_score:
        print(f"You did not beat your high score of {best_score}!")
    else:
        print(f"You tied your high score of {best_score}!")



def play_again():
    """Asks user if they would like play again

        Game will restart if player chooses Y    
    """

    choice = input("Would you like to play again? [Y] for Yes, [N] for No:").upper()

    if choice == "Y":
        play_game()
    elif choice == "N":
        print("Thanks for playing!")
        exit()
    else:
        print("Not a valid response, please choose [Y] or [N]")
        play_again()



play_game()


