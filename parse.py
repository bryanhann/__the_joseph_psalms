import os
import sys
import xml.etree.ElementTree as ET

START="""<div class="book bk"""
STOP="""</div></div></div><div class="version-copyright" """

if __name__=='__main__':
    with open(sys.argv[1]) as fd:
        raw=fd.read()
    ii = raw.find(START)
    jj = raw.find(STOP)
    assert 0 < ii < jj
    root=ET.fromstring(raw[ii:jj])
    acc = [ el.text for el in root.iter() if el.attrib['class'] == 'content' ]
    acc = filter(None,acc)
    print( ''.join(acc) )
