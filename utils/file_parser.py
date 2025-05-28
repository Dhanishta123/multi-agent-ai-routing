import json
from PyPDF2 import PdfReader

def detect_format(input_data):
    if isinstance(input_data, dict):
        return "JSON"
    elif isinstance(input_data, str):
        if input_data.endswith(".pdf"):
            return "PDF"
        elif input_data.endswith(".txt"):
            return "Email"
    return "Unknown"

def extract_text(file_path, file_format):
    if file_format == "PDF":
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            return " ".join([page.extract_text() for page in reader.pages])
    elif file_format == "Email":
        with open(file_path, "r") as f:
            return f.read()
    return ""