import re

def analyze_password(password: str):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long (12+ is better).")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (ex: ! @ # $).")

    return score, feedback


def strength_label(score: int) -> str:
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    return "Strong"


def main():
    password = input("Enter a password to analyze: ")
    score, feedback = analyze_password(password)
    label = strength_label(score)

    print(f"\nPassword Strength: {label}")
    print(f"Score: {score}/6")

    if feedback:
        print("\nSuggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nGreat job! Your password meets strong security standards.")


if __name__ == "__main__":
    main()
