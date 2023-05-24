# Image Steganography using LSB algorithm
# Reference : https://cvnote.ddlee.cc/2019/09/12/psnr-ssim-python

import numpy as np
import cv2
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


def msg_to_bin(message):
    if type(message) == str:
        return ''.join([ format(ord(i), "08b") for i in message ])
    elif type(message) == bytes or type(message) == np.ndarray:
        return ''.join([ format(i, "08b") for i in message ])
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")

def bin_to_msg(binary):
    return bytes([int(binary[i], 2) for i in range(len(binary))])

# 08b adds formatting options for this variable
# 08 formats the number to eight digits zero-padded on the left
# b converts the number to its binary representation

def image_details(image):
    img = Image.open(image, "r")
    width, height = img.size
    return width, height
    

def lsb_encode(image, secret_message):
    width, height = image_details(image)
    image = cv2.imread(image)
    # determine the maximum bytes that can be stored in the image
    n_bytes = width * height * 3 // 8
    print("Maximum bytes to encode:", n_bytes)
    if len(secret_message) > n_bytes:
        raise ValueError("Error encountered insufficient bytes, need bigger image or less data !!")
    
    # secret_message += "#####"
    separator = "#####".encode('utf-8')  # Convert the separator to bytes
    secret_message += separator

    data_index = 0
    # add stopping criteria

    binary_secret_msg = msg_to_bin(secret_message)

    data_len = len(binary_secret_msg) # find the length of data that needs to be hidden
    for row in image:
        for rgb_pixel in row:
            # convert RGB values to binary format
            # r, g, b = msg_to_bin(rgb_pixel)
            r, g, b = rgb_pixel  # Extract the RGB values directly from the pixel
            # Convert each RGB value to binary
            r = msg_to_bin(r)
            g = msg_to_bin(g)
            b = msg_to_bin(b)
            # print(r, g, b)
            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # least significant red pixel bit
                rgb_pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant green pixel bit
                rgb_pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant blue pixel bit
                rgb_pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break
    return image

def lsb_decode(image):
    width, height = image_details(image)
    image = cv2.imread(image)
    binary_data = ""
    for row in image:
        for rgb_pixel in row:
            # r, g, b = msg_to_bin(rgb_pixel)
            r, g, b = rgb_pixel  # Extract the RGB values directly from the pixel
            # Convert each RGB value to binary
            r = msg_to_bin(r)
            g = msg_to_bin(g)
            b = msg_to_bin(b)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
    
    
    decoded_data = bin_to_msg(all_bytes)
    separator = bytes("#####", 'utf-8')
    if separator in decoded_data:
        decoded_data = decoded_data[:decoded_data.index(separator)]
    return decoded_data
