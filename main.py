import re

# List of common passwords to avoid
COMMON_PASSWORDS = [
    "123456", "password", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123", "111111", "123123"
]


def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Check for uppercase, lowercase, digits, and special characters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[]{};:,.<>?/\\|`~" for char in password)

    if not (has_upper and has_lower and has_digit and has_special):
        return ("Weak: Password must include uppercase letters, lowercase letters, digits, "
                "and special characters.")

    # Check for common passwords
    if password in COMMON_PASSWORDS:
        return "Weak: Password is too common. Choose a unique password."

    return "Strong: Your password is secure."


if __name__ == "__main__":
    print("Password Strength Checker")
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print(result)
