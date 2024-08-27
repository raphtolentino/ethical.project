import random
import string
import datetime
import time

# TODO: Add JSON Encryption.
# TODO: Add User feature.

def generate_password(length=15):  # length is 15 characters
    # Generate a random password of the specified length.
    characters = (
        string.ascii_letters + string.digits + string.punctuation
    )  # it accepts letters, digits and punctuations
    password = "".join(
        random.choice(characters) for _ in range(length)
    )  # password is a fusion between the 3 parameters.
    return password
def log_password(password, description, log_file="password_log.txt"):
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y")  # saves the Entry date
    with open(log_file, "a") as file:
        file.write(f"Entry Date: {timestamp}\n")  # writes the date
        file.write(f"Entry Title : {description} \n")  # writes the description
        file.write(f"Entry Password: {password}\n\n")  # writes the password

def prints():
    print("""\
    ┌──────────────────────────────────────────────────────────┐
    │░█▀▀░▀█▀░█░█░▀█▀░█▀▀░█▀█░█░░░░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀│
    │░█▀▀░░█░░█▀█░░█░░█░░░█▀█░█░░░░░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░│
    │░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░│
    └──────────────────────────────────────────────────────────┘""")
    length = 15
    time.sleep(0.5)
    description = input("Enter a description for the password: ")
    password = generate_password(length)
    log_password(password, description)
    time.sleep(0.5)
    print("Password was generated and saved.\n", "Good bye")  # goodbye message


def main():
    prints()
if __name__ == "__main__":
    main()
