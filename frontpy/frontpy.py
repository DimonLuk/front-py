import sys
sys.path.append(sys.path[0]+"/frontpy")
sys.path.append(sys.path[0]+"/frontpy/core")
print(sys.path)
import elements as e
from core.core import CoreElement,serve,runApp,WebPage
class InlineMenu(CoreElement):
    def __init__(self, background, links, linksColor,brand="brand"):
        super().__init__("header",True,True,["class","style"])
        self.background = background
        self.links = links
        self.brand = brand
        self.linksColor = linksColor
        self._addClass("container")
        self._addStyle(self.background)
        self.navigation = e._NavigationElement()
        self.navigation._addClass("navbar","navbar-toggleable-md","navbar-light","bg-faded","col-12","mx-auto")
        self.navigation._addStyle(background)

        self.collapseButton = e._ButtonElement("button","",attributes=["class","style","type","data-toggle","data-target","aria-controls","aria-expanded","aria-label"])
        self.togglerIcon = e._TextElement()
        self.togglerIcon._addClass("navbar-toggler-icon")
        self.collapseButton.addContent(self.togglerIcon)
        self.collapseButton._addClass("navbar-toggler navbar-toggler-rigth")
        self.collapseButton._addAttrValue("data-toggle","collapse")
        self.collapseButton._addAttrValue("data-target",".navbarSupportedContent")
        self.collapseButton._addAttrValue("aria-controls","navbarSupportedContent")
        self.collapseButton._addAttrValue("aria-expanded","false")
        self.collapseButton._addAttrValue("aria-label","Toggle navigation")
        

        self.list = e._UnnumberedListElement()
        self.list._addClass("navbar-nav", "mr-left")

        for i in self.links:
            li = e._InListElement()
            li._addClass("nav-item active")
            link = e._LinkElement(self.links[i])
            link._addClass("nav-link")
            link._addStyle({"color":self.linksColor})
            link.addContent(i)
            li.addContent(link)
            self.list.addContent(li)
        self.block = e._BlockElement()
        self.block._addClass("collapse", "navbar-collapse", "navbarSupportedContent")
        self.block.addContent(self.list)
        self.navigation.addContent(self.collapseButton,self.brand,self.block)
        self.menu = e._MenuElement()
        self.menu.addContent(self.navigation)
        self.menu._addClass("row")
        self.addContent(self.menu)
menu = InlineMenu({"background":"black"},{"Home":"/","Quick guide":"/quickGuide"},"#ffffff", "brand")
