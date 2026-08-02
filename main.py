import hashlib
import os
import json
from getpass import getpass


def master_password_exists():
    return os.path.exists("master_password.json")

def create_master_password():

    while True:
       password = getpass("Enter master password: ").strip()
       if not password:
           print("Please enter a master password")
           continue

       confirm_password = getpass("Confirm master password: ").strip()
       if not confirm_password:
           print("Please enter a master password")
           continue

       if password == confirm_password:

            password_hash = hashlib.sha256(password.encode()).hexdigest()

            with open("master_password.json", "w") as f:
                data = {
                    "master_password": password_hash
                }
                json.dump(data, f, indent=4)

            print(f'Master password created successfully. Please log in.')
            break

       else:
            print("Passwords do not match")
            continue

def login():
    try:
        with open("master_password.json", "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        print("Master password file not found.")
        return False

    except json.JSONDecodeError:
        print("Master password file is corrupted.")
        return False

    stored_password = data["master_password"]

    attempts = 3

    while attempts > 0:

        password = getpass("Enter master password: ").strip()
        if not password:
            attempts -= 1
            print("Please enter a master password")
            print("Attempts left:", attempts)
            continue

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        if stored_password == password_hash:
            print("Master password is correct.")
            return True

        else:
            attempts -= 1
            print("Master password is incorrect")
            print("Attempts left: ", attempts)

    return False

def load_passwords():
    try:
        with open("passwords.json", "r") as f:
            return json.load(f)

    except FileNotFoundError:
        print("Master password file not found.")
        return []

    except json.JSONDecodeError:
        print("Master password file is corrupted.")
        return []

def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f, indent=4)



if not master_password_exists():
    create_master_password()


if login():
    print("Loading Password Manager...")
else:
    print("Too many failed login attempts.")
    exit(0)

