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
from CoreMeta import CoreMeta


class CoreElement(metaclass=CoreMeta):
    """!It's the main class which aim is creating python representation of html elements. Its metaclass is CoreMeta.

    Parameters
    ----------
    element: string
        default: ""
        shows which html element represents current object, but you should pass for example "p", "img" and etc.
    is_closing: boolean
        default: True
        shows if the html element has to be closed(for example \<p\>\</p\>) or not(\<img ...attrs /\>).
    is_add_attrs: boolean
        default: True
        shows if some attributes has to be placed into html element.
    attributes: string[]
        array of strings with names of attributes to be added,
        for example
        >>> ["style","class","id","myattr"]
        to element "p" will result as
        <p style="" class="" myattr=""></p>
        If you haven't added attributes when the object has been created
        you won't be able to add values and attributes later
    """

    def __init__(
            self, element="", is_closing=True,
            is_add_attrs=True, attributes=[]):
        # Shows which html element is represented
        self._element = element

        # Shows if the html tag has to be closed
        self._is_closing = is_closing

        self._mimetype = "text/html"

        # List of HTML attributes to be written in the tag
        self._attributes = attributes

        # Shows which attribute from #_attributes
        # is being processed now
        self._index = 0

        # Shows if it's required to add attributes for tag
        # to make place for attrs
        self._is_add_attrs = is_add_attrs

        #  Dictionary which will contain:
        # @code{"nameOfAttribute":indexToInsertContent}@endcode
        self._indexes_list = dict()
        if self._is_closing:  # If tag has to be closed

            # HTML representation of python object
            self._template = """<%s|||>|||</%s>""" % (element, element)
        else:  # If tag doesn't have to be closed
            self._template = """<%s||| />""" % element
        if self._is_add_attrs:
            for i in attributes:
                self._replace(
                    self,
                    " "+i+'="|||"',
                    self._index)  # Add attribute
                # Save the name of attribute and its index(for _replace method)
                self._indexes_list[i] = self._index
                self._index += 1
            # And clean replacement expression which has been used to add
            # attributes
            self._clean(self, self._index)
            if self._is_closing:  # If tag has to be closed then
                # It can have some content
                self._indexes_list["content"] = self._index
        else:
            # If no attributes just clean replacement expression for attributes
            self._clean(self, self._index)
            if self._is_closing:
                # If tag has to be closed then save index for _replace method
                self._indexes_list["content"] = self._index

    def __str__(self):
        """Creates deepcopy of object, renders it with _render and returns it

        Returns
        ----------
        _template: string
            object which is html representation of object.
        """
        import copy
        cop = copy.deepcopy(self)
        cop._render()
        return cop._template

    def __call__(self, *content):
        """Creates deepcopy of object, put content into copy and return rendered _template.
        It's an implementation of wrapping syntax.

        Parameters
        ----------
        *content: any number of strings and object that are derived from CoreElement
            content to be placed into the object

        Returns
        ----------
        _template: string
            object which is html representation of object
        """
        import copy
        cop = copy.deepcopy(self)
        cop.add_content(*content)
        cop._render()
        return cop._template

    def _add_style(self, styles):
        """Adds value to html attribute style if the object has it.

        Parameters
        ----------
        styles: object (see example)
            JSON object with css3 style notation,
            for example:
            >>> {"text-align":"center","color":"#ff003b"}
        """

        # Styles to be written to HTML tag
        self._styles = styles
        if "style" in self._indexes_list:
            for i in self._styles:
                self._replace(
                    self, "%s:%s; " %
                    (i, self._styles[i]), self._indexes_list["style"])

    def _add_class(self, *cls):
        """Adds value to html attribute class if the object has it.

        Parameters
        ----------
        *cls: string[]
            classnames to be added,
            for example:
            >>> some_object._add_class("col-lg-12","MyClass")
        """

        # HTML classes to be written to the tag
        self._cls = cls  # represents classes of html tag
        if "class" in self._indexes_list:
            for i in self._cls:
                self._replace(self, "%s " % i, self._indexes_list["class"])

    def _add_attr_value(self, attr, value):
        if attr in self._indexes_list:
            self._replace(self, value, self._indexes_list[attr])

    def add_content(self, *content):
        """Adds content to html element if it can be added, content can't be changed after it has been put to object.

        Parameters
        ----------
        *content: any number of strings and objects from framework
            content to be put into object
        """

        # Content to be written to object
        self._content = content  # Represents content to be added to 'self' object
        for i in self._content:
            if isinstance(i, str):  # If content is str
                if "content" in self._indexes_list:  # and it's field to add content
                    self._replace(self, i, self._indexes_list["content"])
            else:  # If content is some object
                if "content" in self._indexes_list:
                    try:
                        import copy
                        # Deep copy because original object can be chenged
                        # later
                        cop = copy.deepcopy(i)
                        cop._render()
                        self._replace(
                            self, cop._template, self._indexes_list["content"])
                    except AttributeError:
                        raise Invalid_insertion(INVALID_INSERTION_MESSAGE % i)

    def _render(self):
        """REQUIRED TO BE CALLED TO INTERPRET HTML CORRECTLY. Renders the _template field by using _clean method.
        """
        for i in self._indexes_list:  # Clean all replacement expressions
            self._clean(self, 0)

    def _link_elements(self, targets=[]):
        """Links elements as target for events in browsers.

        Parameters
        ----------
        targets: objects from framework
            array of objects from the framework which will act as a
            targets of the event, object which has called this method also can act as a target.
        """

        # Personal for each object field, actually it's HTML class property
        # Shows if it's a trigger for some event
        # Soon this will be rewritten
        self._trigger = self._generate_trigger()

        # HTML classname for tag which will be changed during the event
        self._target = self._generate_target(self._trigger)
        if targets:
            for i in targets:
                try:  # If sth not from framework has been passed
                    if "class" in i._indexes_list:
                        i._replace(i, "%s " %
                                   self._target, i._indexes_list["class"])
                    else:
                        raise Missing_parameter_error(
                            "Add attribute 'class' for html element %s" % i)
                except AttributeError:
                    raise Invalid_insertion(INVALID_INSERTION_MESSAGE % i)
        else:
            raise Unlinked_elements_error(
                "You haven't linked any elements to create events between them")
        if "class" in self._indexes_list:
            try:  # Just for safety
                self._replace(
                    self,
                    "%s " %
                    self._trigger,
                    self._indexes_list["class"])
            except AttributeError:
                raise Invalid_insertion(INVALID_INSERTION_MESSAGE % self)
        else:
            raise Missing_parameter_error(
                "Add attribute 'class' for html element %s" % i)

    def _add_script(self, to_do):
        """Adds some javascript to special file which will be sent to browsers.

        Parameters
        ----------
        to_do: string
            javascript, you can use such libraries: jquery and hljs
        """
        self.add_content("<script>%s</script>" % to_do)

    def on_click(self, to_do, targets=[], params={}):
        """Event on object.

        Parameters
        ----------
        to_do: string
            describes the action which will be done during the
            event, now it can be chosen from this list:
            "change_color" -  Avaliable params:
            >>> {"color":"css3_color"}
        targets: objects from the framework
            are targets for the event, object that has called this method can be passed as a target too.
        params: object
            special parameters for each case in list
        """
        self._link_elements(targets)

        # Parameters that should be applied during the event
        # You can read more #on_click
        self._on_clickParams = params
        if to_do == "change_color":
            self._add_script(
                ";(function(){var changed = false;var color = $('.%s').css('color');$('.%s').click(function(event){event.stopPropagation();if(changed){$('.%s').css({'color':color});changed = false;}else{$('.%s').css({'color':'%s'});changed = true;}});})();" %
                (self._target,
                 self._trigger,
                 self._target,
                 self._target,
                 self._on_clickParams["color"]))
        else:
            raise Unsupported_feature(
                "'%s' event for click is unsupported, please write to author lds4ever2000@gmail.com" %
                to_do)


