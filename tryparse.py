import os
import xml
import xml.etree.ElementTree as ET
DOWNLOAD='./__download__'
for fname in os.listdir( DOWNLOAD ):
    try:
        tree = ET.parse( DOWNLOAD + '/' + fname )
        print(fname, tree)
    except xml.etree.ElementTree.ParseError:
        print( fname, 'no' )
exit()
#tree = ET.parse('formatted.xml')
root = tree.getroot()
print( root.tag, root.attrib )
#print( dir(root) )
exit()
for xx in root.iter():
    tag = xx.tag
    attrib = xx.attrib
    if attrib[ 'class' ]=='content':
        print( xx.text  )
    continue
    inner = "%s\t%s" % (xx.tag, xx.attrib)
    #inner = (inner+' '*60)[:60]
    print( inner ,  xx.text.strip())
exit()
def loop(el):

    print(el.tag, el.attrib)
    for child in el:
        loop(el)
for child in root:
    print(child)
#print(dir(root))
exit()
import xml
print(xml)
from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("formatted.xml")
collection = DOMTree.documentElement
print(collection)
aa = collection.getElementsByTagName("content")
print(aa)
for xx in aa: print(xx)
#<div class="book bkPSA">
movies = collection.getElementsByTagName("movie")
