## Dice Rolling Game Documentation

This Python program simulates a dice rolling game where the user can choose how many times they want to roll the dice, and the program will display the results. The program includes input validation, logging, and displays welcome and goodbye messages with game statistics.

### Constants
- **DICE_SIDES**: A constant variable set to `6`, representing the number of sides on the dice.

### Functions

#### `welcome_message()`
Displays a welcome message to the player when the game starts.
- **Returns**: None
- **Side Effect**: Prints a message introducing the game to the user.

#### `goodbye_message(attempts, total_rolls)`
Displays a farewell message at the end of the game, showing the number of times the player attempted to roll the dice and the total number of rolls made.
- **Parameters**:
  - `attempts`: The total number of attempts (or rounds) the player made to roll the dice.
  - `total_rolls`: The total number of dice rolls made during the game.
- **Returns**: None
- **Side Effect**: Prints the farewell message with statistics.

#### `ask_user_input(prompt)`
Asks the user for input and ensures they enter a valid response. It accepts only `'y'` for yes and `'n'` for no.
- **Parameters**:
  - `prompt`: A string displayed to the user to ask for input.
- **Returns**: A string (`'y'` or `'n'`) representing the user's choice.
- **Side Effect**: Continuously prompts the user until valid input is provided.

#### `roll_dice()`
Rolls a six-sided dice a specified number of times and prints the results. It also handles input validation, ensuring the user enters a positive integer.
- **Returns**: The number of dice rolls made (an integer).
- **Side Effect**: 
  - Prints the results of each roll.
  - Logs each dice roll with the debug level in the `logging` module.
  - If the user provides invalid input, it asks for input again until valid input is provided.

#### `main()`
Controls the flow of the dice rolling game. It includes the main game loop, where the user is asked whether they want to roll the dice or not. The game continues until the user chooses to exit.
- **Returns**: None
- **Side Effect**: 
  - Calls `welcome_message()` to greet the user.
  - Repeatedly asks the user if they want to roll the dice using `ask_user_input()`.
  - If the user chooses to roll, it calls `roll_dice()` to perform the rolls.
  - If the user chooses to stop, it calls `goodbye_message()` to show game statistics and exits the loop.

### Logging

The program uses Python's built-in `logging` module to log dice rolls at the debug level. This allows developers to monitor the game's behavior during execution. The log entries are of the form:
```
DEBUG:root:Dice rolled: [roll result]
```

### Execution Flow

1. The program starts by calling the `main()` function.
2. `main()` calls `welcome_message()` to introduce the game.
3. The game enters a loop where the user is asked if they want to roll the dice.
4. If the user answers "y", the program asks how many times to roll the dice, calls `roll_dice()`, and updates the total roll count.
5. The game continues until the user answers "n", at which point `goodbye_message()` is called to display statistics, and the game ends.

### Example Usage

```
Welcome to the Dice Rolling Game!
You will be asked how many times you want to roll the dice each time.
Good luck!

Do you want to roll the dice (y/n): y
How many times do you wish to roll the dice: 3
Roll 1: Dice rolled: 4
Roll 2: Dice rolled: 2
Roll 3: Dice rolled: 6
You have rolled the dice 3 times.

Do you want to roll the dice (y/n): n

Thank you for playing!
You played 1 times and rolled the dice 3 times.
```
