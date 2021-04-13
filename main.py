from scrapSlides import scrap_slides
from cleanSlide import clean_slides
from slidesToPdf import slides_to_pdf


url_slides_bbb = "https://bbb1.centrale-marseille.fr/bigbluebutton/presentation/72a40bfaabf993f8314ef45ca5ba0d053dcacfd7-1618301407645/72a40bfaabf993f8314ef45ca5ba0d053dcacfd7-1618301407645/03e419217621df6af41303f9504397b2d0e44eb0-1618306059443/svg/"

scrap_slides(url_slides_bbb)
clean_slides()
slides_to_pdf()

