"""
This is to create website only with python
All styles with bootstrap 4
"""
from core.core import WebPage
from containers import BlockContainer
import inspect
import core.default as d
test = True
page = WebPage("test","Test","utf-8")
if test:
    for i in d._test:
        obj = i()
        obj.addContent(obj._element)
        obj._addStyle({"color":"orange"})
        obj._addClass("MyClass","My")
        obj.render()
        page.addElement(obj)
page.load()
