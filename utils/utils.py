from pypdf import PdfReader
import re

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

def preprocess_text(text):
    """
    Preprocesses the input text by converting it to lowercase and removing extra spaces.

    Args:
        text (str): The input text to preprocess.
    Returns:
        str: The preprocessed text.
    """
    # Convert to lowercase
    text = text.lower()
    text = re.sub(r"<.*?>", "", text) # remove HTML tags
    text = re.sub(r"http\S+", "", text) # remove URLs
    text = re.sub(r"(?:\.\s*){2,}", " ", text)  # remove .... and . . .
    text = re.sub(r"[^a-z\s.,!?']", "", text) # keep only letters and basic punctuation
    text = re.sub(r"\s+", " ", text).strip() 
    # Remove extra spaces
    text = ' '.join(text.split())

    return text