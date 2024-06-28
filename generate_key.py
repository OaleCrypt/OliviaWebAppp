import os
from cryptography.fernet import Fernet

key_path = 'password_manager/key.key'

def generate_key():
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(key_path, "rb").read()

if not os.path.exists(key_path):
    generate_key()
else:
    print("Key file already exists.")
