# -*- coding: utf-8 -*-
"""
threeway_preprocess.py
[Can be run either standalone or as a module!]

@author: methylDragon

                                   .     .
                                .  |\-^-/|  .
                               /| } O.=.O { |\
                              /´ \ \_ ~ _/ / `\
                            /´ |  \-/ ~ \-/  | `\
                            |   |  /\\ //\  |   |
                             \|\|\/-""-""-\/|/|/
                                     ______/ /
                                     '------'
                       _   _        _  ___
             _ __  ___| |_| |_ _  _| ||   \ _ _ __ _ __ _ ___ _ _
            | '  \/ -_)  _| ' \ || | || |) | '_/ _` / _` / _ \ ' \
            |_|_|_\___|\__|_||_\_, |_||___/|_| \__,_\__, \___/_||_|
                               |__/                 |___/
            -------------------------------------------------------
                           github.com/methylDragon

(This is a generator function! Just keep calling it to process the next image!)

Description:
Takes in input images and yields square images, processed three different ways.

It's an iterator! So call it with iter() and next()
to process arbitrarily large image lists!

This script uses OpenCV to preprocess images for image recognition tasks
using Tensorflow! The order it preprocesses and outputs input images can
be random to cater for minibatch training.

It'll return square images processed in these three ways,
within each iteration, in this order:

    - Square black border padded
    - Centre cropped
    - Stretched (naive resized)

Functions:

Preprocessing functions
- centre_crop(img, height, width)
- square_pad(img, height, width):

Threeway Preprocessing function
- preprocess(folders, extensions = None,
               randomise = True,
               greyscale = False,
               output_height = 299, output_width = 299,
               canny = False):

Note:
Ensure your parent folders are placed in the same folder as your script

Structure your files and folder as such:
    Root directory:
        - your_script.py
        - Parent Folder
            - Label Subfolder
            - Label Subfolder
            - Label Subfolder
"""

import cv2
import glob

import os

import random

# =============================================================================
# SET PARAMETERS
# =============================================================================

# Check if this is run as a module
if __name__ == "__main__":

    # If it is, HELLO! Input your folder names here!
    folders = ["Training\*"]

    extensions = [# TIFFs
                  "tif", "tiff",

                  # GIFs
                  "gif",

                  # JPGs
                  "jpeg", "jpg", "jif", "jfif", "jp2", "jpx", "j2k", "j2c",

                  # Flashpix
                  "fpx",

                  # ImagePac
                  "pcd",

                  # PNG
                  "png",

                  # PDFs
                  "pdf"]

# =============================================================================
# USEFUL FUNCTIONS
# =============================================================================

def centre_crop(img, height, width):
    """
    Returns a centre-cropped square image

    Parameters
    ----------
    - img : numpy.ndarray (eg. from cv2.imread)
        Source image
    - height : int
        Source image height
    - width : int
        Source image width

    Returns
    -------
    - roi : numpy.ndarray
        Image that is centre-cropped
    """
    if height == width:

        top = 0
        bottom = height

        left = 0
        right = width

    elif height > width:

        y_tolerance = width // 2
        y_midpoint = height // 2

        top = y_midpoint - y_tolerance
        bottom = y_midpoint + y_tolerance

        left = 0
        right = width

    elif height < width:

        x_tolerance = height // 2
        x_midpoint = width // 2

        top = 0
        bottom = height

        left = x_midpoint - x_tolerance
        right = x_midpoint + x_tolerance

    roi = img[top:bottom, left:right]

    return roi

def square_pad(img, height, width):
    """
    Returns a border-padded square image

    Parameters
    ----------
    - img : numpy.ndarray(eg. from cv2.imread)
        Source image

    - height : int
        Source image height

    - width : int
        Source image width

    Returns
    -------
    - roi : numpy.ndarray
        Image that is border-padded
    """
    if height == width:

        top, bottom = 0, 0
        left, right = 0, 0

    elif height > width:

        border_width = (height - width) // 2

        top, bottom = 0, 0
        left, right = border_width, border_width

    elif height < width:

        border_width = (width - height) // 2

        top, bottom = border_width, border_width
        left, right = 0, 0

    roi = cv2.copyMakeBorder(img,
                              top, bottom,
                              left, right,
                              cv2.BORDER_CONSTANT)

    return roi

# =============================================================================
# PREPROCESSING FUNCTION
# =============================================================================

