import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected. Please select at least one character type.")

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        if length < 1:
            print("Password length must be at least 1.")
            return

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Your generated password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
