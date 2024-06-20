from cryptography.fernet import Fernet

def write_key():
    """Generates a key and saves it into a file"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as key.key")

write_key()
