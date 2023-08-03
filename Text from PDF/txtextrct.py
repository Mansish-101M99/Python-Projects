# pip install PyPDF2
import PyPDF2

pdf_file = open("sample.pdf","rb")
rd_pdf = PyPDF2.PdfReader(pdf_file)
text = rd_pdf._get_page(0).extract_text()
print(text)