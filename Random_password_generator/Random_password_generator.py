
import secrets
import string

def generate_password(length, use_upper, use_lower,use_digits, use_symbols):
    characters = ""
    password_chars = []

    if use_upper:
        characters += string.ascii_uppercase
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        characters += string.ascii_lowercase
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        characters += string.digits
        password_chars.append(secrets.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()-_=+?"
        characters += symbols
        password_chars.append(secrets.choice(symbols))
    while len(password_chars) < length:
        password_chars.append(secrets.choice(characters))
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)
def main():
    print("=" * 35)
    print("     RANDOM PASSWORD GENERATOR")
    print("=" * 35)
    try:
        length = int(input("Enter password length (4-128): "))
        if not 4 <= length <= 128:
            print("Error: Length must be between 4 and 128.")
            return
        print("Choose character types (y/n):")
        upper = input("Uppercase letters (A-Z)? ").lower() == "y"
        lower = input("Lowercase letters (a-z)? ").lower() == "y"
        digits = input("Numbers (0-9)? ").lower() == "y"
        symbols = input("Special symbols (!@#$)? ").lower() == "y"
        if not any([upper, lower, digits, symbols]):
            print("Invalid! Select at least one character type.")
            return
        selected_types = sum([upper, lower, digits, symbols])
        if length < selected_types:
            print("Error: Length is too short for your choices.")
            return
        password = generate_password(
            length, upper, lower, digits, symbols
        )
        print("\nYour generated password is:", password)
        print("Password length:", len(password))
    except ValueError:
        print("Invalid! Please enter a valid whole number.")
if __name__ == "__main__":
    main()

