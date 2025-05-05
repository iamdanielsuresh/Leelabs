#!/usr/bin/env python3
import random

def play_game():
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    max_attempts = 10
    
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}!")
                continue
                
            if guess < secret_number:
                print(f"Too low! Attempts left: {max_attempts - attempts}")
            elif guess > secret_number:
                print(f"Too high! Attempts left: {max_attempts - attempts}")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return True
                
        except ValueError:
            print("Please enter a valid number!")
            
    print(f"Game over! The number was {secret_number}.")
    return False

def main():
    print("Number Guessing Game")
    print("-------------------")
    
    play_again = True
    wins = 0
    games = 0
    
    while play_again:
        games += 1
        if play_game():
            wins += 1
            
        choice = input("Play again? (y/n): ").lower()
        play_again = choice == 'y'
    
    print(f"\nYou played {games} games and won {wins} times.")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()