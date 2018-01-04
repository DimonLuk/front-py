class CoreMeta(type):
    def __new__(cls,name,bases,dct):
        dct["_replace"] = _replace()
        dct["_clean"] = _clean()
        return super(CoreMeta,cls).__new__(cls,name,bases,dct)

class _replace:
    def __call__(self,it,content,index):
        toRm = 0
        count = 0
        for i in range(len(it.template)):
            if it.template[i-2]=="|" and it.template[i-1] == "|" and it.template[i]=="|":
                toRm = i-2
                if count == index:
                    break
                else:
                    count = count + 1
        if toRm != 0:
            it.template = it.template[:toRm] + content + "|||" + it.template[toRm+3:]
class _clean:
    def __call__(self,it,index):
        toRm = 0
        count = 0
        for i in range(len(it.template)): 
            if it.template[i-2] == "|" and it.template[i-1] == "|" and it.template[i]=="|":
                toRm = i-2
                if count == index:
                    break
                else:
                    count = count +1
        if toRm != 0:
            it.template = it.template[:toRm] + it.template[toRm+3:]


class WebPage(metaclass=CoreMeta):
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
            <div class="global">
            |||
            </div>
            <script src="script.js"></script>
            </body>
        </html>
        """
        self._replace(self,self.title,0)
        self._replace(self,self.encoding,1)
        self._clean(self,0)
        self._clean(self,0)
    def addContent(self,*content):
        """
        Add any additional content to body
        """
        for i in content:
            self._replace(self,i.template,0)
    def load(self):
        """
        TODO fix clean function because now it cleans random times but should do it no more then required
        Creats html file
        """
        self._clean(self,0)
        with open("%s.html" % self.filename,"w") as file:
            file.write(self.template)

page = WebPage("testMeta.html","test","utf-8")
page.load()
