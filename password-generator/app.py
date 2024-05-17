import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    chars = ''
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    print("--------------------------------")

    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("--------------------------------")
        print("ERR! Invalid input!")
        return
    
    use_uppercase = input("Include uppercase letters? (Y/n): ").lower() != 'n'
    use_lowercase = input("Include lowercase letters? (Y/n): ").lower() != 'n'
    use_numbers = input("Include numbers? (Y/n): ").lower() != 'n'
    use_special_chars = input("Include special characters? (Y/n): ").lower() != 'n'

    if not any([use_lowercase,use_uppercase,use_numbers,use_special_chars]):
        print("--------------------------------")
        print("Password cannot be generated!")
        return
    
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
    print("--------------------------------")
    print("Generated Password:", password)
    print("--------------------------------")

if __name__ == "__main__":
    main()
