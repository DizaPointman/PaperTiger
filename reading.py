from pathlib import Path
from pypdf import PdfReader


#pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_pdfs" /"Pride_and_Prejudice.pdf")

pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_pdfs" /"antrag-sgb2_ba042689.pdf")
    

pdf_reader = PdfReader(pdf_path)

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

if __name__ == '__main__':
    
    #pdf_extract_metadata()
    #pdf_extract_data()
    save_to_txt()