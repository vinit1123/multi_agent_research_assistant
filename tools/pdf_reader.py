from pypdf import PdfReader
import os


def pdf_reader_tool(file_path):

    if not os.path.exists(file_path):

        return f"PDF not found: {file_path}"

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text