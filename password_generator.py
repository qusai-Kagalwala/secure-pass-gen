import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while len(pwd) < min_length or not meets_criteria:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers and not has_number:
            meets_criteria = False
        if special_characters and not has_special:
            meets_criteria = False

    return pwd

min_length = int(input("Enter the minimum length of the password: "))
has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
has_special = input("Include special characters? (y/n): ").lower() == 'y'
pwd = generate_password(min_length, has_numbers, has_special)
print(f"Generated password: {pwd}")
