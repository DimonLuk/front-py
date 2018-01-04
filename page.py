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
def replace(self, content,index):
    toRm = 0
    count = 0
    for i in range(len(self.template)):
        if self.template[i-2]=="|" and self.template[i-1] == "|" and self.template[i]=="|":
            toRm = i-2
            if count == index:
                break
            else:
                count = count + 1
    if toRm != 0:
        self.template = self.template[:toRm] + content + "|||" + self.template[toRm+3:]
def cclean(self,index):
    toRm = 0
    count = 0
    for i in range(len(self.template)): 
        if self.template[i-2] == "|" and self.template[i-1] == "|" and self.template[i]=="|":
            toRm = i-2
            if count == index:
                break
            else:
                count = count +1
    if toRm != 0:
        self.template = self.template[:toRm] + self.template[toRm+3:]



class WebPage:
    """
    Main class. It represents the html document with all required parametres
    """
    def __init__(self,filename,title,encoding):
        self.filename = filename
        self.title = title
        self.encoding = encoding
        self.template = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>|||</title>
                <meta charset="|||">
                <link rel="stylesheet" type="text/css" href="style.css">
            </head>
            <body>
            |||
            <script src="script.js"></script>
            </body>
        </html>
        """
        replace(self,self.title,0)
        replace(self,self.encoding,1)
        cclean(self,0)
        cclean(self,0)
    def addContent(self,*content):
        """
        Add any additional content to body
        """
        for i in content:
            replace(self,i.template,0)
        cclean(self,0)
    def load(self):
        """
        TODO fix clean function because now it cleans random times but should do it no more then required
        Creats html file
        """
        with open("%s.html" % self.filename,"w") as file:
            file.write(self.template)




class BlockContainer:
    """
    It's just a <div>
    """
    def __init__(self):
        self.template = """
        <div class="container"><div class="row">|||</div></div>
        """
    def addContent(self,*content):
        """
        Every content in block has to be added throuhg this function
        """
        for i in content:
            replace(self,i.template,0)
        cclean(self,0)




class ParagraphElement:
    def __init__(self, text):
        self.text = text
        self.template = """
        <p class="|||" style="|||">|||</p>
                        """
        replace(self,self.text,2)
        cclean(self,2)
    def _addClass(self,*cl):
        for i in cl:
            replace(self,i+" ",0)
        cclean(self,0)
    def _addStyle(self, style):
        for i in style:
            replace(self,"%s:%s; " % (i,style[i]),1)
        cclean(self,1)



class Positions:
    def __init__(self):
        self.center = "mx-auto"



class TextStyles:
    def __init__(self):
        self.center = "mx-auto"
        
page = WebPage("test1","test1","utf-8")

container = BlockContainer()

text = ParagraphElement("Some test")
text._addClass("mx-auto","col")
text._addStyle({"color":"red","font-weight":"800"})
otherText = ParagraphElement("OtherText")
otherText._addClass("mx-auto","col")
otherText._addStyle({"font-size":"3em","color":"orange"})

container.addContent(text,otherText,text,otherText)
page.addContent(container)

page.load()
