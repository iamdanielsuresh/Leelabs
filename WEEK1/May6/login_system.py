#!/usr/bin/env python3

import time
import getpass

# Simple user database (in a real app, this would be stored securely)
# Format: {username: password}
users = {
    "admin": "admin123",
    "user1": "password123",
    "guest": "guest"
}

def authenticate(username, password):
    """
    Check if the username exists and the password matches
    
    Args:
        username (str): The username to check
        password (str): The password to verify
        
    Returns:
        bool: True if authentication is successful, False otherwise
    """
    # Check if username exists and password matches
    if username in users and users[username] == password:
        return True
    return False

def login_prompt():
    """Display login prompt and handle authentication"""
    
    # Track login attempts
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nLogin System")
        print("------------")
        
        # Get username
        username = input("Username: ").strip()
        
        # Check if username exists
        if not username:
            print("Error: Username cannot be empty")
            continue
            
        # In a real application, you'd use getpass to hide the password
        # But we'll use regular input for simplicity in this example
        try:
            # Note: getpass doesn't work well in all environments
            # password = getpass.getpass("Password: ")
            password = input("Password: ")
        except Exception:
            print("\nError reading password input")
            continue
            
        # Check credentials
        if authenticate(username, password):
            print(f"\nWelcome, {username}!")
            print("Login successful")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Invalid username or password. {remaining} attempts remaining.")
            else:
                print("Too many failed login attempts. Please try again later.")
                # In a real application, you might implement a timeout here
                time.sleep(2)  # Short delay
                
    return False

def main():
    print("Simple Login System")
    print("------------------")
    print("Available users: admin, user1, guest")
    print("(For the demo, passwords are 'admin123', 'password123', and 'guest')")
    
    while True:
        choice = input("\nChoose an option:\n1. Login\n2. Exit\nChoice: ")
        
        if choice == '1':
            if login_prompt():
                print("\nYou are now logged in!")
                # In a real app, you'd show a menu of user actions here
                print("What would you like to do?")
                print("1. View profile")
                print("2. Change settings")
                print("3. Logout")
                
                action = input("Action (1-3): ")
                if action == '1':
                    print("Viewing profile... (demo)")
                elif action == '2':
                    print("Changing settings... (demo)")
                else:
                    print("Logging out...")
                    time.sleep(1)
            else:
                print("Login failed. Please try again later.")
                
        elif choice == '2':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()