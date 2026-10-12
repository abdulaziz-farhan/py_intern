
from cryptography.fernet import Fernet, InvalidToken
import os

KEY_FILE = "key"

if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as f:
        f.write(Fernet.generate_key())

with open(KEY_FILE, "rb") as f:
    key = f.read().strip()

try:
    cipher = Fernet(key)
except ValueError:
    print("Invalid key. Delete the key file and restart.")
    exit()

mode = input("Enter e to encrypt or d to decrypt: ").lower()
name = input("Enter file name: ")

try:
    with open(name, "rb") as f:
        data = f.read()

    if mode == "e":
        result = cipher.encrypt(data)
        output = name + ".enc"
    elif mode == "d":
        result = cipher.decrypt(data)
        output = name.removesuffix(".enc") + ".dec"
    else:
        print("Invalid choice")
        exit()

    with open(output, "wb") as f:
        f.write(result)

    print("Completed:", output)

except FileNotFoundError:
    print("File not found")
except InvalidToken:
    print("Wrong key or invalid encrypted file")

