from pathlib import Path
from pypdf import PdfReader


pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_pdfs"
            /"Pride_and_Prejudice.pdf")

def print_path():
    print(pdf_path)

pdf_reader = PdfReader(pdf_path)

if __name__ == '__main__':
    print_path()
    print(len(pdf_reader.pages))