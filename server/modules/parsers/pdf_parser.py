import PyPDF2
import os
from modules.parsers.IParser import IParser

class PdfParser(IParser):
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def parse(self):
        text = ""
        try:
            with open(self.pdf_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                # Iterate through all the pages in the PDF
                for page_number in range(len(pdf_reader.pages)):
                    # Extract text from each page
                    page = pdf_reader.pages[page_number]
                    text += page.extract_text()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        lines = text.splitlines()
        cleaned_text = ' '.join(lines)
        return cleaned_text