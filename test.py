from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Prompt user for input to encrypt
plaintext = input("Enter text to encrypt: ")

# Generate a 256-bit AES key
key = get_random_bytes(32)

# Create a new AES-GCM cipher object
cipher = AES.new(key, AES.MODE_GCM)

# Encrypt the plaintext
ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())

# Write the encrypted data and key to a file
with open("Ency-py.txt", "w") as f:
    f.write(f"original term: {plaintext}\n")
    f.write(f"encrypted text: {ciphertext.hex()}\n")
    f.write(f"key: {key.hex()}\n")

# Prompt user for input to decrypt
ciphertext_hex = input("Enter ciphertext to decrypt (in hex format): ")
ciphertext = bytes.fromhex(ciphertext_hex)

# Prompt user for input of the key
key_hex = input("Enter key to decrypt (in hex format): ")
key = bytes.fromhex(key_hex)

# Create a new AES-GCM cipher object with the given key
cipher = AES.new(key, AES.MODE_GCM)

# Decrypt the ciphertext
plaintext = cipher.decrypt(ciphertext).decode()

# Write the decrypted data and key to a file
with open("Dec-py.txt", "w") as f:
    f.write(f"encrypted text: {ciphertext_hex}\n")
    f.write(f"key: {key_hex}\n")
    f.write(f"decrypted text: {plaintext}\n")
