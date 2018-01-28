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
from core.core import Core_element,serve,run_app,Page






        

class Block_container(e._Block_element):
    """
    Is used to build complex structures, sometimes can be useful for user, so no '_' in the begining of name
    """
    def __init__(self):
        super().__init__()
        self._add_class("container")

class Section_container(e._Section_element):
    """
    The same as block but section, only semantic difference
    """
    def __init__(self):
        super().__init__()
        self._add_class("container")

class Block_row(e._Block_element):
    """
    Simple row
    """
    def __init__(self,*content):
        super().__init__()
        self._add_class("row")
        self.add_content(*content)

class Container_row(Block_container):
    """
    Creates row inside a Block_container
    """
    def __init__(self,*content):
        super().__init__()
        self.row = Block_row()
        if content:
            self.add_content(*content)
    def add_content(self,*content):
        self.row.add_content(*content)
    def _render(self):
        super().add_content(self.row)
        super()._render()

class Section_row(Section_container):
    """
    Creates a row inside Section_container
    """
    def __init__(self):
        super().__init__()
        self.row = Block_row()
    def add_content(self,*content):
        self.row.add_content(*content)
    def _render(self):
        super().add_content(self.row)
        super()._render()



class Inline_menu(e._Block_element):
    """
    Simple inline bootstrap menu

    The first argument is json represantion of background like {"background":"<some color here>"}
    The second is json like links {"Home":"/","Any page":"/any"}
    The third is color of links
    The fourth is Brand_text or Brand_image object

    If you call this object you'll get deepcopy of it
    """
    def __init__(self, background, links, links_color,brand):
        """
        It has been used a lot of bootstrap features here
        Nothing to describe.
        Just create required element and configure according to bootstrap
        """
        self.background = background
        self.links = links
        self.links_color = links_color
        self.brand = brand
        super().__init__()
        self._add_style(background)

        self.header = e._Header_element()
        self.header._add_class("container")
        self.header._add_style(self.background)
        
        
        self.menu = e._Menu_element()
        self.menu._add_class("row")

        self.navigation = e._Navigation_element()
        self.navigation._add_class("navbar","navbar-toggleable-md","navbar-inverse","bg-faded","col-12","mx-auto")
        self.navigation._add_style(self.background)

        self.collapse_button = e._Button_element(text="",attributes=["class","style","type","data-toggle","data-target","aria-controls","aria-expanded","aria-label"])
        self.collapse_button._add_class("navbar-toggler","navbar-toggler-right")
        self.collapse_button._add_attr_value("type","button")
        self.collapse_button._add_attr_value("data-toggle","collapse")
        self.collapse_button._add_attr_value("data-target",".toggleTarget")
        self.collapse_button._add_attr_value("aria-controls","toggleTarget")
        self.collapse_button._add_attr_value("aria-expanded","false")
        self.collapse_button._add_attr_value("aria-label","Toggle navigation")

        self.toggle_icon = e._Text_element()
        self.toggle_icon._add_class("navbar-toggler-icon")
        self._add_style({"color":"white"})
        self.collapse_button.add_content(self.toggle_icon)
        
        self.nav_block = e._Block_element()
        self.nav_block._add_class("collapse","navbar-collapse","toggleTarget")

        self.links_list = e._Unnumbered_list_element()
        self.links_list._add_class("navbar-nav","mr-left")

        for i in self.links:
            li = e._In_list_element()
            li._add_class("nav-item","active")
            for j in i:
                href = e._Link_element(i[j])
                href.add_content(j)
                href._add_class("nav-link")
                href._add_style({"color":self.links_color})
                li.add_content(href)

            self.links_list.add_content(li)
    def _render(self):
        self.nav_block.add_content(self.links_list)
        self.navigation.add_content(self.collapse_button,self.brand,self.nav_block)
        self.menu.add_content(self.navigation)
        self.header.add_content(self.menu)
        self.add_content(self.header)
        super()._render()
    
    def _add_link(self,links,color=""):
        for link in links:
            li = e._In_list_element()
            li._add_class("nav-item","active")

            href = e._Link_element(links[link])
            href.add_content(link)
            href._add_class("nav-link")
            if color:
                href._add_style({"color":color})
            else:
                href._add_style({"color":self.links_color})
            
            li.add_content(href)
            self.links_list.add_content(li)
    def __call__(self,links={},color=""):
        import copy
        cop = copy.deepcopy(self)
        if links:
            cop._add_link(links,color)
        return cop
    
    def add_links(self,links,color=""):
        return self(links,color)
        
class Brand_text(e._Link_element):
    """
    Company name or other brand short and nice info

    The first argument is text
    The second is color
    """
    def __init__(self,text="",color="#ffffff"):
        super().__init__(href="")
        self.color = color
        self.text = text
        self._add_class("navbar-brand")
        self._add_style({"color":self.color})
        self._add_attr_value("href","#")
        self.add_content(self.text)

class Brand_image(Brand_text):
    """
    Company logo
    The firts arg is name of the picture which is inside the media folder of the project
    The second is text to be displayed if picture can't be loaded
    """
    def __init__(self,imageName,alt):
        super().__init__()
        self.img = e._Image_element(imageName,alt)
        self.add_content(self.img)

        
###########################################################################################
#THE BLOCK BELOW HAS BEEN CREATED TOO FAST SO IT'S A LITLE RANDOM
##########################################################################################

