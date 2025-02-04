## Dice Rolling Game - Program Documentation
Overview
This is a simple command-line game where the user can roll a dice a specified number of times. The program asks the user whether they want to roll the dice, how many times they wish to roll it, and keeps track of the number of rolls. It then shows the results of each roll and provides a summary at the end. The program uses logging for debugging and maintaining a record of each dice roll.
________________________________________
Functions
1. welcome_message()
Description: Displays a welcome message to the user at the start of the game.
Parameters: None
Returns: None
Example Output:
Welcome to the Dice Rolling Game!
You will be asked how many times you want to roll the dice each time.
Good luck!
________________________________________
2. goodbye_message(attempts, total_rolls)
Description: Displays a farewell message when the user exits the game. It includes the total number of times the user played and the total number of dice rolls.
Parameters:
•	attempts: (int) The number of times the user played (pressed 'y' to roll the dice).
•	total_rolls: (int) The total number of dice rolls made by the user.
Returns: None
Example Output:
Thank you for playing!
You played 3 times and rolled the dice 8 times.
________________________________________
3. ask_user_input(prompt)
Description: Prompts the user for input (either 'y' or 'n') with input validation. If the user enters anything other than 'y' or 'n', it asks again.
Parameters:
•	prompt: (str) The message to be displayed to the user.
Returns:
•	(str) The user's response: either 'y' or 'n'.
Example Usage:
ans = ask_user_input("Do you want to roll the dice (y/n): ")
________________________________________
4. roll_dice()
Description: Prompts the user to input the number of times they want to roll the dice, rolls the dice that many times, and displays the result for each roll. It returns the number of rolls made.
Parameters: None
Returns:
•	(int) The number of rolls made.
Example Output:
How many times do you wish to roll the dice: 3
Roll 1: Dice rolled: 4
Roll 2: Dice rolled: 2
Roll 3: Dice rolled: 6
You have rolled the dice 3 times.
________________________________________
5. main()
Description: The main function that controls the flow of the game. It repeatedly asks the user if they want to play, calls the appropriate functions for rolling the dice, and tracks the total number of games played and dice rolls. When the user chooses to quit, it calls goodbye_message() and exits the game.
Parameters: None
Returns: None
Flow:
1.	Welcomes the user and prompts them to play the game.
2.	Calls ask_user_input() to decide if the user wants to roll the dice.
3.	If the user chooses to roll the dice: 
o	Calls roll_dice() to perform the rolls and display results.
o	Tracks the total number of rolls and games played.
4.	If the user chooses to quit, displays a summary message with the total number of games and rolls.
Example Output:
Do you want to roll the dice (y/n): y
How many times do you wish to roll the dice: 2
Roll 1: Dice rolled: 5
Roll 2: Dice rolled: 3
You have rolled the dice 2 times.

Do you want to roll the dice (y/n): n
Thank you for playing!
You played 1 times and rolled the dice 2 times.
________________________________________
Logging
The program uses the logging module to keep a record of dice rolls for debugging purposes. This provides an easy way to track what's happening in the program without cluttering the user interface.
Logging Setup:
logging.basicConfig(level=logging.DEBUG)
This setup ensures that all log messages at the DEBUG level and above (like INFO, WARNING, ERROR, and CRITICAL) are displayed in the terminal.
Logging Usage:
Whenever a dice is rolled, the program logs the value rolled using the logging.debug() function. This helps track what happened behind the scenes:
logging.debug(f"Dice rolled: {die_roll}")
This message is saved in the log, but it doesn't appear in the program's main output unless the logging level is set to DEBUG or lower.
Example Log Output:
DEBUG:root:Dice rolled: 3
DEBUG:root:Dice rolled: 6
DEBUG:root:Dice rolled: 1
________________________________________
Constants
DICE_SIDES:
DICE_SIDES = 6
This constant represents the number of sides on the dice (6-sided). Using a constant makes it easy to modify the dice's behavior if you decide to change the number of sides in the future.
________________________________________
Error Handling
The program includes error handling to manage invalid input. For instance:
•	When asking for the number of rolls, the program uses a try-except block to catch invalid inputs (non-numeric inputs).
•	If the user enters an invalid number of rolls (e.g., zero or a negative number), the program will ask them to enter a valid positive number.
________________________________________
Flow of Execution
1.	Starting the Game:
o	The main() function starts by calling welcome_message().
o	It then enters a loop where the program asks the user if they want to play.
2.	Rolling the Dice:
o	If the user chooses to roll the dice (answers 'y'): 
	The roll_dice() function is called, and the user is asked how many times they want to roll the dice.
	The dice is rolled the specified number of times, and the results are printed.
	The total number of rolls for that session is tracked and added to the cumulative total.
3.	Ending the Game:
o	If the user chooses not to roll the dice (answers 'n'): 
	The goodbye_message() function is called, which displays a summary of the total number of games played and dice rolls made.
4.	Repetition:
o	If the user gives an invalid input (neither 'y' nor 'n'), the program will prompt them again until a valid response is given.
________________________________________
Possible Improvements
1.	Saving Logs to a File: Instead of printing logs to the console, they could be saved to a file for easier tracking.
2.	More Features: You could add features like betting, multiple dice, or advanced game modes.
3.	User Interface: For a more engaging experience, the game could be made with a graphical user interface (GUI) using a module like tkinter.
________________________________________
Conclusion
This program demonstrates several important concepts in Python:
•	User Input Validation.
•	Error Handling with try-except.
•	Logging for debugging and tracking events.
•	Game Flow Control using loops and functions.
By following these best practices, the code is more organized, maintainable, and user-friendly.


