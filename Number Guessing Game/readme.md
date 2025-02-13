---

# **Number Guessing Game Documentation**

This Python program is a **Number Guessing Game** where the computer randomly selects a number in a range that the player specifies. The player guesses the number, and the program provides hints if the guess is too high or too low. It also tracks the best score (fewest guesses) across multiple games.

## **Features**:
- Select difficulty levels: **Easy**, **Medium**, **Hard**.
- Provide dynamic hints based on proximity to the correct number.
- Allow the player to exit the game gracefully.
- Track and display the best score (fewest attempts).

## **Functions Documentation**

### 1. `welcome()`
**Purpose**: Displays a welcome message and game instructions.

```python
def welcome():
    """Displays the welcome message and game instructions."""
```

**Details**:
- Prints a welcome message and a brief explanation of the game.
- Informs the player that they can select a range for the game and that the game will give feedback on whether guesses are too high or too low.

---

### 2. `get_difficulty()`
**Purpose**: Prompts the user to select a difficulty level for the game.

```python
def get_difficulty():
    """Prompts the user to select a difficulty level for the game."""
```

**Details**:
- Prompts the player to select one of three difficulty levels: **Easy**, **Medium**, or **Hard**.
- Returns a tuple containing:
  - `min_val`: The minimum value of the guessing range.
  - `max_val`: The maximum value of the guessing range.
  - `max_attempts`: The number of attempts allowed for guessing the number.

**Possible Values**:
- **Easy**: 1-100 range with 15 attempts.
- **Medium**: 1-500 range with 10 attempts.
- **Hard**: 1-1000 range with 7 attempts.

---

### 3. `get_range()`
**Purpose**: Prompts the user to input a custom range (min and max values) and validates the input.

```python
def get_range():
    """Prompts the user to input the range for the number and validates the input."""
```

**Details**:
- Asks the player to enter the minimum and maximum values for the guessing range.
- Ensures the values are valid (i.e., the minimum is less than the maximum, and both are within the 1-1000 range).
- Returns the validated minimum and maximum values.

---

### 4. `get_number_to_guess(min_val, max_val)`
**Purpose**: Generates a random number for the player to guess within the specified range.

```python
def get_number_to_guess(min_val, max_val):
    """Generates the random number within the user-defined range."""
```

**Details**:
- Uses `random.randint(min_val, max_val)` to generate and return a random number between the minimum and maximum values.
- This number is the one the player will try to guess.

---

### 5. `print_hint(guess, num_to_guess)`
**Purpose**: Provides a hint about how close the guess is to the correct number.

```python
def print_hint(guess, num_to_guess):
    """Provides a hint based on how close the guess is."""
```

**Details**:
- Compares the player's guess with the number to guess.
- Provides hints based on how close the guess is:
  - `Perfect! You got it.` if the guess is exactly correct.
  - `You're VERY close!` if the guess is within 5 units.
  - `You're close!` if the guess is within 15 units.
  - `You're getting farther away, but not by much.` if the guess is within 30 units.
  - `You're far off!` if the guess is more than 30 units away.

---

### 6. `play_game()`
**Purpose**: Handles the main gameplay loop.

```python
def play_game():
    """Handles the main gameplay loop."""
```

**Details**:
- Calls `get_difficulty()` to get the difficulty level and parameters.
- Calls `get_range()` to get the custom range (if applicable).
- Generates a random number using `get_number_to_guess(min_val, max_val)`.
- Provides a loop for the player to make guesses, giving hints for each guess.
- Tracks the number of attempts and ends the game when the player either guesses the correct number or runs out of attempts.
- Displays the result (whether the player won or lost) and returns the number of attempts it took.

---

### 7. `main()`
**Purpose**: Orchestrates the entire game, tracks the best score, and allows the player to play multiple rounds.

```python
def main():
    """Runs the entire game and tracks the best score."""
```

**Details**:
- Initializes the best score as infinity (`best_score = float('inf')`) to track the fewest number of attempts across all rounds.
- Repeatedly calls `play_game()` to allow the player to play multiple rounds.
- Tracks the best score by comparing the attempts in each round with the current best score.
- Displays the best score at the end of each round.
- Asks the player if they want to play again after each round, and exits the game gracefully if the player answers "no".

---

## **Program Flow**

1. **Welcome Screen**: The `welcome()` function is called to explain the game to the player.
2. **Game Setup**:
   - The player chooses a difficulty level via the `get_difficulty()` function.
   - The range for guessing is either predefined based on difficulty or custom-defined by the player using `get_range()`.
   - The number to guess is randomly selected by `get_number_to_guess()`.
3. **Guessing Loop**:
   - The player makes guesses, and the program provides hints via `print_hint()`.
   - If the player guesses the number correctly, the game ends and the number of attempts is returned.
   - If the player runs out of attempts, the correct number is revealed.
4. **Best Score Tracking**: The program tracks the best score (fewest attempts) across multiple rounds.
5. **End Game**: After each round, the player is asked if they want to play again. If "no," the game ends, and the best score is displayed.

---

## **Example Run**

```
Welcome to the Number Guessing Game
===================================
In this game, the computer will randomly select a number within a range you provide.
You will guess the number, and the program will tell you if your guess is too high or too low.
You can specify the minimum and maximum values for the range.
Additionally, you have a limited number of guesses. If you run out, the game will end.
Let's get started!
=============================================

Choose a difficulty level: Easy, Medium, or Hard: Easy

I have selected a number between 1 and 100.
You have 15 attempts to guess it.

Attempt 1/15: Guess the number: 50
You're close!

Attempt 2/15: Guess the number: 70
You're getting farther away, but not by much.

Attempt 3/15: Guess the number: 60
You're VERY close!

Attempt 4/15: Guess the number: 58
Congratulations! You guessed the number in 4 attempts.

Your best score so far is 4 attempts.
Would you like to play again? (yes/no): no
Thanks for playing! Your best score was 4 attempts.
```

---

## **Conclusion**

This **Number Guessing Game** is a simple yet fun game that provides interactive feedback to the player. It has customizable difficulty levels, tracks the player's best score, and gives insightful hints. The program is designed to be extendable with features like time tracking, leaderboards, and more. 
