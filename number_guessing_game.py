import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number.")

if __name__ == "__main__":
    number_guessing_game()