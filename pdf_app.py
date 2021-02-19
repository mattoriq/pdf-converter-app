from pdf2image import convert_from_path
import cv2
import time
from PyPDF2 import PdfFileMerger
from PIL import Image 
import img2pdf 
import os 

print("1. Pdf to images\n2. Merge multiple pdf\n3. Image to Pdf")
ch = input("What do: ")

if(ch == '1'):
	filename = input('FILENAME: ')
	images = convert_from_path(filename)
	i = 0
	for img in images: 
		img.save(filename+str(i)+'.jpg', 'JPEG')
		i += 1
	print('DONE. CHECK UR FOLDER.')
	time.sleep(5)

elif(ch == '2'):
	n = input('Banyak PDF: ')
	pdfs = []
	for i in range(int(n)):
		pdfName = input('Judul PDF '+str(i+1)+": ")
		pdfs.append(pdfName)
	merger = PdfFileMerger()
	for pdf in pdfs:
		merger.append(pdf)
	merger.write("result.pdf")
	merger.close()
	print('DONE. CHECK UR FOLDER.')
	time.sleep(5)

elif(ch == '3'):
	img_name = input('IMAGE NAME: ')
	image = Image.open(img_name) 
	pdf_bytes = img2pdf.convert(image.filename) 
	img_name = img_name.replace('.png','')
	img_name = img_name.replace('.jpg','')
	pdf_name = img_name+'.pdf'
	file = open(pdf_name, "wb") 
	file.write(pdf_bytes) 
	image.close() 
	file.close() 
	print("DONE. CHECK UR FOLDAR.") 
	time.sleep(5)

else:
	print('WROMGN INPUT. RETHINK UR LIFE')
	time.sleep(5)