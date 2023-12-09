import PyPDF2

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    # Open the first PDF file
    with open(pdf1_path, 'rb') as pdf1_file:
        pdf_reader1 = PyPDF2.PdfReader(pdf1_file)
        pdf_writer.add_page(pdf_reader1.pages[0])  # Assuming you want to add all pages from the first PDF

    # Open the second PDF file
    with open(pdf2_path, 'rb') as pdf2_file:
        pdf_reader2 = PyPDF2.PdfReader(pdf2_file)
        for page_num in range(len(pdf_reader2.pages)):
            page = pdf_reader2.pages[page_num]
            pdf_writer.add_page(page)

    # Write the merged PDF to the output file
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    pdf1_path = "output1.pdf"  # Replace with your first PDF file path
    pdf2_path = "output.pdf"  # Replace with your second PDF file path
    output_path = "final.pdf"  # Replace with your desired output file path

    merge_pdfs(pdf1_path, pdf2_path, output_path)

    print("PDFs merged successfully.")
