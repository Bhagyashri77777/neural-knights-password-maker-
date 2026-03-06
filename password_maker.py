import random

print("--- Neural Knights Password Maker ---")
print("By Team Leader: Bhagyashri")

# A simple way to list all our characters
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

# Adding them all together
all_chars = letters + numbers + symbols

# Asking for a number
length = int(input("How long should the password be? "))

# Starting with an empty password
my_password = ""

# A very basic college-level loop to pick random characters
for i in range(length):
    random_char = random.choice(all_chars)
    my_password = my_password + random_char

print("\nYour new password is:")
print(my_password)
