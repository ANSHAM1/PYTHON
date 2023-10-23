import PyPDF2

pdfs=['hello.pdf','Nice.pdf']
output='output.pdf'

pdfmerger=PyPDF2.PdfMerger()
for pdf in pdfs:
    pdfmerger.append(pdf)
with open(output,'wb') as f:
    pdfmerger.write(f)





