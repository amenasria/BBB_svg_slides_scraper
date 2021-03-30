import lxml.etree as etree

# Sources :
# Parse svg files : https://stackoverflow.com/questions/40469870/python-lxml-parsing-svg-file
# Remove element in lxml : https://stackoverflow.com/questions/7981840/how-to-remove-an-element-in-lxml

nb_max = 100

for i in range(1, nb_max):
    try:
        xml = etree.parse("slides/slide" + str(i) + ".svg")
        svg = xml.getroot()
        print(len(svg.findall(".//{http://www.w3.org/2000/svg}path")))
        # for current_element in svg.findall(".//{http://www.w3.org/2000/svg}path"):
        #     # print(current_element.attrib)
        #     if 'transform' in current_element.attrib:
        #         current_element.getparent().remove(current_element)
        #         # print("allez ciao")
        #     if current_element.attrib.get('style') == " stroke:none;fill-rule:nonzero;fill:rgb(83.921814%,83.921814%,94.117737%);fill-opacity:1;":
        #         current_element.getparent().remove(current_element)
                # print("allez ciao")
        # print(etree.tostring(svg))
        # print(len(svg.findall(".//{http://www.w3.org/2000/svg}path")))
        # print(svg.findall(".//{http://www.w3.org/2000/svg}path")[-6])
        for j in range(1, 16):
            current_element = svg.findall(".//{http://www.w3.org/2000/svg}path")[-1]
            current_element.getparent().remove(current_element)
            print(current_element.attrib)

        # for current_element in svg.findall(".//{http://www.w3.org/2000/svg}path")[-5]:
        #     print(current_element)
        #     current_element.getparent().remove(current_element)

        with open("slides/cleanslide" + str(i) +".svg", 'wb') as f:
            f.write(etree.tostring(svg))
    except:
        print(f"Ah, c'était la dernière slide ({i-1})")
        break



