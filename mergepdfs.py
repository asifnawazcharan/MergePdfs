# merge pdfs

from PyPDF2 import PdfMerger
import os

def merge_pdfs(input_folder, output_file):
    merger = PdfMerger()

    # Get a list of PDF files in the input folder
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]

    # Sort the PDF files in alphabetical order
    pdf_files.sort()

    # Merge the PDF files
    for pdf_file in pdf_files:
        file_path = os.path.join(input_folder, pdf_file)
        merger.append(file_path)

    # Write the merged PDF to the output file
    merger.write(output_file)
    merger.close()

    print(f"PDF files merged successfully. Output file: {output_file}")

def main():
    input_folder = "pdfstomerge"  # Specify the input folder containing PDF files
    output_file = "pdfstomerge/merged.pdf"  # Specify the output file path

    merge_pdfs(input_folder, output_file)

if __name__ == "__main__":
    main()
