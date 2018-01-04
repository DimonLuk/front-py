"""
This is to create website only with python
All styles with bootstrap 4
"""
from core import WebPage
from containers import BlockContainer
from default import ParagraphElement, ImageElement

image = ImageElement("test.png","Myalt")
image._addClass("col-2")
image._addStyle({"asdasd":"adasdas"})
image.render()

text = ParagraphElement("Some test")
text._addClass("mx-auto")
text.addContent(image)
text.render()

otherText = ParagraphElement("OtherText")
otherText._addClass("mx-auto")
otherText.render()

container = BlockContainer()
container.addContent(text,otherText,text,otherText,text,otherText)
container.render()

page = WebPage("test","Test","utf-8")
page.addContent(container)
page.load()
