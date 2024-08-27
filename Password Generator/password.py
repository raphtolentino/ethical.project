import random
import string
import datetime
import json
from cryptography.fernet import Fernet

# ASCII Art for the program title
def print_title():
    print("""\
                                                                                                                                                      
            Password Generator Manager                                                                                                                                                
                                                                                                                                                            
    """)

# Generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# Load or create encryption key
def load_key(key_file='secret.key'):
    try:
        with open(key_file, 'rb') as file:
            key = file.read()
    except FileNotFoundError:
        key = generate_key()
        with open(key_file, 'wb') as file:
            file.write(key)
    return key

# Encrypt the content
def encrypt_content(content, key):
    fernet = Fernet(key)
    return fernet.encrypt(content.encode()).decode()

# Decrypt the content
def decrypt_content(encrypted_content, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_content.encode()).decode()

# Save encrypted JSON to a file
def save_encrypted_json(file_name, encrypted_content):
    with open(file_name, 'w') as file:
        file.write(encrypted_content)

# Load encrypted JSON from a file
def load_encrypted_json(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# Generate a random password
def generate_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Create encrypted JSON
def create_encrypted_json(password, description, key):
    log_entry = {
        'Entry Date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        'Description': description,
        'Password': password
    }
    json_content = json.dumps(log_entry, indent=4)
    encrypted_content = encrypt_content(json_content, key)
    return encrypted_content

def main():
    print_title()
    while True:
        print("\nOptions:")
        print("1. Generate and save a new password")
        print("2. Decrypt and display the saved password")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            key = load_key()
            length = int(input("Enter the length of the password (default 15): ") or 15)
            description = input("Enter a description for the password: ")
            password = generate_password(length)
            encrypted_json = create_encrypted_json(password, description, key)
            
            file_name = 'encrypted_password.json'
            save_encrypted_json(file_name, encrypted_json)
            
            print(f"Encrypted JSON has been saved to {file_name}")
        
        elif choice == '2':
            key_input = input("Enter the secret key for decryption: ").strip().encode()
            try:
                key = Fernet(key_input)
                file_name = 'encrypted_password.json'
                encrypted_json = load_encrypted_json(file_name)
                decrypted_json = decrypt_content(encrypted_json, key_input)
                log_entry = json.loads(decrypted_json)
                print("Decrypted JSON:\n", json.dumps(log_entry, indent=4))
            except Exception as e:
                print(f"Failed to decrypt or read the file: {e}")
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
