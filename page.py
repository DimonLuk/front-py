"""
This is to create website only with python
All styles with bootstrap 4
"""
def clean(self):
    """
    Clean %s after all insertions. '%s' is left because of program architecture
    """
    toRm = 0
    for i in range(len(self.template)):
        if self.template[i-1] == "%" and self.template[i] == "s":
            toRm = i-1
    if toRm != 0:
        self.template = self.template[:toRm] + self.template[toRm+2:]

class WebPage:
    """
    Main class. It represents the html document with all required parametres
    """
    def __clean__(self):
        clean(self)
    def __init__(self,filename,title,encoding):
        self.filename = filename
        self.title = title
        self.encoding = encoding
        self.template = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>%s</title>
                <meta charset="%s">
                <link rel="stylesheet" type="text/css" href="style.css">
            </head>
            <body>
            %s
            <script src="script.js"></script>
            </body>
        </html>
        """ % (self.title, self.encoding,"%s")
    def addContent(self,content):
        """
        Add any additional content to body
        """
        self.template = self.template % (content.template+"\n"+"%s")
    def load(self):
        """
        TODO fix clean function because now it cleans random times but should do it no more then required
        Creats html file
        """
        self.__clean__()
        self.__clean__()
        with open("%s.html" % self.filename,"w") as file:
            file.write(self.template)


class BlockContainer:
    """
    It's just a <div>
    """
    def __clean__(self):
        clean(self)
    def __init__(self):
        self.template = """
        <div>%s</div>
        """ % "%s"
    def addContent(self,*content):
        """
        Every content in block has to be added throuhg this function
        """
        for i in content:
            self.template = self.template % (i.template+"\n%s")
        self.__clean__()


class ParagraphElement:
    def __clean__(self):
        clean(self)
    def __init__(self, text):
        self.text = text
        self.template = """
        <p%s>%s</p>
                        """ % ("%s",self.text)
    def addStyle(self,*style):
        self.template = self.template % (' class="%s"' % "%s")
        for i in style:
            self.template = self.template % ("%s %s" % (i,"%s"))
        self.__clean__()


page = WebPage("test1","test1","utf-8")

container = BlockContainer()

text = ParagraphElement("Some test")
text.addStyle("red")
otherText = ParagraphElement("OtherText")

container.addContent(text,otherText)
page.addContent(container)

page.load()
