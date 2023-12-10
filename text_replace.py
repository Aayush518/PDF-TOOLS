import fitz  # PyMuPDF

def edit_pdf_text(input_path, output_path, replacements):
    pdf_document = fitz.open(input_path)

    for page_number, replacement_data in replacements.items():
        page = pdf_document[page_number - 1]  # Page numbers start from 1

        for old_text, new_text in replacement_data.items():
            text_instances = page.search_for(old_text)

            for inst in text_instances:
                rect = inst.rect
                page.add_freetext(rect, new_text, fontname=inst.fontname, fontsize=inst.fontsize, color=inst.color)

    pdf_document.save(output_path)
    pdf_document.close()

if __name__ == "__main__":
    input_pdf_path = "Lorem ipsum dolor sit amet.pdf"  # Replace with your input PDF file path
    output_pdf_path = "text_replaced.pdf"  # Replace with your output PDF file path

    # Specify the replacements as a dictionary where keys are page numbers
    # and values are dictionaries of old_text: new_text pairs
    replacements = {
        1: {
            "Reading": "Writing",
            # "Old Text 2": "New Text 2",
            # Add more replacements for page 1 as needed
        },
    }

    edit_pdf_text(input_pdf_path, output_pdf_path, replacements)


    print("Texts edited successfully.")
