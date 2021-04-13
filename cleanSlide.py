import lxml.etree as etree

# Sources :
# Parse svg files : https://stackoverflow.com/questions/40469870/python-lxml-parsing-svg-file
# Remove element in lxml : https://stackoverflow.com/questions/7981840/how-to-remove-an-element-in-lxml


def clean_slides(temp_path):
    nb_max = 100

    for i in range(1, nb_max):
        try:
            xml = etree.parse(temp_path + "/slides/slide" + str(i) + ".svg")
            svg = xml.getroot()
            for j in range(1, 16):  # Remove small icons at the bottom of the svg file
                current_element = svg.findall(".//{http://www.w3.org/2000/svg}path")[-1]
                current_element.getparent().remove(current_element)
                print(current_element.attrib)

            with open(temp_path + "/slides/slide" + str(i) +".svg", 'wb') as f:
                f.write(etree.tostring(svg))
        except:
            print(f"Ah, c'était la dernière slide ({i-1})")
            break



