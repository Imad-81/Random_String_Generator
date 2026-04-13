import secrets
import string

length = 64
characters = string.ascii_letters + string.digits + string.punctuation

secret_key = ''.join(secrets.choice(characters) for _ in range(length))

print(secret_key)