# Image Steganography Using HBV and Padded RSA

This repository contains the implementation of a secure communication system using HBV, RSA encryption, and image-based Steganography.

## Diagram

Please refer to the Architectural Block Diagram for a visual overview of the system architecture and flow of data.
![Workflow/Architectural Diagram](https://github.com/AmritaCSN/MajorProject_AswathyKrishnaR_AMENP2CSN21004/blob/main/Fig5.png)

## Code Organization

The code in this repository is organized as follows:

-   `/src`: This directory contains all source code files for the project.
    -	`main_code.py': This is main code   
    -   `rsa_code.py`: This file contains functions related to RSA encryption and decryption, as well as generating and loading RSA keys.
    -   `hbv_code.py`: This file contains functions related to HBV encryption and decryption, deriving keys from words and generating random keys.
    -   `lsb_code.py`: This file contains functions related to least significant bit (LSB) steganography, specifically encoding and decoding messages within images.
-   `/data`: This directory contains any data files used or produced by the project.
	- `/cover` : This directory contains cover images used by the project.
	- `/messages` : This directory contains message files used by the project.
-   `/exp`: This directory is used to store results of any experiments conducted as part of the project.

## How It Works

This project implements a secure communication system with encryption, decryption, and LSB techniques.


1.  **Message  Encryption**
     -   Generate two separate random keys of length 128 bits using a random function for        the Beaufort and Vigenere ciphers.
    -   Pass the keys through a Key Derivation Function (KDF) for added security.
    -   Encrypt the message using the HBV cipher with the keys derived from the KDF.
    -   Further encrypt the intermediate HBV ciphertext using RSA public key encryption.
    -   Embed the final ciphertext into a cover image using the LSB technique, resulting in a stego image.
  
 2.  **Secure Communication**
       -   Transfer the stego image through a secure communication channel to the receiver.
    
3. **Message Decryption**
    -   Retrieve the final ciphertext from the stego image using the LSB technique.
    -   Decrypt the extracted ciphertext using the receiver's RSA private key.
    -   Decrypt the intermediate ciphertext using HBV with the two keys derived from the KDF.
    -   Decrypt the Vigenere cipher-encrypted message using the second key derived from the KDF.
    -   Decrypt the resulting ciphertext using the Beaufort cipher with the first key derived from the KDF.


## Getting Started

To run the code, you will need to import the functions from the relevant files as follows:

python

`from rsa_code import rsaencrypt, rsadecrypt, generateKeys, loadPrivateKey, loadPublicKey
from hbv_code import hbv_encrypt, hbv_decrypt, derive_key_from_word, random_key_generator
from lsb_code import lsb_encode, lsb_decode` 

Ensure that you have the necessary dependencies installed, including the necessary cryptographic and image processing libraries.



