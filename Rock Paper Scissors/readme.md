---
## **Documentation for Rock, Paper, Scissors Game**

### **Overview**
This is a command-line implementation of the classic **Rock, Paper, Scissors** game. The game can be played in two modes
1. **Player vs. Computer**
2. **Two Player Mode**

The game tracks the number of rounds played, wins, losses, ties, and streaks. The game can be restarted, and statistics are displayed at the end of each session.

### **Features**
- **Rock, Paper, Scissors Rules**: Players choose one of three options: Rock (`r`), Paper (`p`), or Scissors (`s`). The winner is determined by the classic rules:
  - Rock (`r`) beats Scissors (`s`)
  - Scissors (`s`) beat Paper (`p`)
  - Paper (`p`) beats Rock (`r`)
  
- **Emoji Representation**: Each option is displayed with corresponding emojis to make the game more visually appealing:
  - Rock → 🪨
  - Paper → 📄
  - Scissors → ✂️

- **Modes**:
  - **Player vs. Computer**: The player competes against the computer. The first player or computer to win the specified number of rounds is declared the overall winner.
  - **Two Player Mode**: Two players compete against each other. Each player chooses one of the three options, and the winner of the round is determined based on the same rules.

- **Statistics**:
  - The game tracks the number of rounds played, wins, losses, ties, and the longest win streak for the player.

- **Replay Option**: After each game, the player has the option to restart the game or exit.

---

### **Code Breakdown**

#### **Imports**

```python
import random as r
```
- **random** module is imported to allow the computer to randomly select a choice (Rock, Paper, or Scissors) during the Player vs. Computer mode.

---

#### **Variables & Constants**

```python
choices = {
    'r': '🪨',  # Rock
    'p': '📄',  # Paper
    's': '✂️'   # Scissors
}
```
- The `choices` dictionary maps the player's choice (`r`, `p`, or `s`) to its corresponding emoji for display.

#### **Functions**

1. **`results(choice)`**

   This function converts the player's choice into its respective word representation.
   - **Parameters**: `choice` (string) — the player's input (`r`, `p`, or `s`).
   - **Returns**: A string representing the choice (e.g., "Rock", "Paper", or "Scissors").

   ```python
   def results(choice):
       if choice == 'p':
           return 'Paper'
       elif choice == 'r':
           return 'Rock'
       elif choice == 's':
           return 'Scissors'
   ```

2. **`determine_winner(player_choice, comp_choice)`**

   This function determines the winner of a round based on the classic rules of Rock, Paper, Scissors.
   - **Parameters**: 
     - `player_choice` (string) — the player's selected choice (`r`, `p`, or `s`).
     - `comp_choice` (string) — the computer's selected choice (`r`, `p`, or `s`).
   - **Returns**: A string indicating the result of the round (`'win'`, `'lose'`, or `'tie'`).

   ```python
   def determine_winner(player_choice, comp_choice):
       if player_choice == comp_choice:
           return 'tie'
       elif (player_choice == 'p' and comp_choice == 'r') or \
               (player_choice == 'r' and comp_choice == 's') or \
               (player_choice == 's' and comp_choice == 'p'):
           return 'win'
       else:
           return 'lose'
   ```

3. **`get_valid_choice()`**

   This function ensures that the player enters a valid choice (either `r`, `p`, or `s`). If an invalid input is entered, the player is prompted to enter a valid choice again.
   - **Returns**: A string representing the valid choice (`r`, `p`, or `s`).

   ```python
   def get_valid_choice():
       while True:
           choice = input("Choose Rock (r), Paper (p), or Scissors (s): ").lower()
           if choice in choices:
               return choice
           print("Invalid choice. Please choose 'r', 'p', or 's'.")
   ```

---

#### **Main Game Logic**

1. **Game Mode Selection**

   The game first asks the player whether they want to play against the computer or in two-player mode.
   - If the player selects `1`, the game runs in **Player vs. Computer** mode.
   - If the player selects `2`, the game runs in **Two Player Mode**.

   ```python
   mode = input("Do you want to play against the computer (1) or another player (2)? Enter 1 or 2: ")
   ```

2. **Game Loop** 

   The game runs in a `while True` loop, allowing for replayability. The loop prompts the user for the number of rounds needed to win the game.

   ```python
   while True:
       rounds_to_win = int(input("How many rounds does a player need to win to be declared the overall winner? (1 or 2 recommended): "))
   ```

3. **Player vs. Computer Mode**

   - The player selects their choice and the computer randomly selects its choice. 
   - The winner is determined using the `determine_winner()` function. 
   - The game continues until one side wins the specified number of rounds.

   ```python
   if mode == '1':  # Player vs Computer
       while player_wins < rounds_to_win and computer_wins < rounds_to_win:
           # Game logic...
   ```

4. **Two Player Mode**

   - In this mode, both players take turns selecting their choices. The result is determined using the same rules as in Player vs. Computer mode.
   - Player 1’s wins are tracked using `player_wins`, and Player 2’s wins are tracked using `computer_wins` (despite being Player 2 in this mode).

   ```python
   elif mode == '2':  # Two Player Mode
       while player_wins < rounds_to_win and computer_wins < rounds_to_win:
           # Game logic...
   ```

5. **Final Statistics and Replay Option**

   After the game ends, the final statistics (total wins, losses, ties, rounds played, longest win streak) are displayed, and the user is prompted to play again or exit the game.

   ```python
   print("\nFinal Statistics:")
   print(f"Player Wins: {player_wins}")
   print(f"Computer Wins: {computer_wins}")
   print(f"Ties: {ties}")
   print(f"Total Rounds Played: {rounds}")
   print(f"Longest Win Streak: {win_streak}")
   
   play_again = input("\nDo you want to play again (yes or no)? ").lower()
   ```

---

### **Statistics and Achievements Tracked**

- **Player Wins**: The total number of rounds won by the player.
- **Computer Wins**: The total number of rounds won by the computer (or Player 2 in two-player mode).
- **Ties**: The total number of rounds that resulted in a tie.
- **Rounds Played**: The total number of rounds played during the current game session.
- **Longest Win Streak**: The longest consecutive number of rounds the player has won in a row.

### **Replay Option**
After a game session ends, the player is given the option to either:
- Play again, in which case the statistics are reset and a new game starts.
- Exit the game, which ends the program with a thank you message.

---

### **Potential Improvements**

- **Customizable Round Count**: Allow the user to specify how many rounds they want to play.
- **More Complex AI**: Implement an AI that tries to "learn" the player's patterns and adjusts its strategy.
- **Leaderboard**: Track player performance over multiple sessions and display a leaderboard.
- **Save/Load**: Save statistics between sessions and allow loading previous sessions.
- **More Advanced Achievements**: Track achievements like “winning X rounds in a row” or “winning X games in total.”

---

### **Conclusion**

This code implements the basic mechanics of **Rock, Paper, Scissors** with both single-player and two-player modes. It tracks important statistics, such as wins, losses, and ties, and provides a replay option after each game. The game is designed to be simple yet fun, and its structure allows for further enhancements, such as more advanced AI, multiplayer support, and statistics tracking.
