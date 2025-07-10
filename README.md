# Python Password Strength Checker

## Project Overview

This project is a simple command-line tool written in Python that evaluates the strength of a given password. It helps users understand common weaknesses in their chosen passwords and promotes better security practices. This tool demonstrates fundamental Python programming skills, string manipulation, regular expressions, and basic cybersecurity principles.

## Features

* **Length Check:** Assesses if the password meets a recommended minimum length.
* **Character Diversity:** Checks for the presence of:
    * Lowercase letters
    * Uppercase letters
    * Numbers
    * Special characters
* **Common Password Detection:** Compares the input password against a small, predefined list of highly common/leaked passwords to immediately flag them as "Very Weak."
* **Detailed Feedback:** Provides a strength rating (e.g., "Weak," "Strong") and a list of specific reasons or suggestions for improvement.

## Cybersecurity Concepts Demonstrated

* **Password Policies:** Understanding and implementing criteria for strong passwords.
* **Entropy (Implicit):** The more diverse characters and length a password has, the higher its entropy, making it harder to guess or crack.
* **Common Attack Vectors:** Recognizing that common passwords are the first targets for brute-force or dictionary attacks.
* **Data Validation:** Using code to enforce security best practices for user input.
* **Hashing (Future Scope):** While this project doesn't use hashing for *password storage*, the concept of comparing input against a known list (even if plain text in this simple version) hints at how hashes are used to store and compare passwords securely without storing the actual password.

## How to Run

1.  **Save the files:**
    * Save the Python code as `password_checker.py`.
    * Create a text file named `common_passwords.txt` in the **same directory** as `password_checker.py` and populate it with common passwords (one per line, see example in repository).

2.  **Open your terminal or command prompt.**

3.  **Navigate to the directory** where you saved the files.

4.  **Run the script:**
    ```bash
    python password_checker.py
    ```

5.  **Enter a password** when prompted. Type `exit` to quit the program.

## Example Usage