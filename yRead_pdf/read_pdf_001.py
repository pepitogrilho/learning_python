#install pyDF2 (cmd command)
#pip install "PyPDF2"


# importing all the required modules
import PyPDF2

# preparing for debugging
#import pdb; pdb.set_trace()

# creating an object 
file = open('C:\\GitHub\\learning_python\\read_pdf\\GCCL79B.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

#
number_of_pages = fileReader.numPages

i=0
while i < number_of_pages:
   page = fileReader.getPage(i)
   page_content = page.extractText()
   print(page_content)
   i += 1