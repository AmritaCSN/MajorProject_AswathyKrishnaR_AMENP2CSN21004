
# Image Steganography Using HBV and Padded RSA

This repository contains the implementation of a secure communication system using HBV, RSA encryption, and image-based Steganography.

## Diagram

Please refer to the Architectural Block Diagram for a visual overview of the system architecture and flow of data.
![Workflow/Architectural Diagram](https://github.com/AmritaCSN/MajorProject_AswathyKrishnaR_AMENP2CSN21004/blob/main/Fig5.png)
## Overview

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
  
## Code Organization

The code in this repository is organized as follows:

-   `/src`: This directory contains all source code files for the project.
    -	`main_code.py`: This is main code   
    -   `rsa_code.py`: This file contains functions related to RSA encryption and decryption, as well as generating and loading RSA keys.
    -   `hbv_code.py`: This file contains functions related to HBV encryption and decryption, deriving keys from words and generating random keys.
    -   `lsb_code.py`: This file contains functions related to least significant bit (LSB) steganography, specifically encoding and decoding messages within images.
-   `/data`: This directory contains any data files used or produced by the project.
	- `/cover` : This directory contains cover images used by the project.
	- `/messages` : This directory contains message files used by the project.
-   `/exp`: This directory is used to store analysis codes and results of any experiments conducted as part of the project.



## Running the Project

To run this project on your own machine, follow these steps:

1.  **Clone the Repository:** Use `git clone https://github.com/AmritaCSN/MajorProject_AswathyKrishnaR_AMENP2CSN21004.git` to clone this repository to your local machine.
    
2.  **Install Dependencies:** Ensure that you have the necessary Python libraries installed. These may include cryptographic and image processing libraries.
    
3.  **Run the Main Script:** Navigate to the `src` directory and run the `main_code.py` script. `python main_code.py`

## Libraries Used

Below is a brief explanation of the main Python libraries used in this project:

-   **rsa:** This library provides basic RSA cryptography. We use it here for RSA encryption and decryption.
- **pycipher:** This is a collection of classic cipher algorithms. We use it here for the Beaufort and Vigenere ciphers part of the HBV encryption/decryption.
-   **numpy:** Fundamental package for scientific computing in Python. It provides a powerful N-dimensional array object. In this project, it's used in image manipulation for the steganography component.
-   **cv2:** This is the OpenCV library for Python, used for real-time computer vision. It's used in this project for various image processing tasks.
-   **PIL (Python Imaging Library):** It's used in this project for various image processing tasks.
-   **matplotlib:** A plotting library for Python. It's used in this project to display histograms.
    

    

## References

The main references used for this project include the official Python documentation, library-specific documentation and relevant research papers:

1.  Python 3 documentation: [https://docs.python.org/3/](https://docs.python.org/3/)
2.  RSA in Python: [https://stuvel.eu/python-rsa-doc/](https://stuvel.eu/python-rsa-doc/)
6.  Pycipher documentation: [https://pycipher.readthedocs.io/en/master/](https://pycipher.readthedocs.io/en/master/)
3.  OpenCV documentation: [https://opencv.org/](https://opencv.org/)
4.  Matplotlib documentation: [https://matplotlib.org/](https://matplotlib.org/)
5.  Numpy documentation: [https://numpy.org/doc/](https://numpy.org/doc/)



