
import random
import string

length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter a positive length")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)
