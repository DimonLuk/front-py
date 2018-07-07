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
from containers import SectionContainer
from BlockRow import BlockRow


class SectionRow(SectionContainer):
    """
    Creates a row inside SectionContainer
    """

    def __init__(self):
        super().__init__()
        self.row = BlockRow()

    def add_content(self, *content):
        self.row.add_content(*content)

    def _render(self):
        super().add_content(self.row)
        super()._render()








import unittest


class Test(unittest.TestCase):

    def test_SectionRow(self):
        self.assertEqual("""<section class="container " style=""><div class="row " style=""></div></section>""", SectionRow().__str__())

    def test_SectionRow_add_content(self):
        a = SectionRow()
        a.add_content("Test", a)
        self.assertEqual("""<section class="container " style=""><div class="row " style="">Test<section class="container " style=""><div class="row " style="">Test</div></section></div></section>""", a.__str__())
