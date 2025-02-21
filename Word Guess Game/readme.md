# Word Guessing Game Documentation

## Overview
This is a word guessing game where the player needs to guess the letters of a randomly selected fruit name. The player has a limited number of chances to guess correctly. With each guess, the game updates the word by revealing correct letters. The game ends when the player guesses the word correctly or runs out of chances.

### Features
- **Random Fruit Selection:** A random fruit is selected from a predefined list of fruits.
- **Letter Guessing:** The player guesses one letter at a time.
- **Chances:** The player is given a set number of chances based on the length of the fruit name.
- **Input Validation:** Ensures the player inputs a single valid letter and checks for repeated guesses.
- **Tracking Guesses:** Keeps track of all guessed letters and prevents the player from repeating guesses.

---

## Functions

### 1. `update_word(l_guess, empty_word, w_chosen)`
This function updates the word with the guessed letter if the letter is present in the chosen fruit name.

#### Parameters:
- `l_guess` (str): The letter guessed by the player.
- `empty_word` (str): The current state of the word (with underscores for unguessed letters).
- `w_chosen` (str): The randomly selected fruit name.

#### Returns:
- (str): The updated word with correctly guessed letters.

#### Example:
```python
update_word('a', '_a__a', 'mango')
# Returns '_a_a_'
```

---

### 2. Main Game Loop
The game logic is run inside a `while` loop, where the player is repeatedly prompted to guess a letter. The loop continues until the player either:
- **Wins:** Guesses the complete word correctly.
- **Loses:** Runs out of chances.

#### Steps:
1. **Guess Input:** The player is prompted to input a letter to guess.
2. **Validation:** The game checks that the input is a single letter and that it has not been guessed before.
3. **Update Word:** If the guessed letter is correct, the word is updated.
4. **Chances Decrease:** If the guess is incorrect, the number of remaining chances decreases.
5. **Win Condition:** If the word is completely guessed, the game congratulates the player and ends.
6. **End Condition:** If the player runs out of chances, the game reveals the word and ends.

---

## Game Flow

### 1. **Initialization:**
- The game begins by selecting a random fruit from the `fruits` list.
- An empty word is displayed with underscores corresponding to the length of the chosen fruit name.
- The player is given a number of chances equal to the length of the fruit plus 2.

### 2. **Player Guesses:**
- The player is prompted to guess a letter, and the input is validated:
  - The guess must be a single letter.
  - The guess must not have been made previously.
- If the guess is correct, the word is updated to reveal the guessed letter(s).
- If the guess is incorrect, the number of remaining chances decreases.

### 3. **Game Progress:**
- The player’s guesses are tracked, and they are shown so that repeated guesses can be avoided.
- If the player guesses the word correctly, they win the game, and a congratulatory message is displayed.
- If the player runs out of chances, the game ends, and the correct word is revealed.

---

## Example Gameplay

```
You have 8 chances to guess the word.
Guess a letter of a fruit with 5 letters: _ _ _ _ _: 
Your previous guesses: []:

Guess a letter of a fruit with 5 letters: _ _ _ _ _: (Chances left: 7)
Your previous guesses: ['a']: 
Incorrect guess. You have 6 chances left.

Guess a letter of a fruit with 5 letters: _ _ a _ _: (Chances left: 6)
Your previous guesses: ['a']: 
Updated word: _ a _ _ _

...

Congratulations! You've guessed the word: apple
```

---

## Enhancements and Extensions

1. **Multiple Letter Guessing:**
   - Allow players to guess multiple letters at once (e.g., "a", "b", "c").
   
2. **Hints:**
   - Provide the player with the option to reveal a random letter that has not yet been guessed.
   
3. **Difficulty Levels:**
   - Implement different difficulty levels (e.g., fewer chances for harder words, larger word pool for advanced levels).

4. **Replayability:**
   - Add the option for the player to play multiple rounds without restarting the program.
   
5. **GUI Interface:**
   - Consider building a graphical user interface (GUI) for a more interactive experience, if working with frameworks like Tkinter or Pygame.

---

## Conclusion

This game provides an engaging way to guess words by interacting with letters and receiving feedback on correct and incorrect guesses. It also teaches basic input validation, word manipulation, and game logic. You can expand on this game with additional features to further enhance gameplay.
