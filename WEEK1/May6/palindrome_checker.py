#!/usr/bin/env python3

def is_palindrome(text):
    """
    Check if the input string is a palindrome.
    A palindrome reads the same forward and backward, ignoring case, punctuation, and spaces.
    
    
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if the cleaned text equals its reverse
    return cleaned_text == cleaned_text[::-1]


def main():
    print("Palindrome Checker")
    print("-----------------")
    print("A palindrome is a word, phrase, or sequence that reads the same backward as forward.")
    print("Examples: 'radar', 'madam', 'A man, a plan, a canal, Panama!'")
    
    while True:
        user_input = input("\nEnter a string to check (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Thanks for using the palindrome checker!")
            break
            
        if not user_input.strip():
            print("Please enter a non-empty string.")
            continue
            
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome!")
        else:
            print(f"'{user_input}' is not a palindrome.")
            
        
        cleaned = ''.join(char.lower() for char in user_input if char.isalnum())
        if cleaned != user_input:
            print(f"Note: After removing spaces and punctuation: '{cleaned}'")


if __name__ == "__main__":
    main()