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


class NumberedList(e._NumberedListElement):
    def __init__(self, content_style={}, *content):
        super().__init__()
        self.li = e._InListElement()
        self.li._add_style(content_style)
        if content:
            for i in content:
                self.add_content(self.li(i))

    def add_elements(self, *elements):
        for i in elements:
            self.add_content(self.li(i))

    def __call__(self, *elements):
        import copy
        cop = copy.deepcopy(self)
        cop.add_elements(*elements)
        cop._render()
        return cop._template








import unittest


class Test(unittest.TestCase):

    def test_NumberedList(self):
        self.assertEqual("""<ol class="" style=""></ol>""", NumberedList().__str__())

    def test_NumberedList_add_elements(self):
        a = NumberedList()
        a.add_elements("Test", a)
        self.assertEqual("""<ol class="" style=""><li class="" style="">Test</li><li class="" style=""><ol class="" style=""><li class="" style="">Test</li></ol></li></ol>""", a.__str__())

    def test_NumberedList__call__(self):
        a = NumberedList()
        self.assertEqual("""<ol class="" style=""><li class="" style="">Test</li><li class="" style=""><ol class="" style=""></ol></li></ol>""", a("Test", a))
