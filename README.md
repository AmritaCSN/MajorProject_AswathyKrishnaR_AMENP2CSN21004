# Image Steganography Using HBV and Padded RSA

This repository contains the implementation of a secure communication system using HBV, RSA encryption, and image-based Steganography.

## Diagram

Please refer to the Architectural Block Diagram for a visual overview of the system architecture and flow of data.
![Workflow/Architectural Diagram](https://github.com/AmritaCSN/MajorProject_AswathyKrishnaR_AMENP2CSN21004/blob/main/Fig5.png)

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


The combination of these techniques provides two layers of security for the transmitted message. First, it is encrypted using the RSA and HBV methods. Then, the encrypted message is concealed within an image using steganography, making it extremely difficult to detect and decrypt.

## Getting Started

To run the code, you will need to import the functions from the relevant files as follows:

python

`from rsa_code import rsaencrypt, rsadecrypt, generateKeys, loadPrivateKey, loadPublicKey
from hbv_code import hbv_encrypt, hbv_decrypt, derive_key_from_word, random_key_generator
from lsb_code import lsb_encode, lsb_decode` 

Ensure that you have the necessary dependencies installed, including the necessary cryptographic and image processing libraries.



