import PyPDF2
pdf=open("hello.pdf",'rb')
pdfreader=PyPDF2.PdfReader(pdf)
page=pdfreader.pages
for i in page:
    print(i.extract_text())
pdf.close()
