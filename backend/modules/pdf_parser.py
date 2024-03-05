import PyPDF2
import os

class PdfParser:
    def __init__(self, pdf_path, file_name):
        self.pdf_path = os.path.join(pdf_path,file_name + '.pdf')

    def pdf_to_text(self):
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
        # Split the text into lines
        lines = text.splitlines()
        # Join the lines back together with spaces
        cleaned_text = ' '.join(lines)
        return cleaned_text