class Article(e._Article_element):
    def __init__(self,header_text="",headers_level=1,paragraph="",footer="",column_num=4,responsive=True,save_format=False,is_code=False,lang="",background={}):
        super().__init__()
        self.checker = False
        self.save_format = save_format
        self.is_code = is_code
        if self.save_format and self.is_code:
            self.paragraph = e._Code_element()
            self.paragraph._add_class(lang)
        else:
            self.paragraph = e._Paragraph_element()
        if background:
            self.paragraph._add_style(background)
        self.text = paragraph
        self.header_text = header_text
        self.footer = footer
        self.column_num = column_num
        self.responsive = responsive
        self.headers_level = headers_level
        self._add_class("col-lg-%s" % str(column_num))
        if self.responsive:
            self._add_class("col-12")
        if self.header_text:
            self.header = e._Header_element()

            self.h = e._Header_text_element(headers_level)
            self.h.add_content(header_text)

            self.header.add_content(self.h)
        if self.text:
            self.paragraph.add_content(self.text)
    def add_content(self,*content):
        self.checker = True
        self.paragraph.add_content(*content)
    def _render(self):
        if self.save_format and self.is_code:
            tmp = e._Formated_text_element()
            tmp.add_content(self.paragraph)
            self.paragraph = tmp
        if self.header_text:
            super().add_content(self.header)
        if self.text or self.checker:
            super().add_content(self.paragraph)
        if self.footer:
            super().add_content(self.footer)
        super()._render()
    def __call__(self,header_text="",text="",footer=""):
        obj = Article(header_text=header_text,headers_level=self.headers_level,paragraph=text,footer=footer,column_num=self.column_num,responsive=self.responsive)
        return obj

class Row_articles(Section_row):
    """
    Creates a lot of articles. Each article in one single row
    
    The first argument is title of all articles| not required
    The second is position, now only center or nothing allowed| not required

    Use 'config' method to set your preferences for all articles
    """
    def __init__(self,section_title="",position="center",horizontal_distance="",horizontal_line=False,headers_level=2,save_format=False,is_code=False,lang="",articles_background={},*articles):
        super().__init__()
        self.save_format = save_format
        self.is_code = is_code
        self.articles_background = articles_background
        self.articles = [] #Array with all articles
        if section_title:
            self.section_title = section_title
            header = e._Header_element()
            if position == "center":
                header._add_class("mx-auto")
            h = e._Header_text_element(1,self.section_title)
            header.add_content(h)
            self.add_content(header)
        self.horizontal_line = horizontal_line
        self.horizontal_distance = horizontal_distance
        self.headers_level = headers_level
        if articles:
            for i in articles:
                self.articles.append(i)
    def add_article(self,header_text="",text="",footer="",save_format=False,is_code=False,lang="",background={}):
        """
        Adds single artile with header, text, and footer. All arguments are not required and can be objects
        """
        article = Article(header_text=header_text,paragraph=text,footer=footer,headers_level=self.headers_level,column_num=12,save_format=save_format,is_code=is_code,lang=lang,background=background)
        if self.horizontal_line:
            article.add_content(e._Horizontal_line_element())
        
        if self.horizontal_distance:
            article._add_style({"margin-top":self.horizontal_distance})
        
        self.articles.append(article)
    def _render(self):
        self.add_content(*self.articles)
        super()._render()
    def __call__(self,header_text="",text="",footer=""):
        self.add_article(header_text=header_text,text=text,footer=footer,save_format=self.save_format,is_code=self.is_code,background=self.articles_background)
        return self
    def __iter__(self):
        for i in self.articles:
            yield i

class Footer(e._Footer_element):
    """
    Cretes footer
    The first argument is content to be displayed
    The second is height of the footer
    """
    def __init__(self,content="",height=30):
        super().__init__()
        self._add_class("footer")
        self.row = Container_row()

        if content:
            self.row.add_content(content)
        self.height = height
        self._add_style({"padding-top":"%spx"% (self.height/2),"padding-bottom":"%spx"% (self.height/2)})

    def add_content(self,*content):
        self.row.add_content(*content)
    def _render(self):
        super().add_content(self.row)
        super()._render()
    def __setattr__(self,name,value):
        if name == "background_color":
            self._add_style({"background":value})
        else:
            self.__dict__[name] = value


class Numbered_list(e._Numbered_list_element):
    def __init__(self,content_style={},*content):
        super().__init__()
        self.li = e._In_list_element()
        self.li._add_style(content_style)
        if content:
            for i in content:
                self.add_content(self.li(i))
    def add_elements(self,*elements):
        for i in elements:
            self.add_content(self.li(i))
    def __call__(self,*elements):
        import copy
        cop = copy.deepcopy(self)
        cop.add_elements(*elements)
        cop._render()
        return cop._template

class Column_articles(Section_container):
    def __init__(self,header="",footer="",headers_level=1,position="",vertical_distance="30px",horizontal_line=False,*articles):
        super().__init__()
        self.header = header
        self.headers_level = headers_level
        self.line = horizontal_line
        self.footer = footer
        self.row_header = Block_row()
        
        self.head = Header(self.headers_level,header)
        if position == "center":
            self.head._add_class("mx-auto")
        self.row_header.add_content(self.head)
        if vertical_distance:
            self.row_header._add_style({"margin-bottom":vertical_distance})
        super().add_content(self.row_header)
        
        self.rowArticles = Block_row()
        if articles:
            self.rowArticles.add_content(*articles)
    def add_content(self,*content):
        self.rowArticles.add_content(*content)
    def _render(self):
            super().add_content(self.rowArticles)
            if self.footer:
                super().add_content(self.footer)
            if self.line:
                super().add_content(e._Horizontal_line_element())
            super()._render()
    def __call__(self,*articles):
        for i in articles:
            self.add_content(i)
