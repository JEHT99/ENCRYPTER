from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
#////////////////////////////////////////////////////////////////////////////////////////////////////
def generate_key():
    # Generate a 256-bit (32-byte) key for AES
    key = os.urandom(32)  # This is your encryption key (keep it secret!)
    file = open("crypto.key","wb")
    file.write(key)
    file.close()
#////////////////////////////////////////////////////////////////////////////////////////////////////
def read_key(filePath):
    file = open(filePath,"rb")
    key = file.read()
    file.close()
    return key
#////////////////////////////////////////////////////////////////////////////////////////////////////
def encrypt_text(key, plaintext):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Pad the plaintext to be a multiple of the block size (16 bytes for AES)
    padder = padding.PKCS7(128).padder()  # 128-bit padding
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Create AES cipher in CBC mode with the given key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Return both the IV and the ciphertext (IV is needed for decryption)
    return iv + ciphertext
#////////////////////////////////////////////////////////////////////////////////////////////////////
def decrypt_text(key, ciphertext):
    # Extract the IV from the ciphertext (first 16 bytes)
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]

    # Create AES cipher in CBC mode with the given key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

    # Remove the padding from the plaintext
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()
#////////////////////////////////////////////////////////////////////////////////////////////////////