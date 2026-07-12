import secrets
import string

def generate_password(length):
    """Generate a secure random password."""
    if length < 8:
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    """Check password strength."""
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"

def save_password(password):
    """Save password to passwords.txt"""
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

# ---------------- MAIN PROGRAM ---------------- #
print("=" * 40)
print("      SecureKey Password Generator")
print("=" * 40)
print("Created by: Bhagyashri Yogesh Gawali\n")

try:
    length = int(input("Enter password length (minimum 8): "))
    password = generate_password(length)

    if password is None:
        print("\n❌ Password length must be at least 8 characters.")
    else:
        print("\n✅ Your Password:")
        print(password)
        print(f"\n🔐 Strength: {check_strength(password)}")

        choice = input("\nDo you want to save this password? (y/n): ").lower()
        if choice == "y":
            save_password(password)
            print("✅ Password saved successfully in passwords.txt")
        else:
            print("Password was not saved.")

except ValueError:
    print("\n❌ Please enter a valid number.")

print("\n✨ Thank you for using SecureKey!")