"""
This is to create website only with python
All styles with bootstrap 4
"""
from core import WebPage
from containers import BlockContainer
from default import Paragraph, Image

text = Paragraph()
text.addContent("Some text")
text._addStyle({"color":"red"})
text._addClass("mx-auto")

im = Image()
im.render()

text.addContent(im.template)
text.render()

container = BlockContainer()
container.addContent(text,im)
container.render()

page = WebPage("test","Test","utf-8")
page.addContent(container)
page.load()
