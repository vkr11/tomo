import subprocess
import sys
import os

def pdf_to_text(pdf_path, output_path=None):
    if not os.path.exists(pdf_path):
        print(f"Error: File {pdf_path} not found.")
        return

    if output_path is None:
        output_path = pdf_path.replace(".pdf", ".txt")
    
    try:
        subprocess.run(["pdftotext", pdf_path, output_path], check=True)
        print(f"Successfully converted {pdf_path} to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("Error: pdftotext command not found. Please install poppler.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_txt.py <input_pdf> [output_txt]")
        sys.exit(1)
    
    pdf_in = sys.argv[1]
    txt_out = sys.argv[2] if len(sys.argv) > 2 else None
    pdf_to_text(pdf_in, txt_out)
