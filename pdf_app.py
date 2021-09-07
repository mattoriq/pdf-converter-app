from pdf2image import convert_from_path
import cv2
import time
from PyPDF2 import PdfFileMerger
import img2pdf
from PIL import Image

try:
	while(True):
		print("1. Pdf to images\n2. Merge multiple pdf\n3. Image to Pdf\n4. Exit")
		ch = input("What do: ")
		
		if(ch == '1'):
			filename = input('FILENAME: ')
			images = convert_from_path(filename)
			i = 0
			newFilename = filename.replace(".pdf","")
			for img in images: 
				img.save(newFilename+str(i)+'.jpg', 'JPEG')
				i += 1
			print('DONE. CHECK UR FOLDER.\n')

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
			print('DONE. CHECK UR FOLDER.\n')

		elif(ch == '3'):
			filename = input('FILENAME: ')
			if ".png" in filename:
				myFile = filename.replace(".png","")
			elif ".jpg" in filename:
				myFile = filename.replace(".jpg","")
			pdf_path = myFile + ".pdf"
			image = Image.open(filename)
			pdf_bytes = img2pdf.convert(image.filename)
			file = open(pdf_path, "wb")
			file.write(pdf_bytes)
			image.close()
			file.close()
			print('DONE. CHECK UR FOLDER.\n')

		elif(ch == "4"):
			print("exiting.........................")
			break

		else:
			print('WRONG INPUT')
except Exception as e:
	raise e
	print(e)
	time.sleep(5)


time.sleep(3)
