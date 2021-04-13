from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfFileMerger


def slides_to_pdf(temp_path):
    for i in range(1, 31):
        try:
            #print(i)
            drawing = svg2rlg(f"{temp_path}/slides/slide{i}.svg")
            renderPDF.drawToFile(drawing, f"{temp_path}/files/file{i}.pdf")
        except Exception as e:
            #print(f"Slide {i} failed, error: ", e)
            print("")

    merger = PdfFileMerger()
    for i in range(1, 31):
        try:
            #print(i)
            merger.append(f"{temp_path}/files/file{i}.pdf")
        except Exception as e:
            #print(f"File {i} failed, error: ", e)
            print("")

    merger.write(f"{temp_path}/result.pdf")
    merger.close()
