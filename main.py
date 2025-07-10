import re
import os

def check_password_strength(password):
    """
    Evaluates the strength of a given password based on several criteria.

    Args:
        password (str): The password string to evaluate.

    Returns:
        tuple: A tuple containing a string indicating strength ("Very Weak", "Weak", "Moderate", "Strong", "Very Strong")
               and a list of reasons if the password is not strong.
    """
    reasons = []
    strength_score = 0

    # --- Criteria 1: Length ---
    if len(password) < 8:
        reasons.append("Password is too short (min 8 characters recommended).")
    elif len(password) >= 8 and len(password) < 12:
        strength_score += 1
        reasons.append("Length is acceptable, but longer is better (>=12 for higher score).")
    elif len(password) >= 12:
        strength_score += 2
        reasons.append("Excellent length.")

    # --- Criteria 2: Character Diversity ---
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        reasons.append("Missing lowercase letters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        reasons.append("Missing uppercase letters.")

    # Check for numbers
    if re.search(r"\d", password):
        strength_score += 1
    else:
        reasons.append("Missing numbers.")

    # Check for special characters (e.g., !@#$%^&*()-_+=)
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?`~]", password):
        strength_score += 1
    else:
        reasons.append("Missing special characters.")

    # --- Criteria 3: Common Password Check ---
    common_passwords_file = "common_passwords.txt"
    if os.path.exists(common_passwords_file):
        with open(common_passwords_file, 'r') as f:
            common_passwords = {line.strip() for line in f} # Use a set for faster lookup
            if password in common_passwords:
                strength_score = 0 # Immediately make it very weak
                reasons.insert(0, "Password is a very common/leaked password!")
    else:
        reasons.append(f"Warning: '{common_passwords_file}' not found. Cannot check against common passwords.")


    # --- Determine overall strength ---
    if strength_score >= 5:
        strength_level = "Very Strong"
    elif strength_score == 4:
        strength_level = "Strong"
    elif strength_score == 3:
        strength_level = "Moderate"
    elif strength_score == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"

    return strength_level, reasons

def main():
    """
    Main function to get user input and display password strength.
    """
    print("--- Python Password Strength Checker ---")
    print("Enter a password to check its strength (type 'exit' to quit).")

    while True:
        password = input("\nEnter your password: ")
        if password.lower() == 'exit':
            break

        strength, reasons = check_password_strength(password)

        print(f"\nPassword: '{password}'")
        print(f"Strength: {strength}")
        if reasons:
            print("Reasons/Suggestions:")
            for reason in reasons:
                print(f"  - {reason}")
        else:
            print("Excellent password! No obvious weaknesses found.")

if __name__ == "__main__":
    main()