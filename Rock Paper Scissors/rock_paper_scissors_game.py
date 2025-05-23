import random as r

# Define choices with corresponding emojis
choices = {
    'r': '🪨',  # Rock
    'p': '📄',  # Paper
    's': '✂️'  # Scissors
}


# Function to display result based on the player choice
def results(choice):
    if choice == 'p':
        return 'Paper'
    elif choice == 'r':
        return 'Rock'
    elif choice == 's':
        return 'Scissors'


# Function to determine the winner of the round
def determine_winner(player_choice, comp_choice):
    if player_choice == comp_choice:
        return 'tie'
    elif (player_choice == 'p' and comp_choice == 'r') or \
            (player_choice == 'r' and comp_choice == 's') or \
            (player_choice == 's' and comp_choice == 'p'):
        return 'win'
    else:
        return 'lose'


# Initialize statistics
player_wins = 0
computer_wins = 0
ties = 0
win_streak = 0
total_rounds = 0
# Play against computer or another player
mode = input("Do you want to play against the computer (1) or another player (2)? Enter 1 or 2: ")

while True:
    # Get custom number of rounds to play
    rounds_to_win = int(
        input("How many rounds does a player need to win to be declared the overall winner? (1 or 2 recommended): "))

    # Start the game
    rounds = 0


    def get_valid_choice():
        while True:
            choice = input("Choose Rock (r), Paper (p), or Scissors (s): ").lower()
            if choice in choices:
                return choice
            print("Invalid choice. Please choose 'r', 'p', or 's'.")


    if mode == '1':  # Player vs Computer
        while player_wins < rounds_to_win and computer_wins < rounds_to_win:
            print(f"\nRound {rounds + 1}")
            player_choice = get_valid_choice()

            comp_choice = r.choice(['r', 'p', 's'])

            print(f"You chose: {results(player_choice)} {choices[player_choice]}")
            print(f"Computer chose: {results(comp_choice)} {choices[comp_choice]}")

            result = determine_winner(player_choice, comp_choice)

            if result == 'win':
                print("You win this round!")
                player_wins += 1
                win_streak += 1
            elif result == 'lose':
                print("You lose this round.")
                computer_wins += 1
                win_streak = 0
            else:
                print("It's a tie!")
                ties += 1

            rounds += 1

        if player_wins > computer_wins:
            print("\nYou are the overall winner!")
        else:
            print("\nComputer is the overall winner!")

    elif mode == '2':  # Two Player Mode
        while player_wins < rounds_to_win and computer_wins < rounds_to_win:
            print(f"\nRound {rounds + 1}")

            player1_choice = get_valid_choice()
            player2_choice = get_valid_choice()

            print(f"Player 1 chose: {results(player1_choice)} {choices[player1_choice]}")
            print(f"Player 2 chose: {results(player2_choice)} {choices[player2_choice]}")

            if player1_choice == player2_choice:
                print("It's a tie!")
                ties += 1
            elif (player1_choice == 'p' and player2_choice == 'r') or \
                    (player1_choice == 'r' and player2_choice == 's') or \
                    (player1_choice == 's' and player2_choice == 'p'):
                print("Player 1 wins this round!")
                player_wins += 1
                win_streak += 1
            else:
                print("Player 2 wins this round!")
                computer_wins += 1
                win_streak = 0

            rounds += 1

        if player_wins > computer_wins:
            print("\nPlayer 1 is the overall winner!")
        else:
            print("\nPlayer 2 is the overall winner!")

    # Final statistics and achievements
    print("\nFinal Statistics:")
    print(f"Player Wins: {player_wins}")
    print(f"Computer Wins: {computer_wins}")
    print(f"Ties: {ties}")
    print(f"Total Rounds Played: {rounds}")
    print(f"Longest Win Streak: {win_streak}")

    # Option to restart or exit
    play_again = input("\nDo you want to play again (yes or no)? ").lower()
    if play_again == "yes":
        # Reset statistics and start a new game
        player_wins = 0
        computer_wins = 0
        ties = 0
        win_streak = 0
        rounds = 0
        print("Starting a new game...\n")
    else:
        print("Thank you for playing! Goodbye!")
        break
