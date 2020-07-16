"""
learn basic of  handleing pdf with python
you need install PyPDF2

"""
print(__doc__)
import PyPDF2


"""
exercise1:
given pdf file rotate it in 90 degree and save it in a new pdf file
given pdf: dummy.pdf
result pdf : tilt.pdf
"""
with open ('pdf_files/dummy.pdf','rb')as file: # mode read binary - create binary mode object
    # print(file)
    reader=PyPDF2.PdfFileReader(file)
    # print(reader.numPages)
    page=reader.getPage(0)
    page.rotateCounterClockwise(90) # rotate the page
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('pdf_files/output/rotated_file/tilt.pdf','wb') as new_file:
        writer.write(new_file)



