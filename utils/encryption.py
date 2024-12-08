from cryptography.fernet import Fernet

def generate_key():
    print("Generating encryption key...")
    return Fernet.generate_key()

def encrypt_data(data, key):
    cipher = Fernet(key)
    return cipher.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data).decode()