import unittest


class Test_core_element(unittest.TestCase):
    def __init__(self, a):
        super().__init__(a)
        self.test = CoreElement(
                element="p", is_closing=True,
                is_add_attrs=True, attributes=["class", "style", "someattr"])
        self.test2 = CoreElement(
                element="img", is_closing=False,
                is_add_attrs=True, attributes=["class", "style", "someattr"]
                )

    def test_constructor(self):
        self.assertEqual(
            '<p class="" style="" someattr=""></p>',
            self.test.__str__())
        self.assertEqual(
            '<img class="" style="" someattr="" />',
            self.test2.__str__())

    def test_add_class(self):
        self.test._add_class("Test", "Test2")
        self.test2._add_class("Test", "Test2")
        self.assertEqual(
            '<p class="Test Test2 " style="" someattr=""></p>',
            self.test.__str__())
        self.assertEqual(
            '<img class="Test Test2 " style="" someattr="" />',
            self.test2.__str__())

    def test_add_style(self):
        self.test._add_style({"color": "black", "test": 25})
        self.test2._add_style({"color": "black", "test": 25})
        self.assertEqual(
            '<p class="" style="color:black; test:25; " someattr=""></p>',
            self.test.__str__())
        self.assertEqual(
            '<img class="" style="color:black; test:25; " someattr="" />',
            self.test2.__str__())

    def test_add_attr_value(self):
        self.test._add_attr_value("someattr", "test")
        self.test2._add_attr_value("someattr", "test")
        self.assertEqual(
            '<p class="" style="" someattr="test"></p>',
            self.test.__str__())
        self.assertEqual(
            '<img class="" style="" someattr="test" />',
            self.test2.__str__())

    def test_add_content(self):
        self.test.add_content("Some test", " another test")
        self.test2.add_content("Some test", " another test")
        self.assertEqual(
            '<p class="" style="" someattr="">Some test another test</p>',
            self.test.__str__())
        self.assertEqual(
            '<img class="" style="" someattr="" />',
            self.test2.__str__())
