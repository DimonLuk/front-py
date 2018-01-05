"""
This is to create website only with python
All styles with bootstrap 4
"""
from core.core import WebPage
from containers import BlockContainer
from core.default import Paragraph, Image

text = Paragraph()
text.addContent("Some text")
text._addClass("mx-auto")
text._addStyle({"color":"red"})

im = Image()
im._addClass("My class")
im._addStyle({"color":"red"})
im.render()

text.addContent(im)
text.render()
page = WebPage("test","Test","utf-8")
page.addContent(text,im)
page.load()
print(page._template)
