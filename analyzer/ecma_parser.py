import os, sys
from html.parser import HTMLParser

STATE_SEARCHING = 0
STATE_PARSING   = 1

class ECMAException(Exception):
    pass

class ECMAHTMLParser(HTMLParser):
    """docstring for ECMAHTMLParser"""
    def __init__(self):
        super(ECMAHTMLParser, self).__init__()

        self.state = STATE_SEARCHING
        self.valid_tags = ['emu-production', 'emu-rhs']
        self.tag_stack = []
        self.production = None
        """
        {
            'name': '',
            'arguments': [],
            'rules': [],
                #expands = {
                    'type': 'node', #text
                    'value': 'xxx',
                    'constraints': [],
                    'params': [],
                }
        }
        """
        self.rule = None
        self.node = None

        self.productions = []

    def parse_attributes(self, attributes):
        attrs = {}
        for attr in attributes:
            k = attr[0]
            v = attr[1]
            if k not in attrs.keys():
                attrs[k] = v
            else:
                print('attributes multi same keys: %s' % str(attributes))
        return attrs

    def parse_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        attrs = self.parse_attributes(attributes)
        if tag == 'emu-production':
            self.production = {'name': None, 'params': [], 'rules': []}
            self.production['name'] = attrs['name']
            if 'params' in attrs.keys():
                self.production['params'] = attrs['params'].split(', ')
        elif tag == 'emu-rhs':
            self.rule = {'nodes': []}
        elif tag == 'emu-nt':
            self.node = {'type': 'RULE', 'value': None, 'params': []}
        elif tag == 'emu-t':
            self.node = {'type': 'TEXT', 'value': None, 'params': []}


    def handle_starttag(self, emu, rhs, tag, attrs):
        if self.state == STATE_SEARCHING:
            if tag == 'emu-annex':
                attrs = self.parse_attributes(attrs)
                if 'id' in attrs.keys() and attrs['id']=='sec-grammar-summary':
                    self.state =    
                    print('begin to parsing ecma grammer defination')
        elif self.state == STATE_PARSING:
            self.parse_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if self.state == STATE_SEARCHING:
            return
        if tag not in self.valid_tags:
            return

        stag = self.tag_stack.pop()
        if stag!=tag:
            raise(ECMAException("Encountered an end tag != stag: %s!=%s" % (tag, stag)))
        
        self.parse_endtag(tag)

    def handle_data(self, data):
        if self.state == STATE_SEARCHING:
            return
        print("Encountered some data  :", data)

def parse(data):
    parser = ECMAHTMLParser()
    parser.feed(data)

if __name__=='__main__':
    file = sys.argv[1]
    with open(file) as fr:
        data = fr.read()
        parse(data)
