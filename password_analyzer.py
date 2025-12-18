import re

# Small starter list of common weak passwords/patterns (expandable)
COMMON_PASSWORDS = {
    "password", "passw0rd", "123456", "12345678", "123456789", "qwerty",
    "letmein", "admin", "welcome", "iloveyou"
}

# Common patterns that tend to indicate weak passwords
COMMON_PATTERNS = [
    r"(.)\1\1",                 # any character repeated 3+ times (e.g., "aaa", "111")
    r"1234|2345|3456|4567|5678|6789|7890",  # common number sequences
    r"qwerty|asdf|zxcv",         # common keyboard walks
]


def analyze_password(password: str) -> dict:
    """
    Analyze a password and return a result dictionary containing:
    - score (0-10)
    - strength label (Weak/Moderate/Strong)
    - findings (list of issues found)
    - suggestions (list of improvements)
    """
    findings = []
    suggestions = []
    score = 0

    # ---- Length scoring (max 3 points) ----
    if len(password) >= 16:
        score += 3
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        suggestions.append("Increase length to 12+ characters (16+ is even better).")
    else:
        findings.append("Password is too short.")
        suggestions.append("Use at least 12 characters (minimum 8).")

    # ---- Character variety (max 4 points) ----
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\\[\]`~';:]", password))

    if has_upper:
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    if has_lower:
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    if has_digit:
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    if has_special:
        score += 1
    else:
        suggestions.append("Add at least one special character (example: !, @, #).")

    # ---- Common password check (penalty) ----
    if password.lower() in COMMON_PASSWORDS:
        findings.append("Password appears in a common-password list.")
        suggestions.append("Avoid common passwords—use a unique passphrase.")
        score -= 2

    # ---- Dictionary-style weak word check (basic heuristic) ----
    # NOTE: This is not a full dictionary attack. It's a simple indicator for obvious weak words.
    weak_words = ["password", "admin", "welcome", "letmein"]
    for w in weak_words:
        if w in password.lower():
            findings.append(f"Password contains a common weak word: '{w}'.")
            suggestions.append("Avoid using common words like 'password', 'admin', or 'welcome'.")
            score -= 1
            break

    # ---- Pattern checks (penalty) ----
    for pattern in COMMON_PATTERNS:
        if re.search(pattern, password.lower()):
            findings.append("Password contains a common predictable pattern.")
            suggestions.append("Avoid predictable sequences (e.g., 1234, qwerty) or repeated characters.")
            score -= 1
            break

    # Prevent negative scores
    if score < 0:
        score = 0

    # Cap score at 10
    if score > 10:
        score = 10

    strength = strength_label(score)

    # Remove duplicate suggestions (keep order)
    suggestions = list(dict.fromkeys(suggestions))

    return {
        "score": score,
        "strength": strength,
        "findings": findings,
        "suggestions": suggestions
    }


def strength_label(score: int) -> str:
    """
    Convert numeric score to a readable strength label.
    """
    if score <= 3:
        return "Weak"
    if score <= 7:
        return "Moderate"
    return "Strong"


def main() -> None:
    """
    Command-line entry point for the Password Strength Analyzer.
    """
    print("=== Password Strength Analyzer ===")
    password = input("Enter a password to analyze: ")

    result = analyze_password(password)

    print("\n--- Results ---")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}/10")

    if result["findings"]:
        print("\nFindings:")
        for item in result["findings"]:
            print(f"- {item}")

    if result["suggestions"]:
        print("\nSuggestions:")
        for tip in result["suggestions"]:
            print(f"- {tip}")
    else:
        print("\nNo suggestions needed—your password meets strong security guidelines.")


if __name__ == "__main__":
    main()
