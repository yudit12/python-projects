"""
 add watermark for all pdf
 //mergePage - maarge in the same page not one page after another
"""
print(__doc__)
import PyPDF2

template= PyPDF2.PdfFileReader(open('pdf_files/super.pdf','rb'))
watermark=PyPDF2.PdfFileReader(open('pdf_files/wtr.pdf','rb'))
merger= PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page=template.getPage(i)
    page.mergePage(watermark.getPage(0))# watermark has only one page
    merger.addPage(page)


with open('pdf_files/output/watermarker_file/watermarked_file.pdf','wb') as  new_file:
        merger.write(new_file)