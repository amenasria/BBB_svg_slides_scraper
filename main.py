from scrapSlides import scrap_slides
from cleanSlide import clean_slides
from slidesToPdf import slides_to_pdf
from prepare_architecture import prepare_architecture
from wipeSlidesDirContent import wipe_dir_content
import sys
import os

#url_slides_bbb = "https://bbb1.centrale-marseille.fr/bigbluebutton/presentation/72a40bfaabf993f8314ef45ca5ba0d053dcacfd7-1618301407645/72a40bfaabf993f8314ef45ca5ba0d053dcacfd7-1618301407645/03e419217621df6af41303f9504397b2d0e44eb0-1618306059443/svg/"
url_slides_bbb = sys.argv[1]
#print(sys.argv[1])
#print(os.path.abspath(os.getcwd()))

def main():
    temp_folder = prepare_architecture()
    #print("fini de creer les dossiers")
    if temp_folder[0]:
        scrap_slides(url_slides_bbb, temp_folder[1])
        #print("fini de scraper")
        clean_slides(temp_folder[1])
        #print("fini de cleaner")
        slides_to_pdf(temp_folder[1])
        #print("fini de pdfer")
        wipe_dir_content(temp_folder[1] + "/slides")
        wipe_dir_content(temp_folder[1] + "/files")
        #print("bien delete les fichier temporaires")
        print(temp_folder[1]+"/result.pdf")
    else:
        print("error")

main()
