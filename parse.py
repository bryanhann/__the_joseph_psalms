import os
import sys
import xml
import xml.sax
import xml.etree.ElementTree as ET
#print( sys.argv )
#exit()
START="""<div class="book bkPSA">"""

STOP="""</div></div></div><div class="version-copyright" """


def handle_file(fname):
    base=os.path.basename(fname)
    with open(fname) as fd:
        txt=fd.read()
    ii = txt.find(START)
    jj = txt.find(STOP)#-18
    if ii < 0:
        return
    assert ii <= jj
    out=txt[ii:jj]
    root=ET.fromstring(out)
    for el in root.iter():
        prefix = str(el.attrib).rjust(20)
        text = el.text
        if text is not None:
            text = text.strip()
        if text and el.attrib['class'] == 'content':
            print(text)


handle_file( sys.argv[1] )

