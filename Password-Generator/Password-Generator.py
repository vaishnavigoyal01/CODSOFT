import random
import string

def generate_password(length):
    if length < 8:
        print("Error: Password length must be at least 8 characters.")
        return None
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = []

    for i in range(length):
        random_character = random.choice(all_characters)
        password.append(random_character)

    return ''.join(password)

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 8:
                print("Error: Password length must be at least 8 characters.")
            else:
                return length
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    length = get_user_input()
    password = generate_password(length)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()