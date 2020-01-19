#install pyDF2 (cmd command)
#pip install "PyPDF2"


# importing all the required modules
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader

# preparing for debugging
#import pdb; pdb.set_trace()

# variables
base_path = 'C:\\GitHub\\learning_python\\merge_pdfs\\'
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']
output_pdf = 'files123.pdf'

# creating a pdf merger object
merger = PdfFileMerger()

# appending
for pdf_file in pdf_files:
   # open file
   file = open(base_path+pdf_file, 'rb')
   # creating a pdf reader object
   fileReader = PyPDF2.PdfFileReader(file)
   # append
   merger.append(fileReader)

# creating output
merger.write(base_path+output_pdf)