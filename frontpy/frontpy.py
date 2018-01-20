"""
This module is the main part of the framework where everything is connected.
Soon, it'll be split up on some modules like containers and etc


Copyright (C) 2018  Dima Lukashov github.com/DimonLuk

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
#########################################################################################
#WARNING WARNING WARNING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#THIS MODULE HAS TO BE TESTED
#NO EXCEPTIONS ARE HANDLED HERE FOR NOW
#########################################################################################
import sys
sys.path.append(sys.path[0]+"/frontpy")
sys.path.append(sys.path[0]+"/frontpy/core")
import elements as e
from core.core import CoreElement,serve,runApp,Page

class Text(e._TextElement):
    """
    Simple text
    The first argument of constructor is text which will be shown it's nit required
    
    It can be used as wrapper, you can define some simple styles and use it to wrap text
    For example:
    greenText = Text()
    greenText.color = "green" or greenText.addStyle({"color":"green"})
    p = Paragraph("Some %s text" % greenText("green"))
    
    Or you can use this class in usual way
    """
    def __init__(self,text=""):
        super().__init__(text=text)
    
    def __setattr__(self,name,value):
        if name == "color":
            self._addStyle({"color":value})
        elif name == "position" and value == "center":
            self._addClass("mx-auto")#To place in center in .container > .row
            self._addStyle({"text-align":value})#Sometimes it's useful
        else:
            self.__dict__[name] = value
    def addStyle(self,style):
        self._addStyle(self,style)

class Paragraph(e._ParagraphElement):
    """
    Simple paragraph
    The first argument is text which is not required
    """
    def __init__(self,text=""):
        super().__init__(text=text)

class Image(e._LinkElement):
    """
    Simple responsive image
    """
    def __init__(self,href,alt="picture",columns=6):
        super().__init__(href)
        self.image = e._ImageElement(src=href,alt=alt)
        self.image._addStyle({"width":"100%"})
        self._addClass("col-%s"%str(columns))
        self.addContent(self.image)
class HeaderText(e._HeaderTextElement):
    def __init__(self,level=1,text=""):
        super().__init__(level=level,text=text)

class Header(e._HeaderElement):
    def __init__(self,level=1,text=""):
        super().__init__()
        self.h = HeaderText(level,text)
    def _render(self):
        self.addContent(self.h)
        super()._render()
        

class BlockContainer(e._BlockElement):
    """
    Is used to build complex structures, sometimes can be useful for user, so no '_' in the begining of name
    """
    def __init__(self):
        super().__init__()
        self._addClass("container")

class SectionContainer(e._SectionElement):
    """
    The same as block but section, only semantic difference
    """
    def __init__(self):
        super().__init__()
        self._addClass("container")

class BlockRow(e._BlockElement):
    """
    Simple row
    """
    def __init__(self,*content):
        super().__init__()
        self._addClass("row")
        self.addContent(*content)

class ContainerRow(BlockContainer):
    """
    Creates row inside a BlockContainer
    """
    def __init__(self,*content):
        super().__init__()
        self.row = BlockRow()
        if content:
            self.addContent(*content)
    def addContent(self,*content):
        self.row.addContent(*content)
    def _render(self):
        super().addContent(self.row)
        super()._render()

class SectionRow(SectionContainer):
    """
    Creates a row inside SectionContainer
    """
    def __init__(self):
        super().__init__()
        self.row = BlockRow()
    def addContent(self,*content):
        self.row.addContent(*content)
    def _render(self):
        super().addContent(self.row)
        super()._render()

class Link(e._LinkElement):
    def __init__(self,href,text):
        super().__init__(href=href)
        self.addContent(text)

class InlineMenu(e._BlockElement):
    """
    Simple inline bootstrap menu

    The first argument is json represantion of background like {"background":"<some color here>"}
    The second is json like links {"Home":"/","Any page":"/any"}
    The third is color of links
    The fourth is BrandText or BrandImage object

    If you call this object you'll get deepcopy of it
    """
    def __init__(self, background, links, linksColor,brand):
        """
        It has been used a lot of bootstrap features here
        Nothing to describe.
        Just create required element and configure according to bootstrap
        """
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
    def _render(self):
        self.navBlock.addContent(self.linksList)
        self.navigation.addContent(self.collapseButton,self.brand,self.navBlock)
        self.menu.addContent(self.navigation)
        self.header.addContent(self.menu)
        self.addContent(self.header)
        super()._render()
    
    def _addLink(self,links,color=""):
        for link in links:
            li = e._InListElement()
            li._addClass("nav-item","active")

            href = e._LinkElement(links[link])
            href.addContent(link)
            href._addClass("nav-link")
            if color:
                href._addStyle({"color":color})
            else:
                href._addStyle({"color":self.linksColor})
            
            li.addContent(href)
            self.linksList.addContent(li)
    def __call__(self,links={},color=""):
        import copy
        cop = copy.deepcopy(self)
        if links:
            cop._addLink(links,color)
        return cop
    
    def addLinks(self,links,color=""):
        return self(links,color)
        
class BrandText(e._LinkElement):
    """
    Company name or other brand short and nice info

    The first argument is text
    The second is color
    """
    def __init__(self,text="",color="#ffffff"):
        super().__init__(href="")
        self.color = color
        self.text = text
        self._addClass("navbar-brand")
        self._addStyle({"color":self.color})
        self._addAttrValue("href","#")
        self.addContent(self.text)

class BrandImage(BrandText):
    """
    Company logo
    The firts arg is name of the picture which is inside the media folder of the project
    The second is text to be displayed if picture can't be loaded
    """
    def __init__(self,imageName,alt):
        super().__init__()
        self.img = e._ImageElement(imageName,alt)
        self.addContent(self.img)

        
###########################################################################################
#THE BLOCK BELOW HAS BEEN CREATED TOO FAST SO IT'S A LITLE RANDOM
###########################################################################################

class Article(e._ArticleElement):
    def __init__(self,headerText="",headersLevel=1,paragraph="",footer="",columnNum=4,responsive=True,saveFormat=False,isCode=False,lang="",background={}):
        super().__init__()
        self.checker = False
        self.saveFormat = saveFormat
        self.isCode = isCode
        if self.saveFormat and self.isCode:
            self.paragraph = e._CodeElement()
            self.paragraph._addClass(lang)
        else:
            self.paragraph = e._ParagraphElement()
        if background:
            self.paragraph._addStyle(background)
        self.text = paragraph
        self.headerText = headerText
        self.footer = footer
        self.columnNum = columnNum
        self.responsive = responsive
        self.headersLevel = headersLevel
        self._addClass("col-lg-%s" % str(columnNum))
        if self.responsive:
            self._addClass("col-12")
        if self.headerText:
            self.header = e._HeaderElement()

            self.h = e._HeaderTextElement(headersLevel)
            self.h.addContent(headerText)

            self.header.addContent(self.h)
        if self.text:
            self.paragraph.addContent(paragraph)
    def addContent(self,*content):
        self.checker = True
        self.paragraph.addContent(*content)
    def _render(self):
        if self.saveFormat and self.isCode:
            tmp = e._FormatedTextElement()
            tmp.addContent(self.paragraph)
            self.paragraph = tmp
        if self.headerText:
            super().addContent(self.header)
        if self.text or self.checker:
            super().addContent(self.paragraph)
        if self.footer:
            super().addContent(self.footer)
        super()._render()
    def __call__(self,headerText="",text="",footer=""):
        obj = Article(headerText=headerText,headersLevel=self.headersLevel,paragraph=text,footer=footer,columnNum=self.columnNum,responsive=self.responsive)
        return obj

class RowArticles(SectionRow):
    """
    Creates a lot of articles. Each article in one single row
    
    The first argument is title of all articles| not required
    The second is position, now only center or nothing allowed| not required

    Use 'config' method to set your preferences for all articles
    """
    def __init__(self,sectionTitle="",position="center",horizontalDistance="",horizontalLine=False,headersLevel=2,saveFormat=False,isCode=False,lang="",articlesBackground={},*articles):
        super().__init__()
        self.saveFormat = saveFormat
        self.isCode = isCode
        self.articlesBackground = articlesBackground
        self.articles = [] #Array with all articles
        if sectionTitle:
            self.sectionTitle = sectionTitle
            header = e._HeaderElement()
            if position == "center":
                header._addClass("mx-auto")
            h = e._HeaderTextElement(1,self.sectionTitle)
            header.addContent(h)
            self.addContent(header)
        self.horizontalLine = horizontalLine
        self.horizontalDistance = horizontalDistance
        self.headersLevel = headersLevel
        if articles:
            for i in articles:
                self.articles.append(i)
    def addArticle(self,headerText="",text="",footer="",saveFormat=False,isCode=False,lang="",background={}):
        """
        Adds single artile with header, text, and footer. All arguments are not required and can be objects
        """
        article = Article(headerText=headerText,paragraph=text,footer=footer,headersLevel=self.headersLevel,columnNum=12,saveFormat=saveFormat,isCode=isCode,lang=lang,background=background)
        if self.horizontalLine:
            article.addContent(e._HorizontalLine())
        
        if self.horizontalDistance:
            article._addStyle({"margin-top":self.horizontalDistance})
        
        self.articles.append(article)
    def _render(self):
        self.addContent(*self.articles)
        super()._render()
    def __call__(self,headerText="",text="",footer=""):
        self.addArticle(headerText=headerText,text=text,footer=footer,saveFormat=self.saveFormat,isCode=self.isCode,background=self.articlesBackground)
        return self
    def __iter__(self):
        for i in self.articles:
            yield i

class Footer(e._FooterElement):
    """
    Cretes footer
    The first argument is content to be displayed
    The second is height of the footer
    """
    def __init__(self,content="",height=30):
        super().__init__()
        self._addClass("footer")
        self.row = ContainerRow()

        if content:
            self.row.addContent(content)
        self.height = height
        self._addStyle({"padding-top":"%spx"% (self.height/2),"padding-bottom":"%spx"% (self.height/2)})

    def addContent(self,*content):
        self.row.addContent(*content)
    def _render(self):
        super().addContent(self.row)
        super()._render()
    def __setattr__(self,name,value):
        if name == "backgroundColor":
            self._addStyle({"background":value})
        else:
            self.__dict__[name] = value


class NumberedList(e._NumberedListElement):
    def __init__(self,contentStyle={},*content):
        super().__init__()
        self.li = e._InListElement()
        self.li._addStyle(contentStyle)
        if content:
            for i in content:
                self.addContent(self.li(i))
    def addElements(self,*elements):
        for i in elements:
            self.addContent(self.li(i))
    def __call__(self,*elements):
        import copy
        cop = copy.deepcopy(self)
        cop.addElements(*elements)
        cop._render()
        return cop._template

class ColumnArticles(SectionContainer):
    def __init__(self,header="",footer="",headersLevel=1,position="",verticalDistance="30px",horizontalLine=False,*articles):
        super().__init__()
        self.header = header
        self.headersLevel = headersLevel
        self.line = horizontalLine
        self.footer = footer
        self.rowHeader = BlockRow()
        
        self.head = Header(self.headersLevel,header)
        if position == "center":
            self.head._addClass("mx-auto")
        self.rowHeader.addContent(self.head)
        if verticalDistance:
            self.rowHeader._addStyle({"margin-bottom":verticalDistance})
        super().addContent(self.rowHeader)
        
        self.rowArticles = BlockRow()
        if articles:
            self.rowArticles.addContent(*articles)
    def addContent(self,*content):
        self.rowArticles.addContent(*content)
    def _render(self):
            super().addContent(self.rowArticles)
            if self.footer:
                super().addContent(self.footer)
            if self.line:
                super().addContent(e._HorizontalLine())
            super()._render()
    def __call__(self,*articles):
        for i in articles:
            self.addContent(i)
