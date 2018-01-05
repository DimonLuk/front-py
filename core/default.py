from .core import CoreElement

class _ParagraphElement(CoreElement):
    def __init__(self,text="",element="p",isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self._replace(self,text,self._indexesList["content"])

class _ImageElement(CoreElement):
    def __init__(self,src="#",alt="image",element="img",isClosing=False,isAddAttrs=True,attributes=["class","style","src","alt"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self._addAttrValue("src",src)
        self._addAttrValue("alt",alt)
class _MenuElement(CoreElement):
    def __init__(self,element="menu", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _NavigationElement(CoreElement):             
    def __init__(self,element="nav", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _UnnumberedListElement(CoreElement):             
    def __init__(self,element="ul", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _NumberedListElement(CoreElement):             
    def __init__(self,element="ol", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _InListElement(CoreElement):             
    def __init__(self,element="li", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _LinkElement(CoreElement):             
    def __init__(self,href="#",element="a", isClosing=True,isAddAttrs=True,attributes=["class","style","href"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self._addAttrValue("href",href)

class _BlockElement(CoreElement):             
    def __init__(self,element="div", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _SectionElement(CoreElement):             
    def __init__(self,element="section", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _AsideElement(CoreElement):             
    def __init__(self,element="aside", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _TextElement(CoreElement):             
    def __init__(self,text="",element="span", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self.addContent(text)

class _FooterElement(CoreElement):             
    def __init__(self,element="footer", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _FormElement(CoreElement):             
    def __init__(self,name="",method="POST",element="form", isClosing=True,isAddAttrs=True,attributes=["class","style","method","name"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self._addAttrValue("name",name)
        self._addAttrValue("method",method)

class _InputElement(CoreElement):             
    def __init__(self,typ="text",placeholder="Placeholder",required=False,element="input", isClosing=False,isAddAttrs=True,attributes=["class","style","type","placeholder","required"]):        
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self._addAttrValue("type",typ)
        self._addAttrValue("placeholder",placeholder)
        if required:
            self._addAttrValue("required","true")
        else:
            self._addAttrValue("required","false")
class _ButtonElement(CoreElement):             
    def __init__(self,typ="",text="Button",element="button", isClosing=True,isAddAttrs=True,attributes=["class","style","type"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self._addAttrValue("type",typ)
        self.addContent(text)

class _HeaderElement(CoreElement):             
    def __init__(self,element="header", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _InputTextElement(CoreElement):             
    def __init__(self,placeholder="Placeholder",required=False,element="textarea", isClosing=True,isAddAttrs=True,attributes=["class","style","placeholder","required"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)
        if required:
            self._addAttrValue("required","true")
        else:
            self._addAttrValue("required","false")
        self._addAttrValue("placeholder",placeholder)
_test = (_TextElement,_ParagraphElement,_MenuElement,_NavigationElement,_UnnumberedListElement,_NumberedListElement,_InListElement,_LinkElement,_ImageElement,_BlockElement,_SectionElement,_AsideElement,_FooterElement,_FormElement,_InputElement,_ButtonElement,_HeaderElement,_InputTextElement)
