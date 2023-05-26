import base64
import hashlib
import pycipher
import random

# Beaufort Cipher code
def beaufort_encrypt(plaintext, key):
    beaufortkey = pycipher.Beaufort(key)
    ciphertext = beaufortkey.encipher(plaintext)
    return ciphertext

def beaufort_decrypt(ciphertext, key):
    beaufortkey = pycipher.Beaufort(key)
    plaintext = beaufortkey.decipher(ciphertext)
    return plaintext

# Vigenere Cipher code
def vigenere_encrypt(plaintext, key):
    vigenerekey = pycipher.Vigenere(key)
    ciphertext = vigenerekey.encipher(plaintext)
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    vigenerekey = pycipher.Vigenere(key)
    plaintext = vigenerekey.decipher(ciphertext)
    return plaintext

# Hybrid Vigener Beaufort Cipher code
def hbv_encrypt(plaintext, key1, key2):
    vigenerekey = pycipher.Vigenere(key1)
    beaufortkey = pycipher.Beaufort(key2)
    ciphertext = vigenerekey.encipher(beaufortkey.encipher(plaintext))
    return ciphertext

def hbv_decrypt(ciphertext, key1, key2):
    vigenerekey = pycipher.Vigenere(key1)
    beaufortkey = pycipher.Beaufort(key2)
    plaintext = beaufortkey.decipher(vigenerekey.decipher(ciphertext))
    return plaintext

def derive_key_from_word(word):
    salt = b'\x9a\x1f}\x8b\xf8\x03\xab\xd5\xf0\xe1\x9b\xde\x9e\x10\x15.'
    iterations = 10000 # number of iterations for PBKDF2
    key_length = 64 # desired length of the key
    key = hashlib.pbkdf2_hmac('sha256', word.encode('utf-8'), salt, iterations, key_length)
    key_str = base64.b64encode(key).decode('utf-8') # convert bytes to string
    filtered_key = ''.join(filter(lambda c: c.isalpha() and c.lower() >= 'a' and c.lower() <= 'z', key_str)) # filter out non-alphabetic characters and restrict to letters a-z
    return filtered_key

def random_key_generator(index1, index2):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result_str1 = ''.join(random.choice(letters) for i in range(index1))
    result_str2 = ''.join(random.choice(letters) for i in range(index2))
    return result_str1, result_str2
