# reading and editing pdf files
# pdf files are great for printing and reading, but not great for coding and parsing

import os, PyPDF2

#PyPDF2 will try, but it may not work as well as you want, and this is the best
# It cannot extract media, only text

# opening in read mode
pdf_file = open('meetingminutes1.pdf')

# we actually need to open in binary mode 'rb'
pdf_file = open('meetingminutes1.pdf', 'rb')

# passing file to PyPDF2, returns pdf reader file
reader = PyPDF2.PdfFileReader(pdf_file)

# it can return a number of pa
print(reader.numPages)

# loads individual page
page = reader.getPage(0)

# loads text and prints, note the text is not perfect
print(page.extractText()) 

# print text from all pages
for page_num in range(reader.numPages):
    print(reader.getPage(page_num).extractText())

# there's also a pdf writer, but it can't write arbitrary text due to how
# complex pdfs are. you can add, remove, and reorder pages, though, but you
# can't change the individual text, color font, layout, etc.

# open two existing files 
pdf_file_1 = open('meetingminutes1.pdf', 'rb')
pdf_file_2 = open('meetingminutes2.pdf', 'rb')

# creating reader objects
reader1 = PyPDF2.PdfFileReader(pdf_file_1)
reader2 = PyPDF2.PdfFileReader(pdf_file_2)

writer = PyPDF2.PdfFileWriter() #only exists in computer's memory

# adds all pages to pdf from pdf 1
for page_num in range(reader1.numPages):
    page = reader1.getPage(page_num)
    writer.addPage(page)

# adds all pages to pdf from pdf 2
for page_num in range(reader2.numPages):
    page = reader2.getPage(page_num)
    writer.addPage(page)

# opening and creating output file in "write binary" (wb) mode
output_file = open('CombinedMinutes.pdf', 'wb')

# call writer's write method passing it the output file name and closing
# all files
writer.write(output_file)

output_file.close()
pdf_file_1.close()
pdf_file_2.close()

