import PyPDF2
from pathlib import Path

separateur = "+-" * 13

print("Veuillez mettre les fichier pdf à concaténer dans le dissier pdf ")

print(separateur)

nom_fichier1 = input("Le nom du premier fichier : ")
nom_fichier2 = input("Le nom du deuxieme fichier : ")

nom_fichier3 = input("Le nom du troisième fichier : ")

fichier1 = Path.cwd() / nom_fichier1
fichier2 = Path.cwd() / nom_fichier2
fichier3 = Path.cwd() / nom_fichier3

f1 = open(fichier1, 'rb')
f2 = open(fichier2, 'rb')
f3 = open(fichier3, 'rb')

pdf1 = PyPDF2.PdfFileReader(f1)
pdf2 = PyPDF2.PdfFileReader(f2)
pdf3 = PyPDF2.PdfFileReader(f3)

pdf1_pages = pdf1.getNumPages()
pdf2_pages = pdf2.getNumPages()
pdf3_pages = pdf3.getNumPages()



output_file = open('new_doc.pdf', 'wb')
writer = PyPDF2.PdfFileWriter()

for i in range(pdf1_pages):
	writer.addPage(pdf1.getPage(i))
	
for j in range(pdf2_pages):
	writer.addPage(pdf2.getPage(j))
	
for k in range(pdf3_pages):
	writer.addPage(pdf3.getPage(k))
	
writer.write(output_file)

print(f"Votre nouveau fichier s'appelle new_doc.pdf")

f1.close()
f2.close()
output_file.close()

