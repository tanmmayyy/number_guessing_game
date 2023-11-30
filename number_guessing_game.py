import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I've selected a random number between 1 and 100. Your task is to guess it.")
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I've selected a random number between 1 and 100. Your task is to guess it.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    tries=0

    while True:
        # Get user input for their guess
        user_guess = int(input("Enter your guess: "))
        
        # Increment the attempts counter
        tries += 1

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You've guessed the correct number {secret_number} in {tries} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    number_guessing_game()

    secret_number = random.randint(1, 100)
    
    attempts = 0

    while True:
        # Get user input for their guess
        user_guess = int(input("Enter your guess: "))
        
        # Increment the attempts counter
        attempts += 1

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    number_guessing_game()
