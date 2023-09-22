import PyPDF2

# create file object for pdf file
pdfObj = open('example.pdf',"rb")

# create pdf reader object
pdfReader = PyPDF2.PdfReader(pdfObj)

print(len(pdfReader.pages))

pageObj = pdfReader.pages[0]

print(pageObj.extract_text())
