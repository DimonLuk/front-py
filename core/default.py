from .core import CoreMeta,CoreElement

class Paragraph(CoreElement):
    def __init__(self,element="p",isClosing=True,isAddAttrs=True,attributes=["class","style"],content=""):
        super().__init__(element,isClosing,isAddAttrs,attributes)
        if "content" in self._indexesList:
            self._replace(self,content,self._indexesList["content"])

class Image(CoreElement):
    def __init__(self,element="img",isClosing=False,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)
