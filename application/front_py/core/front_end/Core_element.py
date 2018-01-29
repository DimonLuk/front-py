"""
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
from constants import *
from exceptions import *
from Core_meta import Core_meta

class Core_element(metaclass = Core_meta):
    """
    This class presents is used to build core elements which is simple html tags
    Private methods (user mustn't use this methods):
        _add_style - to add css style to html element
        _add_class - to add class to html element
        _render - removes all replacement expression
        This list may be extended
    Private fields (user mustn't use this variables):
        _element - shows which html element to be created
        _is_closing - shows if the element has closing tag or not. True - has
        _is_add_attrs - shows if the method has to have attributes. True - has to
        _attributes - list or tuple of attributes that has to be added to the element
        _template - DOM representation of the object
    Public fields:
        add_content - adds any content into element if it's possible
    """
    def __init__(
            self, element="", is_closing=True,
            is_add_attrs=True, attributes=[]):
        self._element = element
        self._is_closing = is_closing
        self._attributes = attributes
        self._index = 0#Shows which attribute from _attributes is now in processing
        self._is_add_attrs = is_add_attrs
        self._indexes_list = dict()#Dictionary which will contain {nameOfAttribute:indexToInsertContent}
        if self._is_closing:#If tag has to be closed
            self._template = """<%s|||>|||</%s>""" % (element,element)
        else:#If tag doesn't have to be closed
            self._template = """<%s|||>""" % element
        if self._is_add_attrs:
            for i in attributes:
                self._replace(self," "+i+'="|||"',self._index) #Add attribute
                self._indexes_list[i] = self._index#Save the name of attribute and its index(for _replace method)
                self._index += 1
            self._clean(self,self._index)#And clean replacement expression which has been used to add attributes
            if self._is_closing:#If tag has to be closed then
                self._indexes_list["content"] = self._index#It can have some content
        else:
            self._clean(self,self._index)#If no attributes just clean replacement expression for attributes
            if self._is_closing:
                self._indexes_list["content"] = self._index#If tag has to be closed then save index for _replace method
    def __str__(self):
        import copy
        cop = copy.deepcopy(self)
        cop._render()
        return cop._template

    def __call__(self, *content):
        import copy
        cop = copy.deepcopy(self)
        cop.add_content(*content)
        cop._render()
        return cop._template
    
    def _add_style(self, styles):
        """
        Add style to html element
        styles - JSON like object which contains css properties like {"name":"value"}
        """
        self._styles = styles
        if "style" in self._indexes_list:
            for i in self._styles:
                self._replace(self, "%s:%s; " % (i, self._styles[i]), self._indexes_list["style"])
    def _add_class(self, *cls):
        """
        Add classes
        *cls - tuple of classes to be added
        """
        self._cls = cls#represents classes of html tag
        if "class" in self._indexes_list:
            for i in self._cls:
                self._replace(self, "%s " % i, self._indexes_list["class"])
    def _add_attr_value(self,attr,value):
        if attr in self._indexes_list:
            self._replace(self, value, self._indexes_list[attr])

                    
    def add_content(self, *content):
        """
        Add content which is str or any object that contains _template field
        """
        self._content = content#Represents content to be added to 'self' object
        for i in self._content:
            if type(i) is str:#If content is str
                if "content" in self._indexes_list:#and it's field to add content
                    self._replace(self, i, self._indexes_list["content"])
            else:#If content is some object
                if "content" in self._indexes_list:
                    try:
                        import copy
                        cop = copy.deepcopy(i)#Deep copy because original object can be chenged later
                        cop._render()
                        self._replace(self, cop._template, self._indexes_list["content"])
                    except AttributeError:
                        raise Invalid_insertion(INVALID_INSERTION_MESSAGE % i)
    def _render(self):
        """
        Preparing object to be used. REQURIED METHOD
        """
        for i in self._indexes_list:#Clean all replacement expressions
            self._clean(self, 0)
    def _link_elements(self, targets=[]):
        """
        Links number of elemnts to make them avaliable to add event. self is a trigger, other elements are targets
        """
        self._trigger = self._generate_trigger() #classname for tag which will emit the event
        self._target = self._generate_target(self._trigger)#classname for tag which will be changed during the event
        if targets:
            for i in targets:
                try:#If sth not from framework has been passed
                    if "class" in i._indexes_list:
                        i._replace(i, "%s " % self._target, i._indexes_list["class"])
                    else:
                        raise Missing_parameter_error("Add attribute 'class' for html element %s" % i)
                except AttributeError:
                    raise Invalid_insertion(INVALID_INSERTION_MESSAGE % i)
        else:
            raise Unlinked_elements_error("You haven't linked any elements to create events between them")
        if "class" in self._indexes_list:
            try:#Just for safety
                self._replace(self, "%s " % self._trigger,self._indexes_list["class"])
            except AttributeError:
                raise Invalid_insertion(INVALID_INSERTION_MESSAGE % self)
        else:
            raise Missing_parameter_error("Add attribute 'class' for html element %s" % i)
    def _add_script(self,toDo):
        """
        Creates jquery interpritation of event for browsers
        """
        with open("./pages/scripts/script.js", "a") as script:
            script.write(toDo)
    def on_click(self, toDo, targets=[], params={}):
        """
        Args:
        the first - some predefined word
        the second - elemetns which have to be involved as targets
        the third - dictionary with parametres if they are required
        """
        self._link_elements(targets)
        self._on_clickParams = params
        if toDo == "changeColor":
            self._add_script(";(function(){var changed = false;var color = $('.%s').css('color');$('.%s').click(function(event){event.stopPropagation();if(changed){$('.%s').css({'color':color});changed = false;}else{$('.%s').css({'color':'%s'});changed = true;}});})();"%(self._target,self._trigger,self._target,self._target,self._on_clickParams["color"]))
        else:
            raise Unsupported_feature("'%s' event for click is unsupported, please write to author lds4ever2000@gmail.com" % toDo)




import unittest
class Test_core_element(unittest.TestCase):
    def __init__(self,a):
        super().__init__(a)
        self.test = Core_element(
                element="p", is_closing=True,
                is_add_attrs=True, attributes=["class","style","someattr"])
    
    def test_constructor(self):
        self.assertEqual('<p class="" style="" someattr=""></p>', self.test.__str__())

    def test_add_class(self):
        self.test._add_class("Test")
        self.assertEqual('<p class="Test " style="" someattr=""></p>', self.test.__str__())
    
    def test_add_style(self):
        self.test._add_style({"color":"black","test":25})
        self.assertEqual('<p class="" style="color:black; test:25; " someattr=""></p>', self.test.__str__())

    def test_add_attr_value(self):
        self.test._add_attr_value("someattr", "test")
        self.assertEqual('<p class="" style="" someattr="test"></p>', self.test.__str__())

    def test_add_content(self):
        self.test.add_content("Some test"," another test")
        self.assertEqual('<p class="" style="" someattr="">Some test another test</p>', self.test.__str__())
