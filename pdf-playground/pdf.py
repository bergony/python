import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


# pdf_combiner(inputs)

# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)


pdf_file = "super.pdf"
watermark = "wtr.pdf"
merged_file = "merged.pdf"

input_file = open(pdf_file, 'rb')
input_pdf = PyPDF2.PdfFileReader(input_file)

watermark_file = open(watermark, 'rb')
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
output = PyPDF2.PdfFileWriter()

for i in range(input_pdf.numPages):
    pdf_page = input_pdf.getPage(i)
    watermark_page = watermark_pdf.getPage(0)
    pdf_page.mergePage(watermark_page)
    output.addPage(pdf_page)

merged_file = open(merged_file, 'wb')
output.write(merged_file)

merged_file.close()
watermark_file.close()
input_file.close()
