# Welcome to Secure Code Game Season-1/Level-5!

# This is the last level of our first season, good luck!

import binascii
import secrets
import hashlib
import os
import bcrypt

class Random_generator:
    # Generates a cryptographically secure random token
    def generate_token(self, length=8, alphabet="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    # Generates a secure bcrypt salt
    def generate_salt(self, rounds=12):
        return bcrypt.gensalt(rounds)

class SHA256_hasher:
    # Hashes a password using SHA-256 and bcrypt
    def password_hash(self, password, salt):
        hashed_pw = hashlib.sha256(password.encode()).digest()
        return bcrypt.hashpw(hashed_pw, salt).decode('utf-8')

    # Verifies a hashed password
    def password_verification(self, password, password_hash):
        hashed_pw = hashlib.sha256(password.encode()).digest()
        return bcrypt.checkpw(hashed_pw, password_hash.encode('utf-8'))

class MD5_hasher:
    # Hashes a password using MD5 (⚠️ **MD5 is insecure**)
    def password_hash(self, password):
        return hashlib.md5(password.encode()).hexdigest()

    # Verifies an MD5-hashed password securely
    def password_verification(self, password, password_hash):
        return secrets.compare_digest(self.password_hash(password), password_hash)

# Securely retrieve sensitive keys from environment variables
PRIVATE_KEY = os.environ.get('PRIVATE_KEY', 'default_private_key')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY', 'default_public_key')
SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(16))  # Generate a secure default secret
PASSWORD_HASHER = 'SHA256_hasher'  # Using SHA-256 for better security


# Contribute new levels to the game in 3 simple steps!
# Read our Contribution Guideline at github.com/skills/secure-code-game/blob/main/CONTRIBUTING.md