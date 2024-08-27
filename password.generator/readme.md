# Password Generator & Decryptor

## Overview

Password Generator & Decryptor is a Python script that allows users to generate random passwords, encrypt them, and save them in a JSON file. It also supports decrypting the saved passwords when provided with the correct secret key. This tool is useful for securely managing passwords and handling sensitive information.

## Features

- Generate random passwords with customizable length.
- Encrypt passwords and save them in a JSON file.
- Decrypt and view saved passwords when provided with the correct secret key.
- Interactive menu for easy navigation between functionalities.
- ASCII art header for a visually appealing interface.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/password-generator-decryptor.git
    cd password-generator-decryptor
    ```

2. **Install the required Python libraries:**

    ```bash
    pip install cryptography
    ```

## Usage

1. **Run the script:**

    ```bash
    python password_generator.py
    ```

2. **Choose from the following options:**

    - **Generate and Save a New Password:**
      - Enter `1` when prompted.
      - Input the desired password length and a description.
      - The script will generate a new password, encrypt it, and save it to `encrypted_password.json`.

    - **Decrypt and Display the Saved Password:**
      - Enter `2` when prompted.
      - Provide the correct secret key to decrypt and view the saved password from `encrypted_password.json`.

    - **Exit the Program:**
      - Enter `3` to exit the script.

3. **Example:**

    ```bash
    Enter your choice (1, 2, or 3): 1
    Enter the length of the password (default 15): 20
    Enter a description for the password: MyTestPassword
    Encrypted JSON has been saved to encrypted_password.json

    Enter your choice (1, 2, or 3): 2
    Enter the secret key for decryption: <your_secret_key_here>
    Decrypted JSON:
    {
        "Entry Date": "27-08-2024 12:34:56",
        "Description": "MyTestPassword",
        "Password": "MyGeneratedPassword123!"
    }
    ```

## File Structure

- `password_generator.py`: The main script that handles password generation, encryption, decryption, and JSON file operations.
- `secret.key`: The file where the encryption key is stored (automatically created if it doesn't exist).
- `encrypted_password.json`: The file where the encrypted password is saved (created when generating a new password).

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request. Make sure to follow the project's code of conduct and contribution guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [your-email@example.com](mailto:your-email@example.com).

