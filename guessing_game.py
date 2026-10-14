# Simple project that generates a random number between 1-100 and asks user to guess the number
import random

def generate_random_number(max_number):
    x = random.randint(1, max_number)
    return x

def choose_difficulty():
    while True:
        difficulty = input("What difficulty would you like for the game (Easy, Medium, Hard): ").lower()
        if difficulty == "easy":
            max_number = 50
            max_guesses = 10
            return max_number, max_guesses
        elif difficulty == "medium":
            max_number = 100
            max_guesses = 7
            return max_number, max_guesses
        elif difficulty == "hard":
            max_number = 200
            max_guesses = 5
            return max_number, max_guesses
        else:
            print("Invalid difficulty. Please choose Easy, Medium, or Hard.")

def get_player_guess(max_number):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= max_number:
                return guess
            print(f"Error: Guess must be between 1 and {max_number}.")
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
    print("Welcome to the Guessing Game!")

    while True:

        max_number, max_guesses = choose_difficulty()
        print(f"The secret number is between 1 and {max_number}.")
        print(f"You have {max_guesses} guesses.")
        secret_number = generate_random_number(max_number)

        guess_counter = 0

        while guess_counter < max_guesses:
            guess = get_player_guess(max_number)

            guess_counter += 1

            give_guess_feedback(secret_number, guess)
            if guess == secret_number:
                break

        if guess == secret_number:
            print("Congratulations! You guessed the number right!")
            if guess_counter == 1:
                print(f"You guessed it in {guess_counter} guess.")
            else:
                print(f"You guessed it in {guess_counter} guesses.")
        else:
            print(f"Sorry you have run out of guesses. The secret number is {secret_number}.")

        while True:
            replay_selection = input("Would you like to play again? (yes/no):").lower()

            if replay_selection in ("yes", "no"):
                break
            else:
                print("Invalid selection. Please enter yes or no.")

        if replay_selection == "no":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()