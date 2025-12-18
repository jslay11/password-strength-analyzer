# Password Strength Analyzer

## Project Overview
The Password Strength Analyzer is a Python-based security automation tool designed to evaluate the strength of user passwords and provide actionable feedback to improve weak credentials. Weak passwords are a common attack vector, and this project demonstrates how security checks can be automated to support stronger password hygiene.

This tool analyzes passwords based on length, character variety, common password usage, and predictable patterns, then assigns a strength rating and recommendations for improvement.

---

## Features
- Password length analysis
- Uppercase, lowercase, numeric, and special character checks
- Detection of common and weak passwords
- Detection of predictable patterns and sequences
- Scoring system (0–10) with strength labels:
  - Weak
  - Moderate
  - Strong
- Clear findings and improvement suggestions

---

## How It Works
1. The user enters a password via the command line.
2. The program evaluates the password against multiple security criteria.
3. A numeric score and strength label are generated.
4. Findings and suggestions are displayed to help the user strengthen their password.

---

## Requirements / Dependencies
- Python 3.8 or higher
- No external libraries required (uses Python standard library only)

---

## How to Run
1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the script using the command:

```bash
python password_analyzer.py
