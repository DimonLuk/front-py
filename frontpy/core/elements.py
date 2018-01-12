from core.core import CoreElement
"""
This module contains main elements which is used to develop framework
It contains:
    <menu>:_MenuElement
    <nav>:_NavigationElement
    <ul>:_UnnumberedListElement
    <ol>:_NumberedListElement
    <li>:_InListElement
    <a>:_LinkElement
    <p>:_ParagraphElement
    <img>:_ImageElement
    <div>:_BlockElement
    <section>:_SectionElement
    <aside>:_AsideElement
    <span>:_TextElement
    <footer>:_FooterElement
    <form>:_FormElement
    <input>(all types):_InputElement
    <button>:_ButtonElement
    <header>:_HeaderElement
    <textarea>:_InputTextElement

Copyright (C) 2018  Dima Lukashov github.com/DimonLuk

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
class _ParagraphElement(CoreElement):
    def __init__(self,text="",element="p",isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self.addContent(text)

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
    def __init__(self,typ="text",placeholder="Placeholder",required=False,element="input", isClosing=False,isAddAttrs=True,attributes=["class","style","type","placeholder"]):        
        if required:
            attributes.append("required")
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self._addAttrValue("type",typ)
        self._addAttrValue("placeholder",placeholder)
class _ButtonElement(CoreElement):             
    def __init__(self,typ="",text="Button",element="button", isClosing=True,isAddAttrs=True,attributes=["class","style","type"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self._addAttrValue("type",typ)
        self.addContent(text)

class _HeaderElement(CoreElement):             
    def __init__(self,element="header", isClosing=True,isAddAttrs=True,attributes=["class","style"]):
        super().__init__(element,isClosing,isAddAttrs,attributes)

class _InputTextElement(CoreElement):             
    def __init__(self,placeholder="Placeholder",required=False,element="textarea", isClosing=True,isAddAttrs=True,attributes=["class","style","placeholder"]):
        if required:
            attributes.append("required")
        super().__init__(element,isClosing,isAddAttrs,attributes)
        self._addAttrValue("placeholder",placeholder)
_TEST = (_TextElement,_ParagraphElement,_MenuElement,_NavigationElement,_UnnumberedListElement,_NumberedListElement,_InListElement,_LinkElement,_ImageElement,_BlockElement,_SectionElement,_AsideElement,_FooterElement,_FormElement,_InputElement,_ButtonElement,_HeaderElement,_InputTextElement)
