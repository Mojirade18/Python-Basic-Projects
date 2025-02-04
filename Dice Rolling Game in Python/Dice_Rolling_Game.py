import random as r
import logging

# Constants for better readability
DICE_SIDES = 6

# Setup logging for debugging
logging.basicConfig(level=logging.DEBUG)


def welcome_message():
    """
    Display a welcome message at the start of the game.
    """
    print("Welcome to the Dice Rolling Game!")
    print("You will be asked how many times you want to roll the dice each time.")
    print("Good luck!\n")


def goodbye_message(attempts, total_rolls):
    """
    Display a farewell message at the end of the game with stats.
    """
    print(f"\nThank you for playing!")
    print(f"You played {attempts} times and rolled the dice {total_rolls} times.")


def ask_user_input(prompt):
    """
    Ask the user for input with validation.
    Ensure they only enter 'y' or 'n'.
    """
    while True:
        ans = input(prompt).lower()
        if ans in ['y', 'n']:
            return ans
        else:
            print("Invalid input! Please enter 'y' for yes or 'n' for no.")


def roll_dice():
    """
    Rolls the dice a specified number of times and prints the result.
    Prompts the user to input the number of rolls and handles invalid inputs.
    Returns the number of dice rolls made.
    """
    while True:
        try:
            roll = input("How many times do you wish to roll the dice: ")
            roll = int(roll)  # Convert input to integer
            if roll <= 0:
                print("Please enter a positive number for rolls.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    rolls = []
    for i in range(roll):
        die_roll = r.randint(1, DICE_SIDES)
        rolls.append(die_roll)
        logging.debug(f"Dice rolled: {die_roll}")
        print(f"Roll {i + 1}: Dice rolled: {die_roll}")

    print(f"You have rolled the dice {len(rolls)} times.")
    return len(rolls)  # Return the number of rolls made


def main():
    """
    Main function to control the flow of the dice rolling game.
    """
    welcome_message()  # Display the welcome message

    attempts = 0
    total_rolls = 0

    while True:
        ans = ask_user_input("Do you want to roll the dice (y/n): ")

        if ans == "y":
            attempts += 1
            rolls_in_this_round = roll_dice()  # Capture the number of rolls made this round
            total_rolls += rolls_in_this_round  # Add it to the total number of rolls
        elif ans == "n":
            goodbye_message(attempts, total_rolls)  # Display farewell message
            break
        else:
            print("Invalid Input! Please enter 'y' for yes or 'n' for no.")


# Start the program
if __name__ == "__main__":
    main()
