import re
def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength rating
    if strength == 5:
        rating = "Very Strong"
    elif strength == 4:
        rating = "Strong"
    elif strength == 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return {
        "password": password,
        "strength_score": strength,
        "rating": rating,
        "feedback": feedback
    }

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result = check_password_strength(pwd)
    print("\nPassword Strength Report:")
    print(f"Password: {result['password']}")
    print(f"Strength Score: {result['strength_score']} / 5")
    print(f"Rating: {result['rating']}")
    if result["feedback"]:
        print("Suggestions:")
        for tip in result["feedback"]:
            print(f" - {tip}")
