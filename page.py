from frontpy.frontpy import *
menu = InlineMenu({"background":"black"},{"Home":"/", "Quick guide":"/quickGuide"},"#ffffff",BrandText("Front-py","#00ee00"))
@serve("/")
def index(request):
    page = Page("Sample","utf-8",{"background":"whitesmoke"})
    page.addElement(menu)
    return page

@serve("/quickGuide")
def quickGuide(request):
    page = Page("QuickGuide","utf-8")
    page.addElement(menu)
    return page

@serve("/<any>")
def test(request):
    page = Page("%s" % request.path[1:],"utf-8",{"background-color":"whitesmoke"})
    page.addElement(menu)
    return page

runApp()
