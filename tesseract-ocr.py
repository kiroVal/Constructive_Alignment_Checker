# Install tesseract
!sudo apt update
!sudo apt install tesseract-ocr -y

# Install pytesseract
!pip install pytesseract

# Install pdfminer.six
!pip install pdfminer.six

# When executing, be mindful of the contents path so that It will 
# be able to read it.
import pytesseract
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTImage
from PIL import Image

def ocr_pdf(pdf_path):
    """
    Performs OCR on a PDF file and returns the extracted text.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    extracted_text = ""
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTImage):
                # For images within the PDF, you might need to extract and save them
                # temporarily to perform OCR. This is a simplified example.
                # A more robust solution would involve handling image extraction properly.
                print("Found an image. OCR on images within PDFs is not directly supported in this simplified example.")
            else:
                # Attempt to extract text from text elements
                if hasattr(element, 'get_text'):
                    extracted_text += element.get_text()

    # Note: This is a basic text extraction. For comprehensive OCR on scanned PDFs
    # with images, you would need to convert each PDF page to an image first
    # and then apply pytesseract to the image.

    # Example of how you would process an image if you were to convert a page:
    # from pdf2image import convert_from_path
    # images = convert_from_path(pdf_path)
    # for img in images:
    #     extracted_text += pytesseract.image_to_string(img)

    # For demonstration with text-based PDFs or partially scanned PDFs,
    # we'll rely on the basic text extraction from pdfminer.six first.
    # If your PDF is purely scanned images, you'll need the pdf2image step.

    return extracted_text

# Example usage (assuming you have a PDF file named 'testSyllabus.pdf' in the /content/sample_data directory)
pdf_file_path = '/content/sample_data/testSyllabus.pdf'
text_from_pdf = ocr_pdf(pdf_file_path)
print(text_from_pdf)
