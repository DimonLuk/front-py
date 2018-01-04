from core import CoreMeta


class TestElement():
    def __init__(self):
        self.template = "TestTemplate"


class ParagraphElement(metaclass=CoreMeta):
    def __init__(self, text):
        self.text = text
        self.template = """
        <p class="|||" style="|||">|||</p>
                        """
        self._replace(self,self.text,2)
    def _addClass(self,*cl):
        for i in cl:
            self._replace(self,i+" ",0)
    def _addStyle(self, style):
        for i in style:
            self._replace(self,"%s:%s; " % (i,style[i]),1)
    def render(self):
        self._clean(self,0)
        self._clean(self,0)
        self._clean(self,0)
    def addContent(self,*content):
        for i in content:
            self._replace(self,i.template,2)

class ImageElement(metaclass=CoreMeta):
    def __init__(self,src,alt="image"):
        self.src = src
        self.alt = alt
        self.template = """
        <img src="%s" alt="%s" class="|||" style="|||">
        """ % (src,alt)
    def _addClass(self,*cls):
        for i in cls:
            self._replace(self,i+" ",0)
    def _addStyle(self,style):
        for i in style:
            self._replace(self,"%s:%s; " %(i,style[i]),1)
    def render(self):
        self._clean(self,0)
        self._clean(self,0)
