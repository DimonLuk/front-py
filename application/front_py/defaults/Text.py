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


class Text(e._TextElement):
    """
    It can be used as wrapper, you can define some simple styles and use it to wrap text
    For example:
    >>> greenText = Text()
    >>> greenText.color = "green" or greenText.addStyle({"color":"green"})
    >>> p = Paragraph("Some %s text" % greenText("green"))

    Or you can use this class in usual way

    Parameters
    ----------

    text: str
        just text
    """

    def __init__(self, text=""):
        super().__init__(text=text)

    def __setattr__(self, name, value):
        if name == "color":
            self._add_style({"color": value})
        elif name == "position" and value == "center":
            # To place in center in .container > .row
            self._add_class("mx-auto")
            self._add_style({"text-align": value})  # Sometimes it's useful
        elif name == "decor" and value == "crossed":
            self._add_style({"text-decoration": "line-through"})
        else:
            self.__dict__[name] = value

    def addStyle(self, style):
        self._add_style(self, style)







import unittest


class Test(unittest.TestCase):

    def test_Text(self):
        self.assertEqual("""<span class="" style=""></span>""", Text().__str__())

    def test_Text__setattr__(self):
        a = Text("test")
        a.color = "red"
        self.assertEqual("""<span class="" style="color:red; ">test</span>""", a.__str__())
