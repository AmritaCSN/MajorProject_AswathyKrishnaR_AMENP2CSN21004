# Image Steganography using LSB algorithm
# Reference : https://cvnote.ddlee.cc/2019/09/12/psnr-ssim-python

import numpy as np
import cv2
from PIL import Image
import math
import time
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


def psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def mse(img1, img2):
    # Get the dimensions of the images
    rows, cols, channels = img1.shape
    # Compute the squared difference between the two images
    diff = (img1.astype(float) - img2.astype(float)) ** 2
    # Compute the mean squared error
    mse = np.sum(diff) / (rows * cols * channels)
    return mse


def cc_score(image1, image2):
    """
    Calculate the CC score between two RGB images.
    """
    # Compute the mean pixel value of each image
    mean1 = np.mean(image1)
    mean2 = np.mean(image2)
    # Compute the covariance between the images
    cov = np.sum((image1 - mean1) * (image2 - mean2)) / (image1.size - 1)
    # Compute the standard deviation of each image
    std1 = np.std(image1)
    std2 = np.std(image2)
    # Calculate the CC score
    cc = cov / (std1 * std2)

    return cc

def ssim(img1, img2):
    C1 = (0.01 * 255)**2
    C2 = (0.03 * 255)**2
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())
    mu1 = cv2.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(img2, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(img1**2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(img2**2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()


def calculate_ssim(img1, img2):
    if not img1.shape == img2.shape:
        raise ValueError('Input images must have the same dimensions.')
    if img1.ndim == 2:
        return ssim(img1, img2)
    elif img1.ndim == 3:
        if img1.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim(img1, img2))
            return np.array(ssims).mean()
        elif img1.shape[2] == 1:
            return ssim(np.squeeze(img1), np.squeeze(img2))
    else:
        raise ValueError('Wrong input image dimensions.')

def histogram_function(encoded_image, original_image):
    # reads an input image
    img1 = cv2.imread(encoded_image)
    img = cv2.imread(original_image)
    imgs = mpimg.imread(original_image)
    imgs1 = mpimg.imread(encoded_image)
    plt.subplot(221), plt.imshow(imgs) , plt.title("Original Image "), plt.axis('off')
    plt.subplot(222), plt.imshow(imgs1), plt.title("Encoded Image "), plt.axis('off')
    plt.subplot(223), plt.hist(img.ravel(),256,[0,256])
    plt.subplot(224), plt.hist(img1.ravel(),256,[0,256])
    plt.show()

def main():
    original_image_file = input("Enter the name of the original image file: ")
    encoded_image_file = input("Enter the name of the encoded image file: ")
    original_image = cv2.imread(original_image_file)
    encoded_image = cv2.imread(encoded_image_file)
    print("================================================")
    print(f"Original Image : {original_image.shape[:2]}")
    print(f"Encoded Image : {encoded_image.shape[:2]}")
    print("PSNR value:", psnr(original_image, encoded_image))
    print(f"SSIM : {calculate_ssim(original_image, encoded_image)}")
    print("MSE:",mse(original_image,encoded_image))
    cc = cc_score(original_image,encoded_image)
    print(f"CC score: {cc}")
    print("================================================")
    histogram_function(encoded_image_file,original_image_file)

if __name__ == "__main__":
    main()
