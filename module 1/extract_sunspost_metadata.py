from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
        self.capture = False
    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'h1'):
            self.capture = True
    def handle_endtag(self, tag):
        if tag in ('p', 'h1'):
            self.capture = False
    def handle_data(self, data):
        if self.capture:
            self.data.append(data)

parser = MyHTMLParser()
with open('infosnmtot.html','r') as f:
    parser.feed(f.read())
txt = parser.data[0]+'\n'
for elt in parser.data[1:]:
    if elt == '\n':
        txt += elt
    else:
        elt = elt.removeprefix('\n')
        elt = elt.removesuffix('\n')
    if len(elt) > 0:
        if elt[-1] == ':':
            elt = '\n'+elt
    #if elt[0] == '-':
    #    elt = '\n'+elt 
            txt += elt+'\n'
with open('sunspots_metadata.txt', 'w') as out:
    out.write(txt)