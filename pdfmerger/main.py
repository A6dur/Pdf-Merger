from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs =[]
n = int(input("Enter how many files you want to merge : \n"))

for i in range (0 , n):
    name = input( f"Enter the name of pdf {i+1} :")
    pdfs.append(name)

for pdf in pdfs : 
    merger.append(pdf) 

merger.write("merged-pdf.pdf")
merger.close()