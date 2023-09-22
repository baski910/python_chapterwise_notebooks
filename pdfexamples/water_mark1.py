import PyPDF2

pdf_file = "doc.pdf"
watermark = "watermark.pdf"
merged_file = "merged.pdf"

input_file = open(pdf_file,'rb')
input_pdf = PyPDF2.PdfReader(pdf_file)
watermark_file = open(watermark,'rb')
watermark_pdf = PyPDF2.PdfReader(watermark_file)

pdf_page = input_pdf.pages[0]
watermark_page = watermark_pdf.pages[0]

pdf_page.merge_page(watermark_page)

output = PyPDF2.PdfWriter()
output.add_page(pdf_page)

merged_file = open(merged_file,'wb')
output.write(merged_file)

merged_file.close()
watermark_file.close()
input_file.close()
