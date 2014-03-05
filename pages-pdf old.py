import os.path
import zipfile
from zipfile import *
import sys

file = raw_input('Enter the full path to the .pages file in question. Please note that file and directory names cannot contain any spaces.')
dir = os.path.abspath(os.path.join(file, os.pardir))
fileName, fileExtension = os.path.splitext(file)
if fileExtension == ".pages":
	os.chdir(dir)
	print (dir)
	fileExtension = ".zip"
	os.rename (file, fileName + ".zip")
	newName = fileName + ".zip"  #for debugging purposes
	print (newName) #for debugging purposes
	with ZipFile(newName, 'w') as ZF:
		print("I'm about to list names!")
		print(ZF.namelist()) #for debugging purposes
		ZF.extract("QuickLook/Preview.pdf")
	os.rename('Preview.pdf', fileName + '.pdf')
	finalPDF = fileName + ".pdf"
	print ("Check out the PDF! It's located at" + dir +  finalPDF + ".")
else:
	print ("Sorry, this is not a valid .pages file.")
	sys.exit
