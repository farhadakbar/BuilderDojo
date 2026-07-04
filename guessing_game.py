# Simple project that generates a random number between 1-100 and asks user to guess the number
import random

def generate_random_number():
    x = random.randint(1, 100)
    return x

def get_player_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            print("Error: Score must be between 1 and 100.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def give_guess_feedback(secret_number, guess):
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")

def main():
    print("Welcome to the Guessing Game! The random number is an integer between 1 and 100.")

    secret_number = generate_random_number()

    guess_counter = 0

    while True:
        guess = get_player_guess()

        guess_counter += 1

        give_guess_feedback(secret_number, guess)
        if guess == secret_number:
            break

    print("Congratulations! You guessed the number right!")
    if guess_counter == 1:
        print(f"You guessed it in {guess_counter} guess.")
    else:
        print(f"You guessed it in {guess_counter} guesses.")

main()