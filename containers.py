from core.core import CoreMeta
class BlockContainer(metaclass=CoreMeta):
    """
    It's just a <div>
    """
    def __init__(self):
        self._template = """
        <div class="|||" style="|||"><div class="container"><div class="row">|||</div></div></div>
        """
    def addContent(self,*content):
        """
        Every content in block has to be added throuhg this function
        """
        for i in content:
            self._replace(self,i._template,2)
    def render(self):
        self._clean(self,0)
        self._clean(self,0)
        self._clean(self,0)
    def _addClass(self,*cls):
        for i in cls:
            self._replace(self,i+" ",0)
    def _addStyle(self,style):
        for i in style:
            self._replace(self,"%s:%s; " % (i,style[i]),1)
