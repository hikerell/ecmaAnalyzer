# utf8

import os, sys
from html.parser import HTMLParser

class ECMAException(Exception):
    pass
        
class ECMAHTMLParser(HTMLParser):
    """docstring for ECMAHTMLParser"""
    def __init__(self):
        super(ECMAHTMLParser, self).__init__()
        self.state = 'END_GRAMMER_TAG'

    def handle_starttag(self, tag, attrs):
        if tag!='emu-grammar':
            return
        
        #print(tag, attrs)
        if len(attrs)!=1:
            return
        assert(attrs[0][0] == 'type')
        if attrs[0][1]!='definition':
            return

        self.state = 'START_GRAMMER_TAG'
        #print('</%s %s>' % (tag, str(attrs)))

    def handle_endtag(self, tag):
        if tag!='emu-grammar':
            return
        self.state = 'END_GRAMMER_TAG'
        #print('</%s>' %tag)

    def handle_data(self, data):
        #print(self.state)
        if self.state != 'START_GRAMMER_TAG':
            return
        #print("Encountered some data  :", data)
        print(data)

def parse(data):
    parser = ECMAHTMLParser()
    parser.feed(data)

usage = """
USAGE:
    python3 ecma_spec_parser.py <ecma-spec-file>
"""

if __name__=='__main__':
    if len(sys.argv)!=2:
        print(usage)
        sys.exit(1)
    file = sys.argv[1]
    if not os.path.exists(file) or not os.path.isfile(file):
        print(f'ecma-spec-file {file} not exist or not a file')
        print(usage)
        sys.exit(1)
    with open(file, 'rb') as fr:
        data = fr.read()
        data = data.decode()
        parse(data)
