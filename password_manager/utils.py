from cryptography.fernet import Fernet
import os
from django.conf import settings

def load_key():
    key_path = os.path.join(settings.BASE_DIR, 'password_manager', 'key.key')
    with open(key_path, "rb") as key_file:
        key = key_file.read()
    return key

def write_key():
    key = Fernet.generate_key()
    key_path = os.path.join(settings.BASE_DIR, 'password_manager', 'key.key')
    with open(key_path, "wb") as key_file:
        key_file.write(key)

key = load_key()
fer = Fernet(key)

def view_passwords(username):
    passwords = []
    file_path = os.path.join(settings.BASE_DIR, 'password_manager', 'passwords.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f.readlines():
                user, encrypted_pass = line.strip().split("|")
                if user == username:  # Only return passwords for the specified username
                    passwords.append((user, encrypted_pass))  # Do not decrypt
    return passwords

def add_password(account_name, password):
    encrypted_password = fer.encrypt(password.encode()).decode()
    file_path = os.path.join(settings.BASE_DIR, 'password_manager', 'passwords.txt')
    with open(file_path, 'a') as f:
        f.write(f"{account_name}|{encrypted_password}\n")
