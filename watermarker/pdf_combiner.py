"""
learn basic of  handleing pdf with python
you need install PyPDF2

given pdf files  combine them  to one big pdf file
input: dummy.pdf twopage.pdf wtr.pdf
output  : combine_pdf.pdf

run program  :
 *from command line : ./pdf_combiner.py dummy.pdf twopage.pdf wtr.pdf
 or
*using pycharm :
for runing program with arguments
- goto  Run
- edit configuration
- set argument in the parameters field  : in this case write there dummy.pdf twopage.pdf wtr.pdf ( with white space)
- click Run
"""
print(__doc__)

"""
exercise2:
given pdf files  combine them  to one big pdf file
input: pdf_files/dummy.pdf pdf_files/twopage.pdf pdf_files/wtr.pdf 
output  : combine_pdf.pdf

"""
import PyPDF2
import sys

inputs= sys.argv[1:] # list of all given arguments

def pdf_combiner_func(pdf_list):
    merger=PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        # print (pdf) # print all argument (pdf  file )
        merger.append(pdf)
    with open('pdf_files/output/combined_fle/combine_pdf.pdf', 'wb') as new_file:
        merger.write(new_file)
    # merger.write('combine_pdf.pdf')



pdf_combiner_func(inputs)
# print num of pages in the combine_pdf
# with open ('combine_pdf.pdf','rb')as file: # mode read binary - create binary mode object
#     # print(file)
#     reader=PyPDF2.PdfFileReader(file)
#     print(reader.numPages)