---
# User Registration and Login Program Documentation

### Overview
This program simulates a simple user registration and login system entirely within the console. It allows users to
- Register with a unique username and password.
- Log in with the credentials they provided.
- Retry login a limited number of times (3 attempts) before being locked out.
- Exit the program at any point.

The program does **not** use any external file handling and operates solely in the console. All user data is stored temporarily in a dictionary during the session.

---

## Program Features
1. **User Registration**: 
   - Users are prompted to enter a username and a password to create an account.
   - If the username already exists, they are informed and prompted to choose another one.
   
2. **User Login**: 
   - After registering, the user can attempt to log in using the username and password they provided.
   - The system checks if the username exists and then verifies if the password matches.
   - If the user enters the wrong password, they are allowed 3 attempts to try again.
   
3. **Clear Screen**:
   - The console is cleared between actions (registration, login attempts) for a cleaner user experience.
   
4. **Exit Option**:
   - At any point, the user can choose to exit the program gracefully.

---

## Program Structure

### 1. **`prompt()`**
   - **Description**: This function prompts the user to input their username and password.
   - **Inputs**: None (user interaction through input).
   - **Outputs**: Returns a tuple of `user_name` and `password` entered by the user.
   
   ```python
   def prompt():
       user_name = input("Enter your user name: ")
       password = input("Enter your password: ")
       return user_name, password
   ```

### 2. **`users(users_dict, user_name, password)`**
   - **Description**: This function handles user registration by adding a new username and password pair to the `users_dict`. If the username already exists, it notifies the user.
   - **Inputs**:
     - `users_dict`: The dictionary storing all registered users.
     - `user_name`: The username entered by the user.
     - `password`: The password entered by the user.
   - **Outputs**: Returns the updated `users_dict`.
   
   ```python
   def users(users_dict, user_name, password):
       if user_name not in users_dict:
           users_dict[user_name] = password
           print("User Created Successfully!\n")
       else:
           print("Username already exists! Please choose another one.\n")
       return users_dict
   ```

### 3. **`login(users_dict)`**
   - **Description**: This function handles the login process. It allows the user up to 3 attempts to log in by checking if the username and password match the stored credentials.
   - **Inputs**:
     - `users_dict`: The dictionary containing registered users and their passwords.
   - **Outputs**:
     - `True` if the login is successful.
     - `False` if the login fails after 3 attempts.
     
   ```python
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
   ```

### 4. **`main()`**
   - **Description**: This is the main function that drives the entire program. It:
     - Initializes the dictionary for storing user credentials.
     - Guides the user through registration and login.
     - Allows multiple user registrations and logins.
     - Offers an option to exit the program.
   - **Inputs**: None (except user interaction).
   - **Outputs**: None (loops until the program exits).

   ```python
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
   ```

---

## How the Program Works (User Interaction)

1. **User Registration**:
   - The user is prompted to enter a username and password.
   - The program will check if the username is unique.
     - If the username is available, it will be added to the dictionary, and the user is notified of successful registration.
     - If the username already exists, the user is asked to choose another username.

2. **Login**:
   - The user is asked if they want to log in after registering.
   - If they choose to log in, they will enter their username and password.
   - The program verifies the username and password combination.
     - If both are correct, the user is logged in successfully.
     - If either is incorrect, the user is given up to 3 attempts to try again.
     - If they fail after 3 attempts, the program will lock them out and exit.

3. **Exit**:
   - At any point, the user can choose to exit the program by selecting "no" when prompted for login.

---

## Example Usage

```plaintext
=== User Registration ===

Enter your user name: john
Enter your password: secret

User Created Successfully!

Please proceed to log in.

Do you wish to proceed to login (yes or no) : yes
Enter your user name: john
Enter your password: secret

Welcome, john! You have successfully logged in!!

Thank you very much.
Good Bye
```

---

## Limitations

- **Temporary Data Storage**: All user data is stored in a dictionary that is cleared when the program exits. If you want to persist data beyond a single session, you would need to integrate file handling or a database.
- **Password Security**: The program does not store passwords securely. In a real application, you should hash passwords and use proper security practices.
  
---
