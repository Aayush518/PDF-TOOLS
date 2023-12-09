import PyPDF2

def keep_selected_pages(input_pdf, output_pdf, selected_pages):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for i in range(len(pdf_reader.pages)):
            if i + 1 in selected_pages:
                page = pdf_reader.pages[i]
                pdf_writer.add_page(page)

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_path = "Tribhuvan_University_Project_Proposal_Template-2.pdf"  # Replace with your input PDF file path
    output_pdf_path = "/Users/aayushadhikari/Downloads/pdf/output1.pdf"  # Replace with your output PDF file path

    # Specify the page numbers you want to keep
    pages_to_keep = [1]  # Replace with your desired page numbers

    keep_selected_pages(input_pdf_path, output_pdf_path, pages_to_keep)

    print(f"Selected pages {pages_to_keep} kept successfully.")
