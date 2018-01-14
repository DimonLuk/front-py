import sys
sys.path.append(sys.path[0]+"/frontpy")
sys.path.append(sys.path[0]+"/frontpy/core")
import elements as e
from core.core import CoreElement,serve,runApp,Page


class RowContainer(e._BlockElement):
    def __init__(self):
        super().__init__()
        self._addClass("row")

    def _render(self):
        self._template = """<div class="container">%s</div>""" % self._template
        super()._render()


class InlineMenu(CoreElement):
    def __init__(self, background, links, linksColor,brand):
        self.background = background
        self.links = links
        self.linksColor = linksColor
        self.brand = brand
        super().__init__("header",True,True,["class","style"])
        
        self._addClass("container")
        self._addStyle(self.background)
        
        self.menu = e._MenuElement()
        self.menu._addClass("row")

        self.navigation = e._NavigationElement()
        self.navigation._addClass("navbar","navbar-toggleable-md","navbar-inverse","bg-faded","col-12","mx-auto")
        self.navigation._addStyle(self.background)

        self.collapseButton = e._ButtonElement(text="",attributes=["class","style","type","data-toggle","data-target","aria-controls","aria-expanded","aria-label"])
        self.collapseButton._addClass("navbar-toggler","navbar-toggler-right")
        self.collapseButton._addAttrValue("type","button")
        self.collapseButton._addAttrValue("data-toggle","collapse")
        self.collapseButton._addAttrValue("data-target",".toggleTarget")
        self.collapseButton._addAttrValue("aria-controls","toggleTarget")
        self.collapseButton._addAttrValue("aria-expanded","false")
        self.collapseButton._addAttrValue("aria-label","Toggle navigation")

        self.toggleIcon = e._TextElement()
        self.toggleIcon._addClass("navbar-toggler-icon")
        self._addStyle({"color":"white"})
        self.collapseButton.addContent(self.toggleIcon)
        
        self.navBlock = e._BlockElement()
        self.navBlock._addClass("collapse","navbar-collapse","toggleTarget")

        self.linksList = e._UnnumberedListElement()
        self.linksList._addClass("navbar-nav","mr-left")

        for i in self.links:
            li = e._InListElement()
            li._addClass("nav-item","active")

            href = e._LinkElement(self.links[i])
            href.addContent(i)
            href._addClass("nav-link")
            href._addStyle({"color":self.linksColor})

            li.addContent(href)

            self.linksList.addContent(li)
        self.navBlock.addContent(self.linksList)
        self.navigation.addContent(self.collapseButton,self.brand,self.navBlock)
        self.menu.addContent(self.navigation)
        self.addContent(self.menu)



class BrandText(e._LinkElement):
    def __init__(self,text="",color="#ffffff"):
        super().__init__(href="")
        self.color = color
        self.text = text
        self._addClass("navbar-brand")
        self._addStyle({"color":self.color})
        self._addAttrValue("href","#")
        self.addContent(self.text)

class BrandImage(BrandText):
    def __init__(self,imageName,alt):
        super().__init__()
        self.img = e._ImageElement(imageName,alt)
        self.addContent(self.img)
