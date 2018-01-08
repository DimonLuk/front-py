from core.core import WebPage,serve,runApp
import core.elements as d
test = False
page = WebPage("test","Test","utf-8")
if test:
    for i in d._test:
        obj = i()
        obj.addContent(obj._element)
        obj._addStyle({"color":"orange"})
        obj._addClass("MyClass","My")
        page.addElement(obj)

@serve("/")
def index(request="request"):
    page = WebPage("test","Server","utf-8")
    par = d._ParagraphElement("Trigger")
    text = d._TextElement("Target")
    inp = d._InputElement("text","Some helpful info",False)
    par.onClick("changeColor",[text],{"color":"green"})
    par.addContent(text,text,text,"Some text")
    text.addContent("additional")
    par.addContent(text)
    img = d._ImageElement("test.png")

    page.addElement(par,text,text,inp,img)
    page.load()
    return page
runApp()
