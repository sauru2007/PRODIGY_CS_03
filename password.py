import re

def assess_password_strength(password):
    """Assess the strength of a password."""
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in password)

    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    strength_levels = {0: "Very Weak", 1: "Weak", 2: "Moderate", 3: "Strong", 4: "Very Strong", 5: "Excellent"}
    return strength_levels[strength], feedback

def main():
    print("Password Strength Assessment Tool")
    while True:
        print("\nOptions:")
        print("1. Assess password strength")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            password = input("Enter the password to assess: ")
            strength, feedback = assess_password_strength(password)
            print(f"Password Strength: {strength}")
            if feedback:
                print("Feedback:")
                for f in feedback:
                    print(f"- {f}")

        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
