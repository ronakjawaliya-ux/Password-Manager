import hashlib
import os
from getpass import getpass


def master_password_exists():
    return os.path.exists("master_password.json")




password = getpass("Enter password: ")
password = password.encode()
password_hash = hashlib.sha256(password).hexdigest()
print(password_hash)

