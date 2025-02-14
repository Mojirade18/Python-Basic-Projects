from colorama.ansi import clear_screen


# Create user
def prompt():
    user_name = input("Enter your user name: ")
    password = input("Enter your password: ")
    return user_name, password


# Create dictionary (allows multiple users)
def users(users_dict, user_name, password):
    if user_name not in users_dict:
        users_dict[user_name] = password
        print("User Created Successfully!\n")
    else:
        print("Username already exists! Please choose another one.\n")
    return users_dict


# Login functionality with multiple attempts
def login(users_dict):
    attempts = 3  # Allow a maximum of 3 attempts for login
    while attempts > 0:
        login_user_name, login_password = prompt()  # Get login credentials from prompt

        # Login check
        if login_user_name in users_dict:  # Check if the username exists
            if login_password == users_dict[login_user_name]:  # Check if the password matches
                print(f"\nWelcome, {login_user_name}! You have successfully logged in!!\n")
                return True
            else:
                print("\nInvalid Password. Please Try Again.\n")
                attempts -= 1
        else:
            print("\nInvalid Username. Please Try Again.\n")
            attempts -= 1

        # Notify the user about remaining attempts
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.\n")
        else:
            print("\nYou have been locked out. Exiting the program...\n")
            return False
    return False


# Main function
def main():
    users_dict = {}  # Initialize empty dictionary for multiple users

    while True:
        clear_screen()  # Clear the screen for better user experience

        # Prompt for user registration
        print("=== User Registration ===\n")
        user_name, password = prompt()  # Get username and password from prompt
        users_dict = users(users_dict, user_name, password)

        print("\nPlease proceed to log in.\n")

        # Ask if the user wants to log in
        decide = input("Do you wish to proceed to login (yes or no) : ").lower()
        if decide == 'yes':
            # Attempt login
            if login(users_dict):
                break  # Exit the loop on successful login
        elif decide == 'no':
            print("Thank you very much.\nGood Bye\n")
            break  # Exit the program if the user doesn't want to log in
        else:
            print("Invalid input! Please type 'yes' or 'no'.\n")


# Start point
if __name__ == "__main__":
    main()
