"""
This module contains primitive html elements which is used to develop framework
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

    <textarea>:_InputTextArea

    <h1-6>:_HeaderTextElement

    <hr>:_HorizontalLineElement

    <pre>:_FormatedTextElement

    <code>:_CodeElement

    <article>:_ArticleElement

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
from CoreElement import CoreElement


class _ParagraphElement(CoreElement):
    def __init__(self, text="", element="p", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)
        self.add_content(text)


class _ImageElement(CoreElement):
    def __init__(
            self, src="#", alt="image", element="img", is_closing=False,
            is_add_attrs=True, attributes=["class", "style", "src", "alt"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)
        self._add_attr_value("src", src)
        self._add_attr_value("alt", alt)


class _MenuElement(CoreElement):
    def __init__(self, element="menu", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _NavigationElement(CoreElement):
    def __init__(self, element="nav", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _UnnumberedListElement(CoreElement):
    def __init__(self, element="ul", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _NumberedListElement(CoreElement):
    def __init__(self, element="ol", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _InListElement(CoreElement):
    def __init__(self, element="li", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _LinkElement(CoreElement):
    def __init__(self, href="#", element="a", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style", "href"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)
        self._add_attr_value("href", href)


class _BlockElement(CoreElement):
    def __init__(self, element="div", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _SectionElement(CoreElement):
    def __init__(self, element="section", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _AsideElement(CoreElement):
    def __init__(self, element="aside", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _TextElement(CoreElement):
    def __init__(self, text="", element="span", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)
        self.add_content(text)


class _FooterElement(CoreElement):
    def __init__(self, element="footer", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _FormElement(CoreElement):
    def __init__(self, name="", method="POST", element="form", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style", "method", "name"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)
        self._add_attr_value("name", name)
        self._add_attr_value("method", method)


class _InputElement(CoreElement):
    def __init__(
            self, typ="text", placeholder="Placeholder", required=False,
            element="input", is_closing=False, is_add_attrs=True,
            attributes=["class", "style", "type", "placeholder"]):
        if required:
            attributes.append("required")
        super().__init__(element, is_closing, is_add_attrs, attributes)
        self._add_attr_value("type", typ)
        self._add_attr_value("placeholder", placeholder)


class _ButtonElement(CoreElement):
    def __init__(self, typ="", text="Button", element="button",
                 is_closing=True, is_add_attrs=True,
                 attributes=["class", "style", "type"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)
        self._add_attr_value("type", typ)
        self.add_content(text)


class _HeaderElement(CoreElement):
    def __init__(self, element="header", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _InputTextArea(CoreElement):
    def __init__(self, placeholder="Placeholder", required=False,
                 element="textarea", is_closing=True, is_add_attrs=True,
                 attributes=["class", "style", "placeholder"]):
        if required:
            attributes.append("required")
        super().__init__(element, is_closing, is_add_attrs, attributes)
        self._add_attr_value("placeholder", placeholder)


class _HeaderTextElement(CoreElement):
    def __init__(self, level=1, text="", element="h", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        element = element+str(level)
        super().__init__(element, is_closing, is_add_attrs, attributes)
        if text:
            self.text = text
            self.add_content(self.text)


class _HorizontalLineElement(CoreElement):
    def __init__(self, element="hr", is_closing=False,
                 is_add_attrs=False, attributes=[]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _ArticleElement(CoreElement):
    def __init__(self, element="article", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _FormatedTextElement(CoreElement):
    def __init__(self, element="pre", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


class _CodeElement(CoreElement):
    def __init__(self, element="code", is_closing=True,
                 is_add_attrs=True, attributes=["class", "style"]):
        super().__init__(element, is_closing, is_add_attrs, attributes)


_TEST = (
    _TextElement,
    _ParagraphElement,
    _MenuElement,
    _NavigationElement,
    _UnnumberedListElement,
    _NumberedListElement,
    _InListElement,
    _LinkElement,
    _ImageElement,
    _BlockElement,
    _SectionElement,
    _AsideElement,
    _FooterElement,
    _FormElement,
    _InputElement,
    _ButtonElement,
    _HeaderElement,
    _InputTextArea,
    _HeaderTextElement,
    _HorizontalLineElement,
    _FormatedTextElement,
    _CodeElement,
    _ArticleElement)

import unittest


class Test(unittest.TestCase):
    def test_Text_element(self):
        self.assertEqual("""<span class="" style=""></span>""", _TextElement().__str__())

    def test_Paragraph_element(self):
        self.assertEqual("""<p class="" style=""></p>""", _ParagraphElement().__str__())

    def test_Menu_element(self):
        self.assertEqual("""<menu class="" style=""></menu>""", _MenuElement().__str__())

    def test_Navigation_element(self):
        self.assertEqual("""<nav class="" style=""></nav>""", _NavigationElement().__str__())

    def test_Unnumbered_list_element(self):
        self.assertEqual("""<ul class="" style=""></ul>""", _UnnumberedListElement().__str__())

    def test_Numbered_list_element(self):
        self.assertEqual("""<ol class="" style=""></ol>""", _NumberedListElement().__str__())

    def test_In_list_element(self):
        self.assertEqual("""<li class="" style=""></li>""", _InListElement().__str__())

    def test_Link_element(self):
        self.assertEqual("""<a class="" style="" href="#"></a>""", _LinkElement().__str__())

    def test_Image_element(self):
        self.assertEqual("""<img class="" style="" src="#" alt="image" />""", _ImageElement().__str__())

    def test_Block_element(self):
        self.assertEqual("""<div class="" style=""></div>""", _BlockElement().__str__())

    def test_Section_element(self):
        self.assertEqual("""<section class="" style=""></section>""", _SectionElement().__str__())

    def test_Aside_element(self):
        self.assertEqual("""<aside class="" style=""></aside>""", _AsideElement().__str__())

    def test_Footer_element(self):
        self.assertEqual("""<footer class="" style=""></footer>""", _FooterElement().__str__())

    def test_Form_element(self):
        self.assertEqual("""<form class="" style="" method="POST" name=""></form>""", _FormElement().__str__())

    def test_Input_element(self):
        self.assertEqual("""<input class="" style="" type="text" placeholder="Placeholder" />""", _InputElement().__str__())

    def test_Button_element(self):
        self.assertEqual("""<button class="" style="" type="">Button</button>""", _ButtonElement().__str__())

    def test_Header_element(self):
        self.assertEqual("""<header class="" style=""></header>""", _HeaderElement().__str__())

    def test_Input_text_area(self):
        self.assertEqual("""<textarea class="" style="" placeholder="Placeholder"></textarea>""", _InputTextArea().__str__())

    def test_Header_text_element(self):
        self.assertEqual("""<h1 class="" style=""></h1>""", _HeaderTextElement().__str__())

    def test_Horizontal_line_element(self):
        self.assertEqual("""<hr />""", _HorizontalLineElement().__str__())

    def test_Formated_text_element(self):
        self.assertEqual("""<pre class="" style=""></pre>""", _FormatedTextElement().__str__())

    def test_Code_element(self):
        self.assertEqual("""<code class="" style=""></code>""", _CodeElement().__str__())

    def test_Article_element(self):
        self.assertEqual("""<article class="" style=""></article>""", _ArticleElement().__str__())
