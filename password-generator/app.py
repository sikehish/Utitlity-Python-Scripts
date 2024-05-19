import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    """
    Generate a random password based on specified criteria.
    
    Parameters:
    length (int): The desired length of the password.
    use_uppercase (bool): Whether to include uppercase letters in the password.
    use_lowercase (bool): Whether to include lowercase letters in the password.
    use_numbers (bool): Whether to include numbers in the password.
    use_special_chars (bool): Whether to include special characters in the password.
    
    Returns:
    str: The generated password.
    """
    chars = ''
    # Add characters based on the specified criteria
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    
    # Generate the password by randomly selecting characters from the combined character set
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    """
    Main function to generate a password based on user input.
    """
    print("Welcome to Password Generator!")
    print("--------------------------------")

    try:
        length = int(input("Enter desired password length: "))  # Prompt user for password length
    except ValueError:
        print("--------------------------------")
        print("ERR! Invalid input!")  # Handle invalid input
        return
    
    # Prompt user for password criteria
    use_uppercase = input("Include uppercase letters? (Y/n): ").lower() != 'n'
    use_lowercase = input("Include lowercase letters? (Y/n): ").lower() != 'n'
    use_numbers = input("Include numbers? (Y/n): ").lower() != 'n'
    use_special_chars = input("Include special characters? (Y/n): ").lower() != 'n'

    # Check if at least one character set is selected
    if not any([use_lowercase, use_uppercase, use_numbers, use_special_chars]):
        print("--------------------------------")
        print("Password cannot be generated!")  # Print error message if no criteria selected
        return
    
    # Generate the password based on the specified criteria
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
    print("--------------------------------")
    print("Generated Password:", password)  # Print the generated password
    print("--------------------------------")

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
