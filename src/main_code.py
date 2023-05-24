import time, cv2, datetime
from rsa_code import rsaencrypt, rsadecrypt, generateKeys, loadPrivateKey, loadPublicKey
from hbv_code import hbv_encrypt, hbv_decrypt, derive_key_from_word, random_key_generator
from lsb_code import lsb_encode, lsb_decode
# from rsa_aes_code import rsaencrypt, rsadecrypt, generateKeys, loadPrivateKey, loadPublicKey, hybridEncrypt, hybridDecrypt

def main():
    # Choose encode decode or generate rsa keys
    # If encode is chosen, accept the message file, beaufort key, vigenere key, rsa public key, cover image and output the stego image.
    # If decode is chosen, accept the stego image, beaufort key, vigenere key, rsa private key and output the message file.
    # If the user enters an invalid option, print an error message and exit.
    input_option = input("Enter 'encode', 'decode' or 'generate' to choose an option: ")
    if input_option == "encode":
        message_file = input("Enter the message file name: ") # ../data/message/msgtest.txt
        b_key, v_key = random_key_generator(8, 8)
        # beaufort_key_user_input = input("Enter the beaufort key: ")
        with open("beaufort_key.txt", "w") as f:
            f.write(b_key)
        # vigenere_key_user_input = input("Enter the vigenere key: ")
        with open("vigenere_key.txt", "w") as f:
            f.write(v_key)
        print("Beaufort key saved in beaufort_key.txt and vigenere key saved in vigenere_key.txt")
        beaufort_key = derive_key_from_word(b_key)
        vigenere_key = derive_key_from_word(v_key)
        rsa_public_key = input("Enter the rsa public key file name: ")
        cover_image = input("Enter the cover image file name: ")
        # Generate stego image file name from cover image file name
        # stego_image = "output_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        stego_image = "output_image.png"
        start_time = time.time()
        with open(message_file, "r") as f:
            message = f.read()
        hbv_encrypted_message = hbv_encrypt(message, vigenere_key, beaufort_key)
        public_key = loadPublicKey(rsa_public_key)
        # rsa_encrypted_message = rsaencrypt(hbv_encrypted_message, public_key)
        rsa_encrypted_message = rsaencrypt(hbv_encrypted_message, public_key)
        lsb_encoded_image = lsb_encode(cover_image, rsa_encrypted_message)
        print("Stego image file name: ", stego_image)
        cv2.imwrite(stego_image, lsb_encoded_image)
        end_time = time.time()
        print("Time taken : ", end_time - start_time)
    elif input_option == "decode":
        stego_image = input("Enter the stego image file name: ")
        load_beaufort_key = input("Enter the beaufort key file name: ")
        with open(load_beaufort_key, "r") as f:
            beaufort_key_word = f.read()
        beaufort_key = derive_key_from_word(beaufort_key_word)
        load_vigenere_key = input("Enter the vigenere key file name: ")
        with open(load_vigenere_key, "r") as f:
            vigenere_key_word = f.read()
        vigenere_key = derive_key_from_word(vigenere_key_word)
        rsa_private_key = input("Enter the rsa private key: ")
        # Generate message file name from stego image file name
        message_file = stego_image.split(".")[0] + "_message.txt"
        start_time = time.time()
        lsb_decoded_message = lsb_decode(stego_image)
        private_key = loadPrivateKey(rsa_private_key)
        # rsa_decrypted_message = rsadecrypt(lsb_decoded_message, private_key)
        rsa_decrypted_message = rsadecrypt(lsb_decoded_message, private_key) 
        hbv_decrypted_message = hbv_decrypt(rsa_decrypted_message, vigenere_key, beaufort_key)
        with open(message_file, "w") as f:
            f.write(hbv_decrypted_message)
        end_time = time.time()
        print("Time taken : ", end_time - start_time)
    elif input_option == "generate":
        generateKeys()
    else:
        print("Invalid option")
        exit()


if __name__ == "__main__":
    main()
