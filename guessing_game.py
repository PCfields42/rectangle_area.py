import random

number_to_guess = random.randint(1, 10)  # Generates a random number between 1 and 10
guess = None

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 10: "))  # Convert input to integer

    if guess < number_to_guess:
        print("Too low, try again.")
    elif guess > number_to_guess:
        print("Too high, try again.")
    else:
        print("Congratulations! You guessed the right number.")

print("Game Over")
