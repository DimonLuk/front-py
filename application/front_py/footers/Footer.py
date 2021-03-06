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
from core import elements as e
from rows import ContainerRow


class Footer(e._FooterElement):
    """
    Parameters
    ----------

    content: str or object from framework
        content to be displayed
    """

    def __init__(self, content="", height=30):
        super().__init__()
        self._add_class("footer")
        self.row = ContainerRow()

        if content:
            self.row.add_content(content)
        self.height = height
        self._add_style({"padding-top": "%spx" %
                         (self.height/2), "padding-bottom": "%spx" %
                         (self.height/2)})

    def add_content(self, *content):
        self.row.add_content(*content)

    def _render(self):
        super().add_content(self.row)
        super()._render()

    def __setattr__(self, name, value):
        """
        Allows special syntax to set some css attributes.

        Parameters
        ----------

        name: str
            css property name but written in pythonic style, for example background-color is represented as background_color
        value: str
            css property value

        TODO
        realise more possibilities to customize this object
        """
        if name == "background_color":
            self._add_style({"background": value})
        else:
            self.__dict__[name] = value








import unittest


class Test(unittest.TestCase):

    def test_Footer(self):
        self.assertEqual("""<footer class="footer " style="padding-top:15.0px; padding-bottom:15.0px; "><div class="container " style=""><div class="row " style=""></div></div></footer>""", Footer().__str__())

    def test_Footer_add_content(self):
        a = Footer()
        a.add_content("test", a)
        self.assertEqual("""<footer class="footer " style="padding-top:15.0px; padding-bottom:15.0px; "><div class="container " style=""><div class="row " style="">test<footer class="footer " style="padding-top:15.0px; padding-bottom:15.0px; "><div class="container " style=""><div class="row " style="">test</div></div></footer></div></div></footer>""", a.__str__())

    def test_Footer__setattr__(self):
        a = Footer()
        a.background_color = "red"
        self.assertEqual("""<footer class="footer " style="padding-top:15.0px; padding-bottom:15.0px; background:red; "><div class="container " style=""><div class="row " style=""></div></div></footer>""", a.__str__())
