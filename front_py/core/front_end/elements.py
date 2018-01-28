"""
This module contains main elements which is used to develop framework
It contains:
    <menu>:_Menu_element
    <nav>:_Navigation_element
    <ul>:_Unnumbered_list_element
    <ol>:_Numbered_list_element
    <li>:_In_list_element
    <a>:_Link_element
    <p>:_Paragraph_element
    <img>:_Image_element
    <div>:_Block_element
    <section>:_Section_element
    <aside>:_Aside_element
    <span>:_Text_element
    <footer>:_Footer_element
    <form>:_Form_element
    <input>(all types):_Input_element
    <button>:_Button_element
    <header>:_Header_element
    <textarea>:_Input_text_area
    <h1-6>:_Header_text_element
    <hr>:_Horizontal_line_element
    <pre>:_Formated_text_element
    <code>:_Code_element
    <article>:_Article_element

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
from Core_element import Core_element


class _Paragraph_element(Core_element):
    def __init__(self,text="",element="p",is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)
        self.add_content(text)

class _Image_element(Core_element):
    def __init__(self,src="#",alt="image",element="img",is_closing=False,is_add_attrs=True,attributes=["class","style","src","alt"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)
        self._add_attr_value("src",src)
        self._add_attr_value("alt",alt)
class _Menu_element(Core_element):
    def __init__(self,element="menu", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Navigation_element(Core_element):             
    def __init__(self,element="nav", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Unnumbered_list_element(Core_element):             
    def __init__(self,element="ul", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Numbered_list_element(Core_element):             
    def __init__(self,element="ol", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _In_list_element(Core_element):             
    def __init__(self,element="li", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Link_element(Core_element):             
    def __init__(self,href="#",element="a", is_closing=True,is_add_attrs=True,attributes=["class","style","href"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)
        self._add_attr_value("href",href)

class _Block_element(Core_element):             
    def __init__(self,element="div", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Section_element(Core_element):             
    def __init__(self,element="section", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Aside_element(Core_element):             
    def __init__(self,element="aside", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Text_element(Core_element):             
    def __init__(self,text="",element="span", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)
        self.add_content(text)

class _Footer_element(Core_element):             
    def __init__(self,element="footer", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Form_element(Core_element):             
    def __init__(self,name="",method="POST",element="form", is_closing=True,is_add_attrs=True,attributes=["class","style","method","name"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)
        self._add_attr_value("name",name)
        self._add_attr_value("method",method)

class _Input_element(Core_element):             
    def __init__(self,typ="text",placeholder="Placeholder",required=False,element="input", is_closing=False,is_add_attrs=True,attributes=["class","style","type","placeholder"]):        
        if required:
            attributes.append("required")
        super().__init__(element,is_closing,is_add_attrs,attributes)
        self._add_attr_value("type",typ)
        self._add_attr_value("placeholder",placeholder)
class _Button_element(Core_element):             
    def __init__(self,typ="",text="Button",element="button", is_closing=True,is_add_attrs=True,attributes=["class","style","type"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)
        self._add_attr_value("type",typ)
        self.add_content(text)

class _Header_element(Core_element):             
    def __init__(self,element="header", is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Input_text_area(Core_element):             
    def __init__(self,placeholder="Placeholder",required=False,element="textarea", is_closing=True,is_add_attrs=True,attributes=["class","style","placeholder"]):
        if required:
            attributes.append("required")
        super().__init__(element,is_closing,is_add_attrs,attributes)
        self._add_attr_value("placeholder",placeholder)
class _Header_text_element(Core_element):
    def __init__(self,level=1,text="", element="h",is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        element = element+str(level)
        super().__init__(element,is_closing,is_add_attrs,attributes)
        if text:
            self.text = text
            self.add_content(self.text)

class _Horizontal_line_element(Core_element):
    def __init__(self,element="hr",is_closing=False,is_add_attrs=False,attributes=[]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Article_element(Core_element):
    def __init__(self,element="article",is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)

class _Formated_text_element(Core_element):
    def __init__(self,element="pre",is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)
class _Code_element(Core_element):
    def __init__(self,element="code",is_closing=True,is_add_attrs=True,attributes=["class","style"]):
        super().__init__(element,is_closing,is_add_attrs,attributes)


_TEST = (_Text_element,_Paragraph_element,_Menu_element,_Navigation_element,_Unnumbered_list_element,_Numbered_list_element,_In_list_element,_Link_element,_Image_element,_Block_element,_Section_element,_Aside_element,_Footer_element,_Form_element,_Input_element,_Button_element,_Header_element,_Input_text_area, _Header_text_element,_Horizontal_line_element,_Formated_text_element,_Code_element,_Article_element)
