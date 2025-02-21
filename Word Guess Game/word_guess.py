import random as r

fruits = ['mango', 'apple', 'lemon', 'peach', 'orange', 'banana', 'strawberry', 'grape', 'watermelon',
          'pineapple', 'kiwi', 'pear', 'cherry', 'plum', 'blueberry', 'blackberry', 'raspberry', 'apricot',
          'papaya', 'pomegranate', 'fig', 'nectarine', 'melon', 'tangerine', 'lime', 'coconut', 'cantaloupe',
          'dragon fruit', 'guava', 'lychee', 'persimmon', 'passion fruit', 'jackfruit', 'date', 'jackfruit',
          'soursop', 'starfruit', 'elderberry', 'boysenberry', 'quince', 'mulberry', 'currant', 'lingonberry',
          'honeydew', 'clementine', 'mandarin', 'kumquat', 'longan', 'salak', 'yunnan hackberry', 'baobab',
          'rhubarb', 'sapodilla']

# Random word selected from the list
w_chosen = r.choice(fruits)

# Get length of the word
w_len = len(w_chosen)

# Empty word to hold the result (initialized with underscores)
empty_word = '_' * w_len

# Calculate the number of chances
chances = w_len + 2
guessed_letters = []

print(f"You have {chances} chances to guess the word.")

def update_word(l_guess, empty_word, w_chosen):
    # Convert the empty word to a list for easy modification
    empty_word_list = list(empty_word)

    # Loop through the chosen word to find all occurrences of the guessed letter
    for i in range(len(w_chosen)):
        if w_chosen[i] == l_guess:
            empty_word_list[i] = l_guess  # Replace the underscore with the guessed letter

    # Convert the list back to a string
    return ''.join(empty_word_list)

# Main game loop
while chances > 0:
    # Get user input for a letter
    l_guess = input(f"Guess a letter of a fruit with {w_len} letters: {empty_word} (Chances left: {chances})\nYour previous guesses: {guessed_letters}: ").lower()

    # Validate input (check if it's a single letter and not previously guessed)
    if len(l_guess) != 1 or not l_guess.isalpha():
        print("Please enter a valid single letter.")
        continue
    if l_guess in guessed_letters:
        print(f"You've already guessed the letter '{l_guess}'. Try again.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(l_guess)
    chances -= 1

    # If chances are over
    if chances == 0:
        print("\nYou've run out of chances! The word was:", w_chosen)
        break
    else:
        if l_guess in w_chosen:
            # Update the empty word with the guessed letter
            empty_word = update_word(l_guess, empty_word, w_chosen)
            print("Updated word:", empty_word)

            # Check if the word is fully guessed
            if '_' not in empty_word:
                print("Congratulations! You've guessed the word:", w_chosen)
                break
        else:
            # Decrease the number of chances if the guess is incorrect
            print(f"Incorrect guess. You have {chances} chances left.")
