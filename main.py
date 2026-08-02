import hashlib
import os
import json
from getpass import getpass


def master_password_exists():
    if not os.path.exists("master_password.json"):
        return False

    try:
        with open("master_password.json", "r") as f:
            data = json.load(f)

        return "master_password" in data

    except json.JSONDecodeError:
        return False

def create_master_password():

    while True:
       password = input("Enter master password: ").strip()
       if not password:
           print("Please enter a master password")
           continue

       confirm_password = input("Confirm master password: ").strip()
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

    if "master_password" not in data:
        print("Invalid master password file.")
        return False

    stored_password = data["master_password"]

    attempts = 3

    while attempts > 0:

        password = input("Enter master password: ").strip()
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
        print("Password file not found. Creating a new vault.")
        return []

    except json.JSONDecodeError:
        print("Password file is corrupted.")
        return []

def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f, indent=4)

def add_password():

    passwords = load_passwords()

    while True:
        try:
            password_id = int(input("Enter ID: "))

        except ValueError:
            print("ID must be an integer.")
            continue

        if password_id <= 0:
            print("ID must be +ve integer.")
            continue

        duplicate_found = False

        for existing_password in passwords:
            if existing_password["id"] == password_id:
                duplicate_found = True
                break

        if duplicate_found:
            print("ID already exists. Enter another ID.")
            continue

        break

    while True:
        website = input("Enter website: ").strip()

        if not website:
            print("Please enter a website.")
            continue

        break

    while True:
        username = input("Enter username: ").strip()

        if not username:
            print("Please enter a username.")
            continue

        break

    while True:
        password = input("Enter master password: ").strip()

        if not password:
            print("Please enter a password.")
            continue

        break

    password_entry = {
        "id": password_id,
        "website": website,
        "username": username,
        "password": password
    }

    passwords.append(password_entry)
    save_passwords(passwords)
    print("Password added successfully.")



if not master_password_exists():
    create_master_password()


if login():
    print("Loading Password Manager...")
else:
    print("Too many failed login attempts.")
    exit(0)



