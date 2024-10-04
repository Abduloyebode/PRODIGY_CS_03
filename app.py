import re

def assess_password_strength(password):
    """
    Assesses the strength of a password based on various criteria.

    Args:
        password (str): The password to assess.

    Returns:
        str: A message indicating the password's strength.
    """
    strength = 0

    # Check password length
    if len(password) < 8:
        strength += 1
    elif len(password) >= 8 and len(password) < 12:
        strength += 2
    else:
        strength += 3

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1

    if strength <= 2:
        return "Weak password. Consider using a stronger password."
    elif strength == 3 or strength == 4:
        return "Medium password. You're close, but try to add more complexity."
    else:
        return "Strong password. Good job!"


def main():
    while True:
        print("Password Strength Assessment Tool")
        print("---------------------------------")
        print("1. Assess a password")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter a password: ")
            result = assess_password_strength(password)
            print(result)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()