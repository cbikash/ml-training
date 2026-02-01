from pypdf import PdfReader

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.
    Returns:
        str: The extracted text from the PDF.
    """
    text = ""
    
    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    
    return text.strip()