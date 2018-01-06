from core.core import WebPage
import core.elements as d
test = False
page = WebPage("test","Test","utf-8")
if test:
    for i in d._test:
        obj = i()
        obj.addContent(obj._element)
        obj._addStyle({"color":"orange"})
        obj._addClass("MyClass","My")
        obj.render()
        page.addElement(obj)


par = d._ParagraphElement("Trigger")
text = d._TextElement("Target")
par.onClick("changeColor",[par,text],{"color":"green"})


text.render()
par.render()


page.addElement(par,text,text)
page.load()
