import pycipher
import random
import string
import hashlib
import binascii
import os, base64
# from ..src.hbv_code import hbv_encrypt, hbv_decrypt, random_key_generator, derive_key_from_word
# import hbv_code which is in a `src` folder in the parent directory
from hbv_code import hbv_encrypt, hbv_decrypt, random_key_generator, derive_key_from_word


def modify_key(original_key):
    key_length = len(original_key)
    num_modifications = int(key_length * 0.1) # calculate 10% of key length
    modification_indices = random.sample(range(key_length), num_modifications) # randomly select modification indices
    modified_key = list(original_key)
    for index in modification_indices:
        modified_key[index] = random.choice(string.ascii_lowercase) # replace character with random lowercase letter
    modified_key = ''.join(modified_key)
    return modified_key

def percentage_change(original_key, modified_key):
    if len(original_key) != len(modified_key):
        return None  # keys are not of same length
    num_different_chars = sum(1 for a, b in zip(original_key, modified_key) if a != b)
    return (num_different_chars / len(original_key)) * 100

def get_random_indices(text):
    text_length = len(text)
    half_text_length = text_length // 2
    quarter_text_length = text_length // 4
    if half_text_length > quarter_text_length:
        half_text_length, quarter_text_length = quarter_text_length, half_text_length
    min_index = random.randint(half_text_length, quarter_text_length)
    max_index = random.randint(half_text_length, quarter_text_length)
    while max_index == min_index:
        max_index = random.randint(half_text_length, quarter_text_length)
    return min_index, max_index


def main():
    print("=============================================")
    print("Hybrid Vigenere Beaufort Cipher | Key Sensitivity Analysis")
    print("=============================================")
    plaintext = input("Enter the plaintext: ").upper()
    print("==============================================\n==================================")
    word1, word2 = random_key_generator(16, 24)
    key1 = derive_key_from_word(word1)
    key2 = derive_key_from_word(word2)
    print("Beaufort Key:",word1)
    print("Vigenere Key:",word2)
    ciphertext = hbv_encrypt(plaintext, key1, key2)
    print("=============================================")
    print("Ciphertext from HBV: " + ciphertext)
    plaintext = hbv_decrypt(ciphertext, key1, key2)
    print("=============================================")
    print("Decrypted output with orginal keys : " + plaintext)
    word3 = modify_key(word1)
    word4 = modify_key(word2)
    print("===============================================")
    print("Beaufort Key:",word1)
    print("Modified Beaufort Key",word2)
    percentage = percentage_change(word1, word3)
    print(f"Percentage of change is {round(percentage, 2)}%")
    # print("Length of the beaufort Key:",len(key1))
    print("===============================================")
    print("Vignerekey:",word2)
    print("Modified vigenerekey",word4)
    percentage = percentage_change(word2, word4)
    print(f"Percentage of change is {round(percentage, 2)}%")
    # print("Length of the vignerekey:",len(key2))
    m_plaintext = hbv_decrypt(ciphertext, word3, word4)
    print("=============================================")
    print("Output with modified key  " + m_plaintext)
    percentage = percentage_change(plaintext, m_plaintext)
    print(f"Percentage of change is {round(percentage, 2)}%")

if __name__ == "__main__":
    main()




# Reference
# https://pycipher.readthedocs.io/en/master/ (Official Documentation of pycipher library)