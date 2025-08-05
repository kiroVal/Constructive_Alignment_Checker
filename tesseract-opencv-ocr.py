# Install pytesseract opencv
%pip install pytesseract opencv-python PyMuPDF

# Load the PDF document and convert each page into an image format suitable for image processing.
import fitz
import numpy as np
import os

# Define the path to the PDF file you want to process.
# Replace 'your_document.pdf' with the actual path to your PDF file.
# For demonstration purposes, we will check if a placeholder exists or note the requirement.
pdf_path = "full_filename_path" # This needs to be a valid path to a PDF file

images = []

try:
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The PDF file was not found at: {sample_data}")

    doc = fitz.open(pdf_path)
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        # Render page to an image (pixmap) with a higher DPI for better quality
        # Setting dpi to 300 for better OCR results
        pix = page.get_pixmap(dpi=300)
        # Convert pixmap to a NumPy array
        img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
        # If the image is grayscale or has an alpha channel, convert to BGR for OpenCV compatibility
        if img_array.shape[-1] == 1: # Grayscale
             img_array = np.squeeze(img_array, axis=-1) # Remove the single channel dimension
             img_array = np.stack((img_array,) * 3, axis=-1) # Convert to BGR
        elif img_array.shape[-1] == 4: # RGBA
             img_array = img_array[..., :3] # Drop the alpha channel
             img_array = img_array[..., ::-1] # Convert RGB to BGR

        images.append(img_array)
    doc.close()
    print(f"Successfully processed {len(images)} pages.")

except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
    print("Please make sure the 'pdf_path' variable points to a valid PDF file.")
except Exception as e:
    print(f"An unexpected error occurred during PDF processing: {e}")


# Iterate through the images, apply grayscale conversion, adaptive thresholding, 
# and morphological operations to enhance text, then store the processed images.
# Check if images list is not empty from the previous step
if 'images' in locals() and images:
    for img_array in images:
        # Convert to grayscale
        gray_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding
        # Using ADAPTIVE_THRESH_GAUSSIAN_C and THRESH_BINARY_INV for better results on text
        # blockSize: Size of a pixel neighborhood that is used to calculate a threshold value
        # C: Constant subtracted from the mean or weighted mean
        binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 11, 2)

        # Apply morphological operations
        # Create a kernel for morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

        # Apply opening to remove small noise
        processed_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

        processed_images.append(processed_image)

    print(f"Successfully processed {len(processed_images)} images.")
else:
    print("The 'images' list is empty or not found. Please ensure previous steps were successful.")


processed_images = [] 

# Use Tesseract to perform Optical Character Recognition on the processed images and extract the text.
import pytesseract

extracted_text = []

# Iterate through the processed images, extract text using pytesseract, and store it in the list.
# Check if processed_images list is not empty
if 'processed_images' in locals() and processed_images:
    for i, processed_image in enumerate(processed_images):
        # Use pytesseract to extract text from the processed image
        text = pytesseract.image_to_string(processed_image)
        extracted_text.append(text)
        print(f"Extracted text from image {i+1}/{len(processed_images)}")

    # Optionally print the collected text for verification
    # for i, text in enumerate(extracted_text):
    #     print(f"--- Text from Image {i+1} ---")
    #     print(text)
    #     print("-" * 20)

else:
    print("The 'processed_images' list is empty or not found. Please ensure previous steps were successful.")

# Collect the extracted text from all pages and present it in a readable format.
# 1. Iterate through the extracted_text list and print content per page
for i, text in enumerate(extracted_text):
    print(f"--- Text from Page {i+1} ---")
    print(text)
    print("-" * 30) # Use a clearer separator

# 2. Join the text from all pages into a single string
combined_text = "\n".join(extracted_text)

# 3. Print the combined text
print("\n--- Combined Text from All Pages ---")
print(combined_text)
print("-" * 30)
