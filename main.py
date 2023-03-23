import random
import os
from art import logo

def play_game():
    print(logo)
    print("Welcome To The Number Guessing Game!")
    print("I'm Thinking Of Number Between 1 to 100")

    numbers_range = range(1, 101)

    chosen_number = random.choice(numbers_range)
    chosen_number = int(chosen_number)
    number_length = len(str(chosen_number))
    print(f"pssst the correct answer is {chosen_number}")

    is_game_end = False

    chances = 10
    difficulty = input("Choose difficulty type 'hard or 'easy': ")
        
    if difficulty == "hard":
        chances = 5
        print(f"You have {chances} attempts remaining to guess a number.")
       
    elif difficulty == "easy":
        chances = 10
        print(f"You have {chances} attempts remaining to guess a number.")
      
    while not is_game_end:      
        guess = input("Make a guess: ")
        guess = int(guess)    
            
        if guess == chosen_number:
            print(f"Your guess is correct. The answer is {chosen_number}. ")
            break    
        
        if guess > chosen_number:
            print("Too high.")
            chances -= 1
            print(f"You have {chances} attempts remaining to guess a number.")
            print("Guess again.")
    
        if guess < chosen_number:
            print("Too low.")
            chances -= 1
            print(f"You have {chances} attempts remaining to guess a number.")
            print("Guess again.")
            
        if chances == 0:
            print("You've run out of guesses. You lose.")
            is_game_end = True
            
    play_again = input("Do you want to play again? Type 'yes' or 'no': ")
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")
        is_game_end = True
        
play_game()
