import sys
sys.path.append(sys.path[0]+"/frontpy")
sys.path.append(sys.path[0]+"/frontpy/core")
import elements as e
from core.core import CoreElement,serve,runApp,Page

class Text(e._TextElement):
    def __init__(self,text=""):
        super().__init__(text=text)
    def __str__(self):
        import copy
        cop = copy.deepcopy(self)
        cop._render()
        return cop._template
    def __setattr__(self,name,value):
        if name == "color":
            self._addStyle({"color":value})
        elif name == "position" and value == "center":
            self._addClass("mx-auto")
            self._addStyle({"text-align":value})
        else:
            self.__dict__[name] = value
    def __call__(self,value):
        import copy
        cop = copy.deepcopy(self)
        cop.addContent(value)
        cop._render()
        return cop._template

class Paragraph(e._ParagraphElement):
    def __init__(self,text):
        super().__init__(text=text)

class Image(e._ImageElement):
    def __init__(self,href,alt="picture"):
        super().__init__(href,alt=alt)
        self._addClass("img-fluid")
    def __str__(self):
        import copy
        cop = copy.deepcopy(self)
        cop._render()
        return cop._template

class BlockContainer(e._BlockElement):
    def __init__(self):
        super().__init__()
        self._addClass("container")

class SectionContainer(e._SectionElement):
    def __init__(self):
        super().__init__()
        self._addClass("container")

class BlockRow(e._BlockElement):
    def __init__(self):
        super().__init__()
        self._addClass("row")

class ContainerRow(BlockContainer):
    def __init__(self):
        super().__init__()
        self.row = BlockRow()
    def addContent(self,content):
        self.row.addContent(content)
    def _render(self):
        super().addContent(self.row)
        super()._render()

class SectionRow(SectionContainer):
    def __init__(self):
        super().__init__()
        self.row = BlockRow()
    def addContent(self,content):
        self.row.addContent(content)
    def _render(self):
        super().addContent(self.row)
        super()._render()



class InlineMenu(e._BlockElement):
    def __init__(self, background, links, linksColor,brand):
        self.background = background
        self.links = links
        self.linksColor = linksColor
        self.brand = brand
        super().__init__()
        self._addStyle(background)

        self.header = e._HeaderElement()
        self.header._addClass("container")
        self.header._addStyle(self.background)
        
        
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
        self.header.addContent(self.menu)
        self.addContent(self.header)




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

class RowArticles(SectionRow):
    def __init__(self,sectionTitle="",position="center"):
        super().__init__()
        if sectionTitle:
            self.sectionTitle = sectionTitle
            header = e._HeaderElement()
            if position == "center":
                header._addClass("mx-auto")
            h = e._HeaderTextElement(1,self.sectionTitle)
            header.addContent(h)
            self.addContent(header)
    
    def config(self,horizontalDistance="", horizontalLine=False, headersLevel=2):
        self.horizontalLine = horizontalLine
        self.headersLevel = headersLevel
        if horizontalDistance:
            self.horizontalDistance = horizontalDistance
    def addArticle(self,headerText="",text="",footer=""):
        article = e._ArticleElement()
        article._addClass("col-12")
        header = {}
        paragraph = {}
        foot = {}
        if headerText:
            header = e._HeaderElement()
            h = e._HeaderTextElement(self.headersLevel,headerText)
            
            header.addContent(h)
            article.addContent(header)
        
        if text:
            paragraph = e._ParagraphElement(text)
            article.addContent(paragraph)
        
        if footer:
            #TODO
            pass
        
        if self.horizontalLine:
            article.addContent(e._HorizontalLine())
        if self.horizontalDistance:
            article._addStyle({"margin-top":self.horizontalDistance})
        self.addContent(article)


class Footer(e._FooterElement):
    def __init__(self,content="",width=30):
        super().__init__()
        self._addClass("footer")
        self.row = ContainerRow()

        if content:
            self.row.addContent(content)
        self.width = width
        self._addStyle({"padding-top":"%spx"% (width/2),"padding-bottom":"%spx"% (width/2)})

    def addContent(self,content):
        self.row.addContent(content)
    def _render(self):
        super().addContent(self.row)
        super()._render()
    def __setattr__(self,name,value):
        if name == "BackgroundColor":
            self._addStyle({"background":value})
        else:
            self.__dict__[name] = value
