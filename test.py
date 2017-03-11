__author__ = '4b_skladany_f'


import xml.etree.ElementTree as ET
import xml.dom.minidom
from xml.dom.minidom import parseString

def compact_xml(msg):
    return msg.replace('\n', '').replace('\t', '').replace('> <', "><").replace('?><','?>\n<')

def nice_xml(msg):
    return parseString(compact_xml(msg)).toprettyxml(indent='    ')

def prettify(elem):
    rough_string = ET.tostring(elem, "utf-8")
    reparsed = parseString(rough_string)
    pretty = nice_xml(reparsed.toprettyxml(indent='    '))
    return pretty


html = ET.Element("html", attrib={"xmlns":"http://w3.org/1999/xhtml"})


title = ET.SubElement(html, "h1")
title.value = "The Python Python Table Table"
par = ET.SubElement(html, "p", attrib={"align":"justify"})
par.value = "paragraf, ne?"

#table = ET.SubElement(html, "table", attrib={"id":"t01",
 #                                            "cellspacing":"0"})

tds = []
#for i in range(10):
  #  tds.append(ET.SubElement(table, "tr", attrib={"style":'border:solid 1px #000000', "bgcolor": "#fff" if i%2 else "#ddd"}))

#for td in tds:
#    for i in range(6):
#        a = ET.SubElement(td, "th", attrib={"colspan":"2","style":'border:solid 1px #000000'})
#        a.text = "Hello %d  " %i





#table = ET.SubElement(html, "table")
print(prettify(html))



with open("test.html", mode="w", encoding="utf8") as fw:
    fw.write(prettify(html))