from frontpy.frontpy import *
menu = InlineMenu({"background":"black"},{"Home":"/", "Quick guide":"/quickGuide"},"#ffffff","Front-py")
@serve("/")
def index(request):
    page = WebPage("test","Sample","utf-8")
    page.addElement(menu)
    page.load()
    return page

runApp()
