import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number I'm thinking of within the range you specify.")
    
    lower = int(input("Enter the lower bound of the range: "))
    upper = int(input("Enter the upper bound of the range: "))
    
    if lower >= upper:
        print("Invalid range. The upper bound must be greater than the lower bound.")
        return
    
    secret_number = random.randint(lower, upper)
    attempts = 0
    
    while True:
        guess = input(f"Enter your guess ({lower} to {upper}): ")
        
        if not guess.isdigit():
            print("Please enter a valid integer.")
            continue
        
        guess = int(guess)
        
        if guess < lower or guess > upper:
            print(f"Your guess is out of bounds. Please guess between {lower} and {upper}.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
