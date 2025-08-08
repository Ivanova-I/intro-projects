import random
import string
import secrets

def generate_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

print(f' Your randomly generated password ist {generate_password()}')