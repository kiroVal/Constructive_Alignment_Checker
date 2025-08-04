# First Step is to install easyocr
!pip install easyocr

# Second is to install the libraries
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

# Step 3 find the path for the image to be used in extracting 
# Replace 'Test' to your relative image path
TEST = 'sample.png'
#TEST = 'sample.jpeg'

# Step 4 install the reader for the easyocr as well as the languages
# Step 5 run the code below to start processing the images
reader = easyocr.Reader(['en'])
result = reader.readtext(TEST)
result

