import random

def guess_number():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        # Increment the number of attempts
        attempts += 1

        # Take the user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        # Check if the guess is correct
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

# Start the game
if __name__ == "__main__":
    guess_number()
