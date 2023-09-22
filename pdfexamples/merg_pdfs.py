import PyPDF2

def PDFmerge(pdfs, output):
    pdfMerger = PyPDF2.PdfMerger()

    for pdf in pdfs:
        with(open(pdf, "rb")) as f:
            pdfMerger.append(f)

    with(open(output, "wb")) as f:
        pdfMerger.write(f)

def main():
    pdfs = ['example.pdf', 'rotated_example.pdf']
    # output pdf file name
    output  = 'combined_example.pdf'
    
    # calling pdf merge function
    PDFmerge(pdfs = pdfs, output = output)

if __name__ == '__main__':
    main()