# Folders is a LIST OF FOLDERS
def preprocess(folders, extensions = None,
               randomise = True,
               greyscale = False,
               output_height = 299, output_width = 299,
               canny = False):
    """
    Takes in input images and yields square images, processed three different ways.

    preprocess(folders [, extensions = None,
               randomise = True,
               greyscale = False,
               output_height = 299, output_width = 299,
               canny = False])

    The function is an iterator function! So call it with iter() and next()
    to process arbitrarily large image lists!

    This script uses OpenCV to preprocess images for image recognition tasks
    using Tensorflow! The order it preprocesses and outputs input images can
    be random to cater for minibatch training.

    It'll return square images processed in these three ways,
    within each iteration, in this order:

        - Square black border padded
        - Centre cropped
        - Stretched (naive resized)

    Parameters
    ----------
    - folders : list of str
        List of folder names
        (eg. sub-folders specified as "Parent/Sub/Sub")

    - extensions : list of str, optional
    List of extensions
    (eg. "tif", "tiff", "png")

    - randomise : bool, optional
        If True, turn on randomisation for minibatch training

    - greyscale : bool, optional
        If True, set output images to greyscale (1 channel)

    - output_height : int, optional
        Height of the outputted images

    - output_width : int, optional
        Width of the outputted images

    - canny : bool, optional
        Utilise Canny image processing

    Yields
    ------
    - square_pad_img : numpy.ndarray
        The image preprocessed via border-padding

    - centre_crop_img : numpy.ndarray
        The image preprocessed via centre-cropping

    - stretch_resized_img : numpy.ndarray
        The image preprocessed via stretch resizing

    - label : str
        The folder name the image came from (usually the label)

    Note
    ----
    Ensure your parent folders are placed in the same folder as your script

    Structure your files and folder as such:
        Root directory:
            - your_script.py
            - Parent Folder
                - Label Subfolder
                - Label Subfolder
                - Label Subfolder
    """

    if extensions == None:
        extensions = [# TIFFs
                      "tif", "tiff",

                      # GIFs
                      "gif",

                      # JPGs
                      "jpeg", "jpg", "jif", "jfif", "jp2", "jpx", "j2k", "j2c",

                      # Flashpix
                      "fpx",

                      # ImagePac
                      "pcd",

                      # PNG
                      "png",

                      # PDFs
                      "pdf"]

    # Generate paths list
    paths = [os.path.join(os.path.abspath(""), folder) for folder in folders]

    file_list = []

    # Create a list of input file paths for all images
    for path in paths:
        for extension in extensions:
            file_list.extend([file for file in glob.iglob(str(path) + "\*." + str(extension))])

    # If the randomise flag is activated, shuffle the list
    if randomise == True:
        random.shuffle(file_list)

    # Iteratively run through the list for the current folder
    for file in file_list:
        try:
            if greyscale == True:
                # Read the file as a greyscale image
                image = cv2.imread(file, 0)
            else:
                # Read the file as colour image
                image = cv2.imread(file, 1)

            # Try to read the height and width (and channel if possible!)
            try:
                i_height, i_width = image.shape
            except:
                i_height, i_width, i_channels = image.shape

            # Create the pre-processed image versions
            centre_crop_img = centre_crop(image, i_height, i_width)
            square_pad_img = square_pad(image, i_height, i_width)

            # Resize te pre-processed image versions
            square_pad_img = cv2.resize(square_pad_img, (output_height, output_width))
            centre_crop_img = cv2.resize(centre_crop_img, (output_height, output_width))
            stretch_resized_img = cv2.resize(image, (output_height, output_width))

            # Optional canny preprocess
            if canny == True:
                min_thresh = 38
                max_thresh = 53
                square_pad_img = cv2.Canny(square_pad_img, min_thresh, max_thresh)
                centre_crop_img = cv2.Canny(centre_crop_img, min_thresh, max_thresh)
                stretch_resized_img = cv2.Canny(stretch_resized_img, min_thresh, max_thresh)

            try:
                # Output the current iteration's images
                yield square_pad_img, centre_crop_img, stretch_resized_img, file.split("\\")[-2]

            # Ignore the GeneratorExit exception
            # Close the generator when done
            except GeneratorExit:
                print("\nCleaning up generator")
                return

        except:
            print("ERROR! SKIPPING IMAGE")
            continue

    # Close when done
    return

# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":

    preprocessor = preprocess(folders, extensions, True)

    for _ in range(1000):
        images = next(preprocessor)
        pad = images[0]
        crop = images[1]
        stretch = images[2]

        print(images[3])

        cv2.imshow("pad", pad)
        cv2.imshow("crop", crop)
        cv2.imshow("stretch", stretch)

        ch = cv2.waitKey(100)
    
    cv2.destroyAllWindows()
