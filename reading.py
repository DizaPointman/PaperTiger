from pathlib import Path
from pypdf import PdfReader, PdfWriter


#pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_pdfs" /"Pride_and_Prejudice.pdf")

pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_pdfs" /"antrag-sgb2_ba042689.pdf")

#pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger" /"blank.pdf")
    

pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter(pdf_path)

def pdf_extract_metadata():
    print("Printing Path")
    print(pdf_path)    
    print("Printing Pages")
    print(pdf_reader.pages)
    print("Printing Metadata as a whole")
    print(pdf_reader.metadata)
    print("Printing extracted Metadata")
    
    for x in pdf_reader.metadata:
        # getting all the metadata
        print(f"{x[1:]}...: " + pdf_reader.metadata.get(f"{x}", ""))
        

def pdf_extract_data():
    for page in pdf_reader.pages[0:1]:
        print("-----new page-----")
        print(page.extract_text())

def save_to_txt():
    
    txt_file = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_output" /"test.txt")
    content = [
        f"{pdf_reader.metadata.title}",
        f"Number of pages: {len(pdf_reader.pages)}",            
        ]
    
    for page in pdf_reader.pages:
        content.append(page.extract_text())
        
    txt_file.write_text("\n".join(content))
    
def pdf_write_new():
    
    # width/height arguments required;Dimensions in user space units;One unit equals 1/72 inch;width=8.27 * 72, height=11.7 * 72 = A4
    blank_page = pdf_writer.add_blank_page(width=8.27 * 72, height=11.7 * 72)
    blank_page = pdf_writer.add_blank_page(width=8.27 * 72, height=11.7 * 72)
    pdf_writer.write("blank.pdf")
    
def extract_single_page_and_write_new_pdf():
    single_input_pdf = pdf_reader
    first_page = single_input_pdf.pages[0]
    single_output_pdf = pdf_writer
    
    # .add_page() adds a page to list of pages in the output_pdf object, but needs existing page
    # .add_blank_page() creates new blank page
    single_output_pdf.add_page(first_page)
    single_output_pdf.write("extract_first_page.pdf")
    
def extract_multiple_pages_and_write_new_pdf():
    input_pdf = pdf_reader
    output_pdf = pdf_writer
    
    for page in input_pdf.pages[1:4]:
        output_pdf.add_page(page)

    output_pdf.write("multiple_pages_extracted.pdf")
    
def appending_from_reader_to_writer():
    input_pdf = pdf_reader
    output_pdf = pdf_writer
    
    pdf_writer.append_pages_from_reader(input_pdf)
    output_pdf.write("appending_from_reader_to_writer.pdf")

def appending_pdfs():

if __name__ == '__main__':
    
    #pdf_extract_metadata()
    #pdf_extract_data()
    #save_to_txt()
    #pdf_write_new()
    #extract_single_page_and_write_new_pdf()
    #extract_multiple_pages_and_write_new_pdf()
    #appending_from_reader_to_writer()