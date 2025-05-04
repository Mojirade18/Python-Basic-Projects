import random as r
import time


def welcome():
    """Displays the welcome message and game instructions."""
    print("Welcome to the Number Guessing Game\n"
          "===================================\n"
          "In this game, the computer will randomly select a number within a range you provide.\n"
          "You will guess the number, and the program will tell you if your guess is too high or too low.\n"
          "You can specify the minimum and maximum values for the range.\n"
          "Additionally, you have a limited number of guesses. If you run out, the game will end.\n"
          "Let's get started!\n"
          "=============================================\n")


def get_difficulty():
    """Prompts the user to select a difficulty level for the game."""
    while True:
        difficulty = input("Choose a difficulty level: Easy, Medium, or Hard: ").strip().lower()
        if difficulty == 'easy':
            return 1, 100, 15  # Range: 1-100, attempts: 15
        elif difficulty == 'medium':
            return 1, 500, 10  # Range: 1-500, attempts: 10
        elif difficulty == 'hard':
            return 1, 1000, 7  # Range: 1-1000, attempts: 7
        else:
            print("Invalid choice. Please choose 'Easy', 'Medium', or 'Hard'.")


def get_range():
    """Prompts the user to input the range for the number and validates the input."""
    while True:
        try:
            min_val = int(input("Enter the minimum number of the range (1-1000): "))
            max_val = int(input("Enter the maximum number of the range (1-1000): "))
            if min_val < 1 or max_val > 1000 or min_val >= max_val:
                print(
                    "Please enter a valid range where the minimum is less than the maximum and both are between 1 and 1000.")
            else:
                return min_val, max_val
        except ValueError:
            print("Invalid input! Please enter valid integers.")


def get_number_to_guess(min_val, max_val):
    """Generates the random number within the user-defined range."""
    return r.randint(min_val, max_val)


def print_hint(guess, num_to_guess):
    """Provides a hint based on how close the guess is."""
    difference = abs(guess - num_to_guess)
    if difference == 0:
        return "Perfect! You got it."
    elif difference <= 5:
        return "You're VERY close!"
    elif difference <= 15:
        return "You're close!"
    elif difference <= 30:
        return "You're getting farther away, but not by much."
    else:
        return "You're far off!"


def play_game():
    """Handles the main gameplay loop."""
    difficulty_range = get_difficulty()
    min_val, max_val, max_attempts = difficulty_range

    num_to_guess = get_number_to_guess(min_val, max_val)

    print(f"\nI have selected a number between {min_val} and {max_val}.\nYou have {max_attempts} attempts to guess it.")

    attempts = 0
    start_time = time.time()

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess the number: "))
            if guess < min_val or guess > max_val:
                print(f"Please guess a number between {min_val} and {max_val}.")
                continue
            attempts += 1
            print(print_hint(guess, num_to_guess))

            if guess == num_to_guess:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return attempts
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print(f"Sorry, you have run out of attempts! The correct number was {num_to_guess}.")
    return attempts


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def get_random_hint(answer):
    hints = [
        f"The number is {'even' if answer % 2 == 0 else 'odd'}.",
        f"The number is {'a prime number' if is_prime(answer) else 'not a prime number'}.",
        f"The number is {'divisible by 3' if answer % 3 == 0 else 'not divisible by 3'}.",
        f"The number is {'divisible by 5' if answer % 5 == 0 else 'not divisible by 5'}.",
        f"The number is {'greater' if answer > 50 else 'less'} than 50.",
        f"The number is {'divisible by 7' if answer % 7 == 0 else 'not divisible by 7'}."
    ]
    return r.choice(hints)


def main():
    """Runs the entire game and tracks the best score."""
    best_score = float('inf')  # Initialize the best score as infinity (best is the lowest number of attempts)

    while True:
        welcome()
        attempts = play_game()

        # Track the best score (fewest attempts)
        if attempts < best_score:
            best_score = attempts

        print(f"\nYour best score so far is {best_score} attempts.")

        # Ask the player if they want to play again
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(f"Thanks for playing! Your best score was {best_score} attempts.")
            break


if __name__ == "__main__":
    main()
