import pypdf

pdf_path = "06-049-2 Django – Sticky Notes Application Part 2.pdf"
output_path = "06-049-2 Django – Sticky Notes Application Part 2 extracted.txt"

with open(pdf_path, 'rb') as file:
    reader = pypdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n---\n"

with open(output_path, 'w', encoding='utf-8') as outfile:
    outfile.write(text)

print(f"Extracted text saved to {output_path}")
