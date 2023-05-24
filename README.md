# Image Steganography Using HBV and Padded RSA

This repository contains the implementation of a secure communication system using HBV, RSA encryption, and image-based Steganography.

## Diagram

Please refer to the Architectural Block Diagram for a visual overview of the system architecture and flow of data.
![enter image description here](test.test)

## Code Organization

The code in this repository is organized as follows:

-   `/src`: This directory contains all source code files for the project.
    -   `rsa_code.py`: This file contains functions related to RSA encryption and decryption, as well as generating and loading RSA keys.
    -   `hbv_code.py`: This file contains functions related to HBV encryption and decryption, deriving keys from words and generating random keys.
    -   `lsb_code.py`: This file contains functions related to least significant bit (LSB) steganography, specifically encoding and decoding messages within images.
-   `/data`: This directory contains any data files used or produced by the project.
	- `/cover` : This directory contains cover images used by the project.
	- `/messages` : This directory contains message files used by the project.
-   `/exp`: This directory is used to store results of any experiments conducted as part of the project.

## How It Works

This project implements a secure communication system using a combination of different encryption techniques.

1.  **RSA Encryption**: The RSA algorithm is used for secure data transmission. The public key is used for encryption and the private key is used for decryption.
    
2.  **HBV Encryption**: HBV is a symmetric encryption method. It uses a shared key for both encryption and decryption. The key is derived from a word input by the user.
    
3.  **Steganography**: Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. In this case, the LSB steganography technique is used to hide encrypted messages within an image.

### Functions and Usage
| Function | Description | Usage |
| --- | --- | --- |
| rsaencrypt | Encrypts a message using RSA encryption. | `rsaencrypt(public_key, message)` |
| rsadecrypt | Decrypts a message using RSA decryption. | `rsadecrypt(private_key, encrypted_message)` |
| generateKeys | Generates a new RSA public-private key pair. | `public_key, private_key = generateKeys()` |
| loadPrivateKey | Loads a RSA private key from a file. | `private_key = loadPrivateKey('path/to/privatekey.pem')` |
| loadPublicKey | Loads a RSA public key from a file. | `public_key = loadPublicKey('path/to/publickey.pem')` |
| hbv_encrypt | Encrypts a message using HBV encryption. | `encrypted_message = hbv_encrypt(key, message)` |
| hbv_decrypt | Decrypts a message using HBV decryption. | `decrypted_message = hbv_decrypt(key, encrypted_message)` |
| derive_key_from_word | Derives an encryption key from a password or word. | `key = derive_key_from_word('password')` |
| random_key_generator | Generates a random encryption key. | `key = random_key_generator()` |
| lsb_encode | Encodes a message into an image using LSB steganography. | `image_with_message = lsb_encode('path/to/image.png', 'Secret Message')` |
| lsb_decode | Decodes a message from an image using LSB steganography. | `message = lsb_decode('path/to/image_with_message.png')` |



The combination of these techniques provides two layers of security for the transmitted message. First, it is encrypted using the RSA and HBV methods. Then, the encrypted message is concealed within an image using steganography, making it extremely difficult to detect and decrypt.

## Getting Started

To run the code, you will need to import the functions from the relevant files as follows:

python

`from rsa_code import rsaencrypt, rsadecrypt, generateKeys, loadPrivateKey, loadPublicKey
from hbv_code import hbv_encrypt, hbv_decrypt, derive_key_from_word, random_key_generator
from lsb_code import lsb_encode, lsb_decode` 

Ensure that you have the necessary dependencies installed, including the necessary cryptographic and image processing libraries.



