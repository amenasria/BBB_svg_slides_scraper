from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfFileMerger


def slides_to_pdf(temp_path):
    i, j = 1, 1
    while True:
        try:
            #print(i)
            drawing = svg2rlg(f"{temp_path}/slides/slide{i}.svg")
            renderPDF.drawToFile(drawing, f"{temp_path}/files/file{i}.pdf")
            i += 1
        except Exception as e:
            #print(f"Slide {i} failed, error: ", e)
            print("")
            break

    merger = PdfFileMerger()
    while True:
        try:
            #print(i)
            merger.append(f"{temp_path}/files/file{j}.pdf")
            j += 1
        except Exception as e:
            #print(f"File {i} failed, error: ", e)
            print("")
            break

    merger.write(f"{temp_path}/result.pdf")
    merger.close()
