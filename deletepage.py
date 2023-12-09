import PyPDF2

def delete_page(input_pdf, output_pdf, page_number):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for i in range(len(pdf_reader.pages)):
            if i + 1 != page_number:
                page = pdf_reader.pages[i]
                pdf_writer.add_page(page)

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_path = "hello.pdf"  # Replace with your input PDF file path
    output_pdf_path = "output.pdf"  # Replace with your output PDF file path
    page_to_delete = 19  # Replace with the page number you want to delete

    delete_page(input_pdf_path, output_pdf_path, page_to_delete)

    print(f"Page {page_to_delete} deleted successfully.")